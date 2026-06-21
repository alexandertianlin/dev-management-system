#!/usr/bin/env python3
"""
Auto-heal: 自动修复 enforce_check.py 检测出的常见违规。

用法:
    python scripts/auto_heal.py                              # 扫描并修复
    python scripts/auto_heal.py --dry-run                    # 预览不执行
    python scripts/auto_heal.py --violation C-06 --task hand-tracking  # 针对修复

从 enforce_check.py 调用:
    from auto_heal import auto_heal
    fixed = auto_heal(violations, dry_run=True)
"""

import argparse, os, re, shutil, sys
from pathlib import Path
from datetime import datetime
from typing import List, Tuple

Violation = Tuple[str, str, str]

SCRIPT_DIR = Path(__file__).resolve().parent
DEV_DIR = SCRIPT_DIR.parent
CODEX_ROOT = DEV_DIR.parent
SKILLS_DIR = CODEX_ROOT / "skills"
MEMORY_DIR = CODEX_ROOT / "memory"
TASKS_DIR = CODEX_ROOT / "tasks"

TODAY = datetime.now().strftime("%Y%m%d")

TEMPLATE_VERSION_SPEC = f"""# 版本说明书

> 本文件由 auto_heal.py 自动生成，请补充完整内容。

## 1. 版本元信息
- **所属任务**: {{task_name}}
- **版本号**: {{version_name}}
- **状态**: in_progress

## 2. 开发记录
（待补充）

---

> **最后更新**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
"""

TEMPLATE_MEMORY = f"""# 任务记忆 — {{task_name}}

## Session: {datetime.now().strftime("%Y-%m-%d %H:%M")} — 自动创建

### 关键决策
（待补充）

### 遗留事项
（待补充）

---

> **最后更新**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
"""


def auto_heal(violations: List[Violation], dry_run: bool = False) -> Tuple[int, int, List[str]]:
    """自动修复可修复的违规。
    
    Returns:
        (fixed_count, failed_count, messages)
    """
    fixed = 0
    failed = 0
    messages = []

    for cid, level, desc in violations:
        msg = None
        
        # C-06: 缺子目录
        if cid == "C-06" and "缺" in desc:
            # 解析: "task-xxx/v1.0: 缺 src/"
            parts = desc.split(": ")
            if len(parts) >= 2:
                path_part = parts[0].strip()
                subdir_part = parts[1].replace("缺 ", "").replace("/", "")
                fp = TASKS_DIR / path_part / subdir_part
                if dry_run:
                    msg = f"[DRY-RUN] 将创建: {fp}"
                else:
                    fp.mkdir(parents=True, exist_ok=True)
                    gitkeep = fp / ".gitkeep"
                    gitkeep.touch()
                    msg = f"已创建: {fp}"
        
        # C-03: 缺 _VERSION_SPEC.md
        elif cid == "C-03" and "缺 _VERSION_SPEC.md" in desc:
            parts = desc.split(": ")
            if len(parts) >= 2:
                task_ver = parts[0].strip()  # task-hand-tracking/v1.0-feat-xxx
                ver_dir = TASKS_DIR / task_ver
                spec_path = ver_dir / "_VERSION_SPEC.md"
                if not spec_path.exists() and ver_dir.is_dir():
                    if dry_run:
                        msg = f"[DRY-RUN] 将创建: {spec_path}"
                    else:
                        # Parse task name and version from path
                        task_name = task_ver.split("/")[0] if "/" in task_ver else task_ver
                        ver_name = task_ver.split("/")[1] if "/" in task_ver else ""
                        content = TEMPLATE_VERSION_SPEC.format(
                            task_name=task_name, version_name=ver_name
                        )
                        spec_path.write_text(content, encoding="utf-8")
                        msg = f"已创建: {spec_path}"
                    fixed += 1
                    messages.append(msg)
                    continue
        
        # C-08: 无 memory-*.md
        elif cid == "C-08" and "无 memory-*" in desc:
            # 解析: "memory/task-xxx/ 无 memory-*.md"
            task_name = desc.split("/")[0].replace("memory/", "").strip()
            mem_dir = MEMORY_DIR / task_name
            if not mem_dir.exists():
                if dry_run:
                    msg = f"[DRY-RUN] 将创建目录并生成 Memory: {mem_dir}"
                else:
                    mem_dir.mkdir(parents=True, exist_ok=True)
                    mem_file = mem_dir / f"memory-{TODAY}.md"
                    content = TEMPLATE_MEMORY.format(task_name=task_name)
                    mem_file.write_text(content, encoding="utf-8")
                    msg = f"已创建: {mem_file}"

        if msg:
            messages.append(msg)
            if msg.startswith("已创建") and not dry_run:
                fixed += 1
            elif msg.startswith("[DRY-RUN]") and not dry_run:
                fixed += 1
            else:
                failed += 1

    return fixed, failed, messages


def main():
    p = argparse.ArgumentParser(description="Auto-heal for dev compliance")
    p.add_argument("--dry-run", "-d", action="store_true", help="预览不执行")
    p.add_argument("--violation", help="指定违规编号（如 C-06），否则修复全部")
    p.add_argument("--task", help="限定任务名称")
    args = p.parse_args()

    from enforce_check import check_core_docs, check_tasks, check_skills_memory
    all_v = check_core_docs() + check_tasks() + check_skills_memory()

    if args.task:
        all_v = [v for v in all_v if args.task in v[2]]
    if args.violation:
        all_v = [v for v in all_v if v[0] == args.violation]

    if not all_v:
        print("无违规项需要修复。")
        return

    print(f"=== Auto-heal ({'DRY RUN' if args.dry_run else '执行'}） ===")
    for cid, lv, desc in sorted(all_v):
        print(f"  [{lv}] {cid}: {desc}")

    fixed, failed, msgs = auto_heal(all_v, dry_run=args.dry_run)
    print(f"\n结果: 修复 {fixed} 项, 失败 {failed} 项")
    for m in msgs:
        print(f"  {m}")

    if args.dry_run:
        print(f"\n实际执行: python {__file__}")


if __name__ == "__main__":
    main()

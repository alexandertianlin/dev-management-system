# Deployment Guide / 部署指南

## Prerequisites

- Python 3.8+
- Windows (for native `cd /d` support) or Linux/macOS
- Codex desktop app (for AGENTS.md integration)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/alexandertianlin/dev-management-system.git
cd dev-management-system
```

### 2. Set up environment

```bash
python -m pip install -r requirements.txt
```

### 3. Add to Codex path (optional)

Copy or symlink the `dev-management-system` folder to your Codex root:

```bash
# Windows
robocopy /e dev-management-system C:\Users\tianl\Documents\Codex\dev-management-system

# Linux/macOS
cp -r dev-management-system /path/to/codex/
```

### 4. Integrate with AGENTS.md

Append to `~/.codex/AGENTS.md`:

```markdown
## 开发管理流程强制指令

### 核心全局路径定义
- **管理系统根目录**: C:\Users\tianl\Documents\Codex\dev-management-system\
- **全局技能库 (Skills)**: C:\Users\tianl\Documents\Codex\skills\
- **全局记忆库 (Memory)**: C:\Users\tianl\Documents\Codex\memory\
- **全局任务空间 (Tasks)**: C:\Users\tianl\Documents\Codex\tasks\
```

### 5. Verify installation

```bash
# Run compliance check
python scripts/enforce_check.py

# Run with auto-heal (pass@3)
python scripts/enforce_check.py --pass-n 3 --heal
```

## Directory Structure Requirements

```
Codex Root/
├── dev-management-system/    ← This repo
├── skills/                   ← Global skill library
├── memory/                   ← Global memory store
├── tasks/                    ← Task workspace
│   ├── task-<id>/
│   │   ├── _TASK_SPEC.md
│   │   └── vX.Y-feat-<feature>-<YYYYMMDD>/
│   │       ├── _VERSION_SPEC.md
│   │       └── src/config/lib/requirements/
```

## Commands Reference

| Command | Description |
|---------|-------------|
| `python scripts/enforce_check.py` | Basic compliance check |
| `python scripts/enforce_check.py --pass-n 3` | Require 3 consecutive passes |
| `python scripts/enforce_check.py --pass-n 3 --heal` | Full CI with auto-repair |
| `python scripts/enforce_check.py --quiet` | Silent mode |
| `python scripts/auto_heal.py --dry-run` | Preview auto-fixes |
| `make check` | Compliance check (via Make) |
| `make heal` | Check + heal (via Make) |
| `make ci` | Full pipeline (via Make) |

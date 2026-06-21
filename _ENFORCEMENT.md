
# ⚠️ 违规处罚条例（增强版）

> 本文档与 _DEVELOPMENT_PROCEDURE.md 配套使用。
> 违反开发管理总规程者，将依据本条例进行处罚。**处罚即时生效，不容申诉。**

---

## 1. 处罚等级

| 等级 | 名称 | 触发条件 | 处罚措施 |
|------|------|----------|----------|
| L1 | **警告** | 首次轻微违规（遗漏 Memory、文件放错子目录、commit 格式错误） | 记录违规日志，自动修复或要求更正后继续 |
| L2 | **停工作业** | 首次中等违规（未写 _VERSION_SPEC.md、未声明 Skill、版本名不合规） | **立即停止工作**，重新阅读 _DEVELOPMENT_PROCEDURE.md 全文，确认理解后方可恢复 |
| L3 | **强制回退** | 严重违规（未注册任务即开发、未写 _TASK_SPEC.md、CI 未过擅自合并） | 立即停止工作，回退到上一个合规检查点，阅读 _DEVELOPMENT_PROCEDURE.md + _ENFORCEMENT.md 全文 |
| L4 | **任务终止** | 同类型违规累计 3 次 | 终止当前任务，任务标记为 FAILED，需人工审核方可重新开始 |

## 2. 违规检测清单

| 编号 | 违规行为 | 等级 | 检测方式 |
|------|----------|------|----------|
| V-01 | 未在 _TASK_REGISTRY.md 注册任务 | L3 | 人工 / enforce_check.py |
| V-02 | 未创建 _TASK_SPEC.md | L3 | enforce_check.py |
| V-03 | 未创建 _VERSION_SPEC.md | L2 | enforce_check.py |
| V-04 | 文件未按 src/config/lib/requirements 分类 | L1 | enforce_check.py |
| V-05 | 模型文件未放入 models/ | L1 | enforce_check.py |
| V-06 | 未记录 Memory 文件 | L1 | enforce_check.py |
| V-07 | 版本名不符合规范 | L2 | enforce_check.py |
| V-08 | 声明了 Skill 但 skill 文件不存在 | L2 | enforce_check.py |
| V-09 | 任务目录结构不符合规范 | L3 | enforce_check.py |
| V-10 | Git Commit Message 不符合 Angular 规范 | L1 | Git Hook |
| V-11 | CI 未通过即合并 PR | L3 | 人工 |
| V-12 | 同类型违规再次发生（第 2 次） | L2+ | 累计 |
| V-13 | 同类型违规第三次发生 | L4 | 累计 |

## 3. 违规处理流程

```
检测到违规 → 确定等级 (L1-L4)
  L1: 记录日志 → 自动修复 → 继续工作
  L2: 立即停止 → 显示违规信息 → 用户确认已阅读规程 → 继续
  L3: 立即停止 → 回退到上一检查点 → 用户确认已阅读规程+本条例 → 继续
  L4: 立即停止 → 标记任务 FAILED → 通知人工审核 → 终止
```

### L2 / L3 恢复步骤

1. 立即停止所有开发操作
2. 记录违规信息到 memory/（注明 violation ID）
3. 重新读取 _DEVELOPMENT_PROCEDURE.md 全文
4. （L3 额外）重新读取 _ENFORCEMENT.md 全文
5. 确认理解后在任务文档中签署确认
6. 恢复工作

## 4. 违规日志格式

每次违规必须记录到对应任务 Memory 中：

```
## VIOLATION
- Violation ID: V-{编号}
- Level: L{等级}
- Timestamp: {YYYY-MM-DD HH:mm}
- Description: {违规描述}
- Action Taken: {处罚措施}
- Resolution: {L2/L3: 已重读规程 / L4: 标记 FAILED}
```

## 5. 启动检查

**每次开始一个新任务 / 新版本时，必须先执行以下检查：**

1. [ ] 读取 _DEVELOPMENT_PROCEDURE.md
2. [ ] 读取 _ENFORCEMENT.md
3. [ ] 读取 _AGENTS_INTEGRATION.md
4. [ ] 检查 _TASK_REGISTRY.md 中任务是否已注册
5. [ ] 检查 _TASK_SPEC.md 是否存在且内容完整
6. [ ] 检查所需 Skill 是否在 skills/ 中可用
7. [ ] 检查所需 Memory 是否存在

**未完成以上检查即开始工作 → 触发 L3 处罚。**

---

> **最后更新**: 2026-06-18
> **版本**: v2.0.0

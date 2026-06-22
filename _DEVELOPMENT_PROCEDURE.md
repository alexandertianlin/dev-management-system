# 预警 开发管理总规程（完整版）

> 本文档是开发管理监督流程的核心规章制度。在开始任何开发任务之前，必须完整阅读本文档。
> 违反本文档中的任何条款将触发 _ENFORCEMENT.md 中的处罚机制。

---

## 1. 总则

### 1.1 宗旨

建立一套标准化、可追溯、可集成、可自动化的开发管理流程。杜绝以散乱的时间标记代替规范版本管理的做法。

每个任务必须有明确的任务说明书、版本记录、资源索引，确保最终能够将不同组件的不同版本集成到统一的交付物中。

### 1.2 适用范围

适用于工作室及 Codex 环境内的所有开发任务，包括但不限于：模型训练、数据采集、传感器驱动、手势识别算法、三维重建、集成测试等。

## 2. 目录结构规范

### 2.1 顶层结构

以下是 Codex 根目录的黄金结构：

 C:/Users/tianl/Documents/Codex/          ← Codex 根目录
│
├── dev-management-system/         ← ⚙️ 全局管理系统（制度 + 校验脚本 + 总账本）
│   ├── _DEVELOPMENT_PROCEDURE.md   ← 本文件（总规程）
│   ├── _ENFORCEMENT.md             ← 违规处罚条例
│   ├── _AGENTS_INTEGRATION.md      ← Codex 启动自检流程
│   ├── _TASK_REGISTRY.md           ← 全局任务注册数据库
│   ├── _INTEGRATION_MANIFEST.md    ← 集成清单
│   └── scripts/
│       └── enforce_check.py        ← 合规检查工具（pathlib 动态寻址）
│
├── skills/                         ← 🧠 全局技能库（跨任务复用）
│   ├── hand-tracking/
│   ├── depth-processing/
│   └── camera-calibration/
│
├── memory/                         ← 📝 全局记忆库（跨任务继承）
│   ├── task-d435i-integration/
│   ├── task-hand-tracking/
│   └── task-model-training/
│
├── tasks/                          ← 📂 全局任务空间（长期迭代）
│   ├── task-d435i-integration/
│   ├── task-hand-tracking/
│   └── task-model-training/
│
└── shared/                         ← 📦 跨任务共享资源
    ├── scripts/
    ├── config-templates/
    ├── src/
    ├── lib/
    └── models/

### 2.2 任务目录结构

任务目录位于 Codex 根目录的 tasks/ 下。

 {Codex 根}/tasks/task-{name}/
├── _TASK_SPEC.md                 ← 任务说明书（必须）
├── _common/                      ← 该任务所有版本共享的资源
│   ├── src/
│   ├── config/
│   ├── lib/
│   └── requirements/
├── models/                       ← 该任务的模型文件统一存放
├── v1.0-feat-{feature}-{YYYYMMDD}/
│   ├── _VERSION_SPEC.md          ← 版本说明书（必须）
│   ├── src/
│   ├── config/
│   ├── lib/
│   └── requirements/
├── v1.1-feat-{feature}-{YYYYMMDD}/
└── v2.0-feat-{feature}-{YYYYMMDD}/

### 2.3 版本命名规则

格式： v{major}.{minor}-{feature_key}-{YYYYMMDD}

- 版本号确保按时间排序
- 特征描述使用英文（如 baseline, calibration, yolo）


### 3.6 推荐的项目文件

每个任务目录应包含以下项目基础设施文件（来自 skills/task-automation 最佳实践）：

| 文件 | 用途 | 模板位置 |
|------|------|----------|
| Makefile | 一键命令（setup/clean/help） | shared/config-templates/Makefile |
| .gitignore | 忽略规则（缓存/密钥/输出） | shared/config-templates/dot_gitignore |
| .gitattributes | 跨平台换行符 | shared/config-templates/gitattributes |
| requirements.txt | 依赖锁定 | 任务自定义 |

Makefile 标准目标：
- make setup — 安装依赖
- make clean — 清理缓存
- make help — 查看可用命令

---

> 最后更新: 2026-06-18
> 版本: v2.0.0


### 阶段一：任务初始化与就绪 (Initialization)
1. 检查 _TASK_REGISTRY.md 注册状态。
2. **终端自动化重定向**：Agent 必须根据当前 <task-id>，主动输出：
   ```cmd
   cd /d C:\\Users\\tianl\\Documents\\Codex\\tasks\\<task-id>\\
   ```
3. 严禁在未切换至对应任务根目录的情况下让用户或系统执行任何 Python 或 Git 命令。
## 3. 任务生命周期

每个任务经历五个阶段：

注册 → 规划 → 开发 → 验证 → 归档/集成

### 3.1 注册
在 _TASK_REGISTRY.md 中添加一条新记录，包含：任务 ID、名称、目标、依赖、登记时间。

### 3.2 规划
在全局 tasks/{task-id}/_TASK_SPEC.md 中填写任务说明书。

### 3.3 开发
每个版本开发流程：
1. 创建版本目录：v{major}.{minor}-{feature_key}-{YYYYMMDD}
2. 创建 _VERSION_SPEC.md
3. 文件归入 src/config/lib/requirements 子目录
4. 模型文件放入 models/（任务级）
5. 跨版本公共文件放入 _common/
6. 更新 Memory：memory/{task-id}/memory-{YYYYMMDD}.md
7. 更新 Skill：可复用能力写入全局 skills/

### 3.4 验证
运行 enforce_check.py 验证合规。

### 3.5 归档 / 集成
在 _INTEGRATION_MANIFEST.md 中记录集成信息。

---

## 4. Git 工作流与代码规范

### 4.1 分支管理（Git Flow 简化版）

| 分支 | 用途 | 保护规则 |
|------|------|----------|
| main | 生产分支 | 受保护，只能通过 Release PR 合并 |
| develop | 开发主干 | 所有 feature/hotfix 分支的集散地 |
| feature/{task-id}-{desc} | 功能开发 | 从 develop 切出，完成合并回 develop |

### 4.2 Commit Message 规范

格式：<type>(<scope>): <subject>

| Type | 说明 |
|------|------|
| feat | 新功能 |
| fix | 修补 bug |
| docs | 文档修改 |
| refactor | 重构 |
| test | 增加测试 |

示例：feat(task-hand-tracking): add MediaPipe 21-keypoint detection

### 4.3 代码风格

| 语言 | 工具 | 规范 |
|-----------|------|------|
| Python | Ruff / Black | PEP 8, Pydantic 类型注解 |
| JS/TS | Prettier | 统一排版 |

---

## 5. Skill 管理规范

### 5.1 原则
- 原子化与单一职责：一个 Skill 只做一件事
- 严格的输入输出声明：必须使用 Pydantic Schema
- 内置自愈与异常处理：不直接 Crash
- 文档即代码：Docstring = LLM Prompt

### 5.2 目录结构

skills/{name}/
├── SKILL.md          ← 技能说明文档
├── schema.py         ← Pydantic 输入输出 Schema
├── impl.py           ← 实现代码
└── tests/            ← 单元测试

---

## 6. Memory 管理规范

### 6.1 分层存储

| 层级 | 存储介质 | 有效期 | 内容 |
|------|----------|--------|------|
| 短期记忆 | 内存 | TTL 过期 | 当前 Session 对话历史 |
| 长期记忆 | memory/ 文件系统 | 持久化 | 关键决策、技术方案、问题解决记录 |

### 6.2 Memory 文件格式

memory/{task-id}/memory-{YYYYMMDD}.md

包含：Session 标题、关键决策、技术方案、问题与解决、遗留事项

---

## 7. CI/CD 流水线

### 7.1 本地防线
运行 enforce_check.py 确保目录结构合规。

### 7.2 远端 CI
当 PR 提交时，GitHub Actions 自动执行：
- 镜像检查整体目录结构
- 验证所有 _TASK_SPEC.md 和 _VERSION_SPEC.md 存在
- 运行 enforce_check.py

见 .github/workflows/ci-cd.yml

-

## 8. 违规处理

任何检测到未按本规程操作的情况，将触发 _ENFORCEMENT.md 中的处罚流程。

违规场景包括：未注册任务、未编写 _TASK_SPEC.md / _VERSION_SPEC.md、文件未按目录分类、模型文件未放入 models/、未记录 Memory、版本号不符合规范、CI 未通过善自合并。

> 最后更新: 2026-06-18 | 版本: v3.0.0

## 9. Git Push 规范

Agent 在完成 commit 后必须自动输出标准化的 git push 命令：

`cmd
cd /d C:\Users\tianl\Documents\Codex\<仓库路径>\
git push origin <分支名>
`

禁止让用户询问如何推送。此命令应与 cd /d 同样作为 Agent 输出的标准格式。
---

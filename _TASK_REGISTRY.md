?
 # 任务注册中心
 > **本文件是任务管理数据库。所有开发任务必须先在此注册方可开始�?*
 > 注册即创建一条记录，标记任务状态并分配任务 ID�?
 ---
 ## 任务注册表（数据库）
 | 任务 ID | 任务名称 | 目标 | 依赖任务 | 状�?| 登记时间 |
 |---------|----------|------|----------|------|----------|
 | task-hand-tracking | 手势追踪系统开�?| 构建基于 Astra Plus + MediaPipe 的实时手势追踪系�?| task-model-training | in_progress | 2026-06-01 09:00 |
 | task-model-training | 手势检测模型训�?| 训练 YOLOv8 手势检测模型，支持 ONNX 部署 | �?| in_progress | 2026-06-01 14:00 |
 | task-d435i-integration | D435i 多模态信号读�?| 读取 Intel RealSense D435i �?RGB、红外、深度信号并实现多模态同�?| task-hand-tracking | in_progress | 2026-06-18 15:00 |
 ### 状态说�?
 | 状�?| 含义 |
 |------|------|
 | `registered` | 已注册，尚未开�?|
 | `in_progress` | 开发中 |
 | `paused` | 暂时暂停 |
 | `completed` | 已完�?|
 | `failed` | 任务终止（L4 处罚触发�?|
 | `archived` | 已归�?|
 ---
 ## 版本汇�?
 | 任务 ID | 版本 | 特征 | 日期 | 状�?|
 |---------|------|------|------|------|
 | task-hand-tracking | v1.0-feat-baseline-20260601 | 基础 MediaPipe 检测管�?| 2026-06-01 | completed |
 | task-hand-tracking | v1.1-feat-calibration-20260605 | ChArUco 标定�?RGB-D 对齐 | 2026-06-05 | completed |
 | task-hand-tracking | v1.2-feat-depthfusion-20260610 | 深度图融合优�?| 2026-06-10 | in_progress |
 | task-hand-tracking | v2.0-feat-d435i-hand-20260621 | D435i + MediaPipe Hand 基础检测 | 2026-06-21 | completed
 | task-hand-tracking | v2.1-feat-unity-bridge-20260621 | D435i + MediaPipe Hand -> Unity UDP bridge | 2026-06-21 | completed
 | task-hand-tracking | v2.2-feat-direct-hand-control-20260621 | MediaPipe 直接驱骨（独立脚本,端口5056）| 2026-06-21 | in_progress
 | task-hand-tracking | v2.3-feat-fingersolver-integration-20260621 | MediaPipe -> FingerSolver 管线集成（端口5057）| 2026-06-21 | in_progress | |
 | task-hand-tracking | v2.2-feat-mediapipe-control-20260621 | [已替代] MediaPipe -> FingerSolver IK 管线集成 | 2026-06-21 | paused | | |
 | task-hand-tracking | v2.0-feat-unity-20260620 | Unity 集成（暂缓，等待基础版本完成）| 2026-06-20 | paused |
 | task-model-training | v1.0-feat-yolo-20260601 | YOLOv8 基线训练 | 2026-06-01 | completed |
 | task-model-training | v1.1-feat-quant-20260608 | FP16/INT8 量化 | 2026-06-08 | in_progress |
 | task-model-training | v1.2-feat-onnx-20260612 | ONNX 导出与优�?| 2026-06-12 | registered |
 | task-d435i-integration | v1.0-feat-baseline-20260618 | librealsense SDK 基线 �?RGB/IR/Depth 同步读取 | 2026-06-18 | completed |
| task-d435i-integration | v1.1-feat-streamtool-20260618 | multimodal stream collector - RGB/IR/Depth + IMU display/recording | 2026-06-18 | in_progress |
| task-xiaohongshu-auto-post | v1.0-feat-baseline-20260620 | 基线版本: 集成 white0dew/XiaohongshuSkills 开源方案 | 2026-06-20 | in_progress |
 | task-cc-switch-token | CC-Switch Token ???? | ? CC-Switch ?? SQLite ????? token ????????? | ? | in_progress | 2026-06-20 23:00 |
 ---
 > **最后更新**: 2026-06-21

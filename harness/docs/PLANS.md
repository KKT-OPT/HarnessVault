---
documentName: docs/PLANS.md
title: Harness 阶段计划
aliases:
  - PLANS
  - Harness Plans
  - 阶段计划
tags:
  - harness
  - plan
  - governance
version: v0.1.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-29 00:00:00.000 +08:00
status: draft
type: plan
purpose: 记录 HarnessVault 当前阶段目标、验收标准和后续落地计划。
scope: HarnessVault 通用文档系统。
prerequisites:
  - AGENTS.md
  - docs/INDEX.md
relatedDocuments:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-29 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P0 - HarnessVault 基础仓库结构治理`

目标是在 [[HarnessEngineering]] v1.1.0 的基础上，补齐最小可用文档入口、索引、计划、Obsidian Dashboard 和模板骨架，避免仓库继续被 IDE 状态、Obsidian workspace 状态和插件运行代码污染。

## 2. P0 验收标准

P0 完成标准：

1. 仓库根目录存在 `README.md` 和 `AGENTS.md`。
2. `harness/` 被明确为 Obsidian vault root。
3. `harness/AGENTS.md` 存在并定义智能体入口契约。
4. `harness/docs/INDEX.md` 存在并链接核心文档。
5. `harness/docs/PLANS.md` 存在并记录当前阶段计划。
6. `harness/docs/Dashboard.md` 存在，提供 Dataview 动态视图。
7. `harness/templates/` 存在最小模板骨架。
8. `.gitignore` 已防止后续提交 IDE 状态、Obsidian workspace 状态和插件运行代码。
9. 已跟踪的 `.idea/` 与 Obsidian 插件运行代码已在临时分支中删除或准备删除。
10. 本次变更通过临时分支提交，不直接合并到 `main`。

## 3. P1 建议任务

P1：拆分核心治理子文档。

建议优先拆分：

1. `docs/governance/ArtifactLifecycle.md`
2. `docs/governance/ScheduledGovernance.md`
3. `docs/governance/SecurityGovernance.md`
4. `docs/governance/IndexMaintenancePolicy.md`
5. `docs/governance/SkillGovernance.md`
6. `docs/governance/MemoryGovernance.md`

## 4. P2 建议任务

P2：落地 Agent / Skill / Memory 基础文档。

建议优先拆分：

1. `docs/agent/ContextLoadingPolicy.md`
2. `docs/agent/SkillPolicy.md`
3. `docs/agent/MemoryPolicy.md`
4. `docs/agent/skills/SkillIndex.md`
5. `docs/agent/memory/MemoryIndex.md`
6. `docs/agent/skills/_TEMPLATE/SKILL.md`

## 5. P3 建议任务

P3：落地 RAG 和 Project Template。

建议优先拆分：

1. `docs/rag/RAGIndex.md`
2. `docs/rag/KnowledgeBasePolicy.md`
3. `docs/project-template/ProjectIndex.md`
4. `docs/project-template/architecture/ARCHITECTURE.md`
5. `docs/project-template/dictionary/SemanticDictionary.md`
6. `docs/project-template/workflow/WorkflowTemplate.md`

## 6. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 文件进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 不要在未建立治理报告前自动修改长期资产。
5. 重大架构变化应走分支和 PR。

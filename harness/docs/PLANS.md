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
version: v0.2.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-30 00:00:00.000 +08:00
status: draft
type: plan
purpose: 记录 HarnessVault 当前阶段目标、验收标准和后续落地计划。
scope: HarnessVault 通用文档系统。
prerequisites:
  - AGENTS.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
  - "[[AgentIndex]]"
  - "[[RAGIndex]]"
  - "[[ProjectIndex]]"
  - "[[Dashboard]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-29 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P1 - HarnessVault 计划与索引治理收口`

P1 的目标是在 [[HarnessEngineering]] v1.1.0 的基础上，完成当前仓库文档结构、阶段计划、分层索引和治理报告入口的收口，使 HarnessVault 从“架构占位文档初始化阶段”进入“核心治理文档实质化阶段”。

## 2. P0 状态

P0：`HarnessVault 基础仓库结构治理`

状态：`completed`

已完成：

1. 仓库根目录存在 `README.md` 和 `AGENTS.md`。
2. `harness/` 已明确为 Obsidian vault root。
3. `harness/AGENTS.md` 已定义 vault 内智能体入口契约。
4. `harness/docs/INDEX.md` 已升级为顶层分层索引。
5. `harness/docs/PLANS.md` 已建立阶段计划入口。
6. `harness/docs/Dashboard.md` 已建立 Dataview 动态视图。
7. `harness/templates/` 已建立基础模板骨架。
8. `.gitignore` 已按 IDEA + Obsidian 场景修正。
9. Obsidian Git 已不作为推荐维护方式。
10. `workspace.json` 和插件运行代码不再作为 Harness 事实源。

## 3. P1 目标

P1 聚焦计划与索引治理收口，不展开所有政策正文。

P1 要完成：

1. 更新本计划文档，标记 P0 完成并进入 P1。
2. 确认当前仓库 `harness/` vault root 与设计稿中 `docs/` 路径的映射关系已由 `README.md`、`AGENTS.md`、[[INDEX]] 和 [[ObsidianSetup]] 承载。
3. 确认顶层 [[INDEX]] 只链接各架构层 index。
4. 确认各架构层 index 已能链接本层占位文档。
5. 新增治理报告目录占位文档。
6. 给出 P2 的核心治理文档实质化拆分清单。

## 4. P1 验收标准

P1 完成标准：

1. [[INDEX]] 指向 [[GovernanceIndex]]、[[AgentIndex]]、[[RAGIndex]]、[[ProjectIndex]]、[[ReportsIndex]]、[[ObsidianSetup]]、[[Dashboard]]。
2. [[GovernanceIndex]] 指向治理层占位文档。
3. [[AgentIndex]] 指向 Agent 能力层占位文档。
4. [[RAGIndex]] 指向知识库治理文档。
5. [[ProjectIndex]] 指向项目模板层说明。
6. `docs/reports/README.md` 存在。
7. `docs/reports/governance/README.md` 存在。
8. `docs/reports/index/README.md` 存在。
9. 当前阶段不再描述过期的 P0 临时分支状态。
10. 下一阶段 P2 的拆分清单明确。

## 5. P2 建议任务

P2：`核心治理规则实质化`

建议优先实质化以下文档：

1. `docs/governance/IndexMaintenancePolicy.md`
2. `docs/agent/ContextLoadingPolicy.md`
3. `docs/governance/ArtifactLifecycle.md`
4. `docs/governance/ScheduledGovernance.md`
5. `docs/agent/SkillPolicy.md`
6. `docs/agent/MemoryPolicy.md`

优先级说明：

1. `IndexMaintenancePolicy.md` 决定所有新增、移动、归档文档如何更新索引。
2. `ContextLoadingPolicy.md` 决定智能体面对不同任务时应读取哪些上下文。
3. `ArtifactLifecycle.md` 决定文档、Skill、Memory、RAG、Workflow 的状态迁移。
4. `ScheduledGovernance.md` 决定定期治理的 dry-run、报告和人工审批规则。
5. `SkillPolicy.md` 和 `MemoryPolicy.md` 用于防止长期项目中的 Skill / Memory 污染。

## 6. P3 建议任务

P3：`Project Template 最小实例化能力`

建议优先落地：

1. `docs/project-template/README.md`
2. `docs/project-template/architecture/ARCHITECTURE.md`
3. `docs/project-template/dictionary/SemanticDictionary.md`
4. `docs/project-template/git/Repository.md`
5. `docs/project-template/workflow/WorkflowTemplate.md`

P3 的目标是让 HarnessVault 可以被复制到真实项目，并能快速形成 Project Harness Instance。

## 7. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 不要在未建立治理报告前自动修改长期资产。
5. 重大架构变化应走分支和 PR。
6. 当前阶段不要一次性写满所有政策文档，应优先稳定索引、计划和治理报告入口。

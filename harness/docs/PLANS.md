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
version: v0.3.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
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
  - "[[ReportsIndex]]"
  - "[[Dashboard]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P2 - 核心治理规则实质化`

P2 的目标是在 P1 已完成的索引、计划和报告入口基础上，将最关键的 6 个占位文档升级为可执行治理规则，使智能体可以按规则加载上下文、维护索引、判断文档生命周期，并受控地处理 Skill 与 Memory。

## 2. P0 状态

P0：`HarnessVault 基础仓库结构治理`

状态：`completed`

已完成：

1. 仓库根目录存在 `README.md` 和 `AGENTS.md`。
2. `harness/` 已明确为 Obsidian vault root。
3. `harness/AGENTS.md` 已定义 vault 内智能体入口契约。
4. `harness/docs/INDEX.md` 已建立顶层分层索引。
5. `harness/docs/Dashboard.md` 已建立 Dataview 动态视图。
6. `harness/templates/` 已建立基础模板骨架。
7. `.gitignore` 已按 IDEA + Obsidian 场景修正。

## 3. P1 状态

P1：`HarnessVault 计划与索引治理收口`

状态：`completed`

已完成：

1. [[INDEX]] 已指向 [[GovernanceIndex]]、[[AgentIndex]]、[[RAGIndex]]、[[ProjectIndex]]、[[ReportsIndex]]、[[ObsidianSetup]]、[[Dashboard]]。
2. 各架构层 index 已能链接本层占位文档。
3. `docs/reports/README.md`、`docs/reports/governance/README.md`、`docs/reports/index/README.md` 已建立。
4. 当前阶段不再描述过期的 P0 临时分支状态。
5. P2 的核心治理规则实质化清单已明确。

## 4. P2 目标

P2 聚焦核心治理规则实质化，不扩展 Project Template，不新增运行时代码。

P2 要完成以下文档的正文实质化：

1. `docs/governance/IndexMaintenancePolicy.md`
2. `docs/agent/ContextLoadingPolicy.md`
3. `docs/governance/ArtifactLifecycle.md`
4. `docs/governance/ScheduledGovernance.md`
5. `docs/agent/SkillPolicy.md`
6. `docs/agent/MemoryPolicy.md`

## 5. P2 验收标准

P2 完成标准：

1. [[IndexMaintenancePolicy]] 能指导新增、移动、归档、删除文档时应更新哪些 index。
2. [[ContextLoadingPolicy]] 能指导智能体按任务类型加载最小必要上下文。
3. [[ArtifactLifecycle]] 能定义文档、Skill、Memory、RAG、Workflow、Report 的状态迁移。
4. [[ScheduledGovernance]] 能定义 dry-run、报告优先、人工审批和允许自动修复的边界。
5. [[SkillPolicy]] 能定义 Skill 的使用、创建、更新、合并、归档和污染控制。
6. [[MemoryPolicy]] 能定义 Memory 的读取、写入、候选生成、晋升、归档和污染控制。
7. 本阶段不修改 `main`，通过 P2 分支和 PR 交付。

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
6. 当前阶段只实质化核心治理规则，不扩展项目模板细节。

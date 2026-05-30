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
version: v0.4.0
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

当前阶段：`P3 - Project Template 最小实例化能力`

P3 的目标是在 P2 已完成的核心治理规则基础上，补齐通用 Harness Template 的最小项目实例化能力，使 `docs/project-template/` 可以被复制为真实项目中的 `docs/project/`，并为智能体提供项目架构、语义字典、仓库信息和任务 workflow 的标准入口。

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

## 4. P2 状态

P2：`核心治理规则实质化`

状态：`completed`

已完成：

1. [[IndexMaintenancePolicy]] 已能指导新增、移动、归档、删除文档时应更新哪些 index。
2. [[ContextLoadingPolicy]] 已能指导智能体按任务类型加载最小必要上下文。
3. [[ArtifactLifecycle]] 已定义文档、Skill、Memory、RAG、Workflow、Report 的状态迁移。
4. [[ScheduledGovernance]] 已定义 dry-run、报告优先、人工审批和允许自动修复的边界。
5. [[SkillPolicy]] 已定义 Skill 的使用、创建、更新、合并、归档和污染控制。
6. [[MemoryPolicy]] 已定义 Memory 的读取、写入、候选生成、晋升、归档和污染控制。

## 5. P3 目标

P3 聚焦 Project Template 最小实例化能力，不填入任何具体项目事实。

P3 要完成以下模板文档：

1. `docs/project-template/README.md`
2. `docs/project-template/architecture/ARCHITECTURE.md`
3. `docs/project-template/dictionary/SemanticDictionary.md`
4. `docs/project-template/git/Repository.md`
5. `docs/project-template/workflow/WorkflowTemplate.md`

## 6. P3 验收标准

P3 完成标准：

1. [[ProjectIndex]] 已从 planned 列表升级为可导航的项目模板索引。
2. `docs/project-template/README.md` 能说明如何从通用模板实例化到 `docs/project/`。
3. `docs/project-template/architecture/ARCHITECTURE.md` 能作为项目架构事实源模板。
4. `docs/project-template/dictionary/SemanticDictionary.md` 能作为术语、命名、字段和概念归一模板。
5. `docs/project-template/git/Repository.md` 能记录仓库、分支、构建、测试和提交边界模板。
6. `docs/project-template/workflow/WorkflowTemplate.md` 能记录真实项目任务过程、验收和 promotion candidates。
7. 新增文档全部包含 frontmatter。
8. 新增文档全部被 [[ProjectIndex]] 链接。
9. 文档内容不包含任何具体项目事实。
10. 本阶段不修改 `main`，通过 P3 分支和 PR 交付。

## 7. P4 建议任务

P4：`Project Template 扩展分区占位与 RAG 最小治理`

建议后续根据需要补齐：

1. `docs/project-template/prd/README.md`
2. `docs/project-template/api/README.md`
3. `docs/project-template/data/README.md`
4. `docs/project-template/test/README.md`
5. `docs/project-template/decision/ADR-0001-template.md`
6. `docs/rag/KnowledgeBasePolicy.md` 正文实质化

P4 的目标是扩展 Project Template 的项目管理覆盖面，同时开始建立 RAG 知识库准入规则。

## 8. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 不要在未建立治理报告前自动修改长期资产。
5. 重大架构变化应走分支和 PR。
6. 当前阶段只落地通用项目模板，不填入具体项目事实。

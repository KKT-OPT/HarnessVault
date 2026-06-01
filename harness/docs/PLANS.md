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
version: v0.8.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
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
  - "[[ObservabilityIndex]]"
  - "[[VerificationIndex]]"
  - "[[Dashboard]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P7 - Skill / Memory 最小资产骨架`

P7 的目标是在 P6 已完成 runtime 边界、Observability 和 Verification 最小闭环的基础上，让 Skill / Memory 从 policy 层进入可管理资产层。

P7 只建立通用资产骨架、模板和分区说明，不写入用户知识、不写入具体项目内容、不创建真实 active Memory，也不创建真实业务 Skill。

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

## 5. P3 状态

P3：`Project Template 最小实例化能力`

状态：`completed`

已完成：

1. [[ProjectIndex]] 已从 planned 列表升级为可导航的项目模板索引。
2. `docs/project-template/README.md` 已说明如何从通用模板实例化到 `docs/project/`。
3. `docs/project-template/architecture/ARCHITECTURE.md` 已可作为项目架构事实源模板。
4. `docs/project-template/dictionary/SemanticDictionary.md` 已可作为术语、命名、字段和概念归一模板。
5. `docs/project-template/git/Repository.md` 已可记录仓库、分支、构建、测试和提交边界模板。
6. `docs/project-template/workflow/WorkflowTemplate.md` 已可记录真实项目任务过程、验收和 promotion candidates。
7. 新增文档全部包含 frontmatter。
8. 新增文档全部被 [[ProjectIndex]] 链接。
9. 文档内容不包含任何具体项目事实。

## 6. P4 状态

P4：`Project Template 扩展分区占位与 RAG 最小治理`

状态：`completed`

已完成：

1. Project Template 的 `prd/api/data/test/decision` 分区已有最小占位文档。
2. [[ProjectIndex]] 已链接 P3 与 P4 的 project-template 文档。
3. [[KnowledgeBasePolicy]] 已说明 RAG 知识库的来源、准入、审查、更新和只读边界。
4. [[KnowledgePromotionPolicy]] 已说明 Workflow、Memory、Skill、RAG、Project Facts 之间的晋升路径和审批规则。
5. [[RAGIndex]] 已能导航 RAG 策略文档与 `standard/domain` 分区。
6. 新增文档全部包含 frontmatter。
7. 新增文档不包含任何真实项目事实或外部知识正文。

## 7. P5 状态

P5：`Harness 最小治理报告与检查清单`

状态：`completed`

已完成：

1. [[SecurityGovernance]] 已定义上下文安全、插件代码边界、外部工具输出和敏感信息检查规则。
2. [[DocumentGovernance]] 已定义文档新增、更新、拆分、归档、删除和审查规则。
3. [[CleanupPolicy]] 已定义文档资产、Memory、Skill、RAG 和报告产物的清理、归档和删除规则。
4. `GovernanceReportTemplate.md` 已可作为人工治理报告模板。
5. `IndexCheckReportTemplate.md` 已可作为索引完整性检查报告模板。
6. [[ReportsIndex]] 已链接治理报告模板和索引检查报告模板。

## 8. P6 状态

P6：`Runtime Boundary 与 Observability / Verification 最小闭环`

状态：`completed`

已完成：

1. [[RuntimeBoundaryPolicy]] 已区分 OpenClaw、Hermes-agent、Claude Code、Codex 等 agent runtime 的执行职责与 HarnessVault 的文档控制职责。
2. [[ObservabilityIndex]] 已作为顶层架构层入口，被 [[INDEX]] 链接。
3. [[TraceSchema]] 已定义任务 trace、操作事件、证据、成本、失败和人工介入的最小记录结构。
4. [[FailureAttributionPolicy]] 已定义模型、工具、上下文、生命周期、权限、文档事实和用户输入等失败归因维度。
5. [[VerificationIndex]] 已作为顶层架构层入口，被 [[INDEX]] 链接。
6. [[ReadinessCheckPolicy]] 已定义 agent runtime 执行前的任务、权限、上下文、分支和验收准备检查。
7. [[RegressionPolicy]] 已定义回归验证、复测、失败修复和验收闭环。

## 9. P7 目标

P7 聚焦通用 Skill / Memory 资产骨架。

P7 要完成：

1. `docs/agent/skills/.skill-usage.json` 初始结构
2. `docs/agent/skills/_TEMPLATE/SKILL.md` 通用模板
3. `docs/agent/memory/active/README.md`
4. `docs/agent/memory/candidates/README.md`
5. `docs/agent/memory/archive/README.md`
6. `docs/reports/governance/ExampleDryRunGovernanceReport.md`
7. 更新 [[SkillIndex]] 与 [[MemoryIndex]]

## 10. P7 验收标准

P7 完成标准：

1. [[SkillIndex]] 能导航 Skill 模板、usage sidecar 和正式 Skill 存放规则。
2. `.skill-usage.json` 只包含结构字段和空数组，不记录真实使用数据。
3. `_TEMPLATE/SKILL.md` 是通用 Skill 模板，不包含具体项目流程。
4. [[MemoryIndex]] 能导航 active / candidates / archive 三个 Memory 分区。
5. Memory 分区 README 只定义规则和占位结构，不包含用户知识或项目知识。
6. `ExampleDryRunGovernanceReport.md` 是治理报告示例，不记录真实检查结果。
7. 本阶段不修改 `main`，通过 P7 分支和 PR 交付。

## 11. P8 建议任务

P8：`Harness 最小自检与索引完整性 dry-run`

建议后续优先落地：

1. 基于 [[IndexCheckReportTemplate]] 生成一次真实 index dry-run 报告；
2. 检查 Obsidian wikilink unresolved 情况；
3. 检查 frontmatter `documentName` 与实际路径一致性；
4. 检查 stale / reviewAfter 文档；
5. 输出不自动修复的治理报告。

P8 的目标是第一次对 HarnessVault 自身做 dry-run 治理审查，但仍不写入用户知识或具体项目事实。

## 12. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 治理报告是证据，不是事实源。
5. 重大架构变化应走分支和 PR。
6. Project Template 只保留通用占位，不填入具体项目事实。
7. Observability 和 Verification 只定义记录与验证规则，不实现 runtime、sandbox、工具调度或模型调用。
8. Skill / Memory 资产骨架只允许模板和空结构，禁止写入用户知识和具体项目内容。

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
version: v0.6.0
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

当前阶段：`P5 - Harness 最小治理报告与检查清单`

P5 的目标是在 P4 已完成 Project Template 扩展分区和 RAG 最小治理的基础上，补齐可执行的人工治理报告模板，并实质化安全治理、文档治理和清理规则，使 HarnessVault 具备可审查、可记录、可回滚的治理闭环。

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

## 7. P5 目标

P5 聚焦最小治理报告与检查清单，补齐安全、文档和清理规则。

P5 要完成：

1. `docs/reports/governance/GovernanceReportTemplate.md`
2. `docs/reports/index/IndexCheckReportTemplate.md`
3. `docs/governance/SecurityGovernance.md` 正文实质化
4. `docs/governance/DocumentGovernance.md` 正文实质化
5. `docs/governance/CleanupPolicy.md` 正文实质化
6. 更新 [[ReportsIndex]] 与对应 reports README

## 8. P5 验收标准

P5 完成标准：

1. [[SecurityGovernance]] 能定义上下文安全、插件代码边界、外部工具输出和敏感信息检查规则。
2. [[DocumentGovernance]] 能定义文档新增、更新、拆分、归档、删除和审查规则。
3. [[CleanupPolicy]] 能定义文档资产、Memory、Skill、RAG 和报告产物的清理、归档和删除规则。
4. `GovernanceReportTemplate.md` 能作为人工治理报告模板。
5. `IndexCheckReportTemplate.md` 能作为索引完整性检查报告模板。
6. [[ReportsIndex]] 能链接治理报告模板和索引检查报告模板。
7. 本阶段不修改 `main`，通过 P5 分支和 PR 交付。

## 9. P6 建议任务

P6：`Skill / Memory 最小资产骨架与治理报告实例`

建议后续优先落地：

1. `docs/agent/skills/.skill-usage.json` 初始结构确认
2. `docs/agent/skills/_TEMPLATE/SKILL.md` 正文增强
3. `docs/agent/memory/active/README.md`
4. `docs/agent/memory/candidates/README.md`
5. `docs/agent/memory/archive/README.md`
6. 生成第一份 dry-run governance report 示例

P6 的目标是让 Skill / Memory 目录从 policy 层进入可管理资产层。

## 10. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 治理报告是证据，不是事实源。
5. 重大架构变化应走分支和 PR。
6. Project Template 只保留通用占位，不填入具体项目事实。
7. RAG 最小治理只定义准入和晋升规则，不直接导入外部知识正文。

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
version: v0.11.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: plan
purpose: 记录 HarnessVault 当前阶段目标、验收标准、剩余落地路线和验证路线。
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
  - "[[KnowledgeIntakePolicy]]"
  - "[[ReportArchivePolicy]]"
  - "[[HarnessValidationPlan]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P10 - Harness 完成路线图、阶段报告归档与架构验证`

P10 的目标是在 P9 已完成 dry-run 自检脚本和报告/RAG 分区补齐的基础上，明确通用 Harness 架构离完成还剩哪些工作、阶段性治理报告如何关闭和归档，以及架构完成后如何通过智能体模拟任务验证整套 Harness 是否可用。

P10 仍不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不执行自动修复。

## 2. P0-P9 状态

P0：`HarnessVault 基础仓库结构治理`，状态：`completed`。

P1：`HarnessVault 计划与索引治理收口`，状态：`completed`。

P2：`核心治理规则实质化`，状态：`completed`。

P3：`Project Template 最小实例化能力`，状态：`completed`。

P4：`Project Template 扩展分区占位与 RAG 最小治理`，状态：`completed`。

P5：`Harness 最小治理报告与检查清单`，状态：`completed`。

P6：`Runtime Boundary 与 Observability / Verification 最小闭环`，状态：`completed`。

P7：`Skill / Memory 最小资产骨架`，状态：`completed`。

P8：`Harness 自检与知识引入框架`，状态：`completed`。

P9：`Harness 自检工具与报告目录补齐`，状态：`completed`。

## 3. P9 验收结论

P9 已满足验收标准：

1. `check_harness_docs.py` 是 dry-run 自检脚本，只读取文件并打印 findings，不修改、移动、删除或创建 Harness 文档。
2. 自检脚本能检查 Markdown frontmatter、`documentName` 路径一致性和 wikilink 候选解析。
3. reports memory / skills / rag / security 分区已有 README。
4. RAG standard / domain 分区已有 README。
5. `FrontmatterPathDryRunReport.md` 已记录 frontmatter path consistency dry-run 的检查范围、限制和发现问题。
6. [[RAGIndex]] 已链接 standard / domain / intake 分区。
7. [[ReportsIndex]] 已链接 memory / skills / rag / security 分区。
8. P9 未写入真实用户知识，未写入具体项目事实。

## 4. P10 目标

P10 要完成：

1. `docs/governance/ReportArchivePolicy.md`
2. `docs/reports/archive/README.md`
3. `docs/verification/HarnessValidationPlan.md`
4. `docs/verification/HarnessInteractionSimulation.md`
5. 更新 [[GovernanceIndex]]、[[ReportsIndex]]、[[VerificationIndex]]
6. 在本文件中列出通用 Harness 架构落地剩余步骤和完成标准

## 5. P10 验收标准

P10 完成标准：

1. [[ReportArchivePolicy]] 能说明阶段性治理报告何时关闭、何时归档、何时不应作为默认上下文。
2. `docs/reports/archive/README.md` 已定义报告归档区规则。
3. [[HarnessValidationPlan]] 能定义通用 Harness 架构完成后的验证方法。
4. [[HarnessInteractionSimulation]] 能模拟智能体从用户 prompt 出发，通过 `AGENTS.md`、[[INDEX]]、[[PLANS]]、RAG、Project Template、Verification、Observability、Reports 完成一次任务闭环。
5. [[PLANS]] 已列出通用 Harness 架构落地剩余步骤。
6. 本阶段不写入真实用户知识、不写入具体项目事实。
7. 本阶段不修改 `main`，通过 P10 分支和 PR 交付。

## 6. 通用 Harness 架构剩余落地步骤

除了需要用户提供真实知识、具体项目事实、具体编程规范和具体业务上下文的部分外，通用 Harness 架构还剩以下步骤：

### P11 - 执行真实 dry-run 自检并修复低风险机械问题

目标：从设计型 dry-run 进入真实脚本检查。

需要完成：

1. 在本地或 CI 中运行 `python harness/scripts/check_harness_docs.py --root harness --format text`；
2. 保存真实输出到 `docs/reports/index/`；
3. 根据输出区分 false positive、低风险修复项和需要人工审查项；
4. 只修复已批准的低风险机械问题，例如明显 `documentName` 路径错误、缺失基础 frontmatter 字段、已确认的 alias 冲突；
5. 不自动删除、不自动归档、不自动修改语义内容。

### P12 - 阶段性治理报告归档收口

目标：处理 P8/P9 形成的阶段性报告资产。

需要完成：

1. 审查 `HarnessArchitectureAssessment.md`、`HarnessIndexDryRunReport.md`、`FrontmatterPathDryRunReport.md`；
2. 将已经被 policy / index / PLANS 吸收的结论标记为 closed；
3. 按 [[ReportArchivePolicy]] 归档阶段性报告；
4. 确保归档报告不进入默认上下文；
5. 保留历史追溯，不直接删除。

### P13 - Obsidian 与 Git 跟踪边界收口

目标：清理或确认 Obsidian UI 状态文件、workspace 状态和插件边界。

需要完成：

1. 评估 `.obsidian/graph.json` 是否应继续由 Git 跟踪；
2. 确认 `.obsidian/workspace.json` 不作为事实源；
3. 确认插件运行代码不进入默认上下文；
4. 梳理 README alias 和 Obsidian wikilink 歧义；
5. 必要时更新 `.gitignore` 和 Obsidian 说明文档。

### P14 - 通用 Harness 完成态验证

目标：验证 HarnessVault 能被任意智能体作为通用文档控制层使用。

需要完成：

1. 使用 [[HarnessValidationPlan]] 定义验证范围；
2. 使用 [[HarnessInteractionSimulation]] 模拟一次智能体任务；
3. 验证智能体是否能从 `AGENTS.md` 和 [[INDEX]] 找到正确文档；
4. 验证智能体是否能区分 RAG、Project Facts、Memory、Skill、Workflow、Report；
5. 验证智能体是否能执行 readiness、trace、verification、regression、promotion candidate 的闭环；
6. 输出验证报告。

### P15 - 通用模板冻结与 v1.0.0 发布候选

目标：将 HarnessVault 从持续搭建阶段转为可复制使用阶段。

需要完成：

1. 将核心入口、索引、治理策略、project-template、RAG intake、observability、verification、reports、scripts 标记为 release candidate；
2. 更新版本号策略；
3. 明确哪些文档可 active，哪些保持 draft，哪些归档；
4. 输出 `HarnessVault v1.0.0 Release Checklist`；
5. 用户验收后标记 v1.0.0。

## 7. 需要用户后续输入的内容

以下内容不应由通用 HarnessVault 预置，需要用户在具体项目或知识库建设阶段输入：

1. 具体项目需求、架构、仓库、分支、接口、数据、测试和 ADR；
2. 具体项目编程规范、代码风格、审查规则和测试规则；
3. 真实领域知识、标准资料、论文、网页资料、NotebookLM 输出；
4. 用户长期偏好、组织内部约束和项目长期决策；
5. 可复用但需要真实任务验证的 Skill；
6. 真实 dry-run、真实验证、真实失败归因和真实回归报告。

这些内容应通过 [[KnowledgeIntakePolicy]]、[[ProjectIndex]]、[[MemoryPolicy]]、[[SkillPolicy]] 和 [[KnowledgePromotionPolicy]] 引入，而不是直接写入通用模板。

## 8. 完成态判断

通用 Harness 架构可视为基本完成，当满足：

1. 入口完整：`AGENTS.md`、[[INDEX]]、[[PLANS]] 可引导智能体；
2. 分层完整：Governance、Agent、RAG、Project Template、Reports、Observability、Verification、Scripts 均有入口；
3. 生命周期完整：draft、active、review、stale、deprecated、archived 有规则；
4. 知识引入完整：intake、candidate、review、promotion、target asset 有规则；
5. 验证完整：readiness、trace、failure attribution、regression、acceptance 有规则；
6. 报告完整：治理、索引、Memory、Skill、RAG、安全、归档报告有规则；
7. 自检可运行：至少有 dry-run 脚本和报告模板；
8. 模拟可通过：智能体能按 [[HarnessInteractionSimulation]] 完成任务闭环；
9. 不污染：通用仓库不包含真实用户知识和具体项目事实。

## 9. 风险与注意事项

1. 治理报告是证据，不是长期事实源。
2. 阶段性报告应关闭和归档，不应长期进入默认上下文。
3. 自检脚本只允许 dry-run，不允许自动修改文档。
4. Project Template 只保留通用占位，不填入具体项目事实。
5. Knowledge intake 只能保存候选和模板，不得把未审查内容写入 RAG 或 Project Facts。
6. HarnessVault 不实现 agent runtime、sandbox、tool routing、model call 或实际任务执行。

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
version: v0.10.0
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
  - "[[KnowledgeIntakePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P9 - Harness 自检工具与报告目录补齐`

P9 的目标是在 P8 已完成自检报告和知识引入框架的基础上，补齐 report 分区 README、RAG standard/domain 分区 README，并建立最小 dry-run 自检脚本与 frontmatter path consistency 报告能力。

P9 仍然遵循 report-first 和 no silent mutation 原则：脚本只做检查和报告，不自动修改文档，不写入用户知识，不写入具体项目内容。

## 2. P0-P8 状态

P0：`HarnessVault 基础仓库结构治理`，状态：`completed`。

P1：`HarnessVault 计划与索引治理收口`，状态：`completed`。

P2：`核心治理规则实质化`，状态：`completed`。

P3：`Project Template 最小实例化能力`，状态：`completed`。

P4：`Project Template 扩展分区占位与 RAG 最小治理`，状态：`completed`。

P5：`Harness 最小治理报告与检查清单`，状态：`completed`。

P6：`Runtime Boundary 与 Observability / Verification 最小闭环`，状态：`completed`。

P7：`Skill / Memory 最小资产骨架`，状态：`completed`。

P8：`Harness 自检与知识引入框架`，状态：`completed`。

## 3. P8 验收结论

P8 已满足验收标准：

1. [[KnowledgeIntakePolicy]] 已区分用户知识、项目事实、RAG、Memory、Skill、Workflow、Report 的进入路径。
2. `docs/rag/intake/README.md` 已定义知识暂存区规则，并明确 intake 不是事实源。
3. `KnowledgeIntakeTemplate.md` 已作为用户提交知识、外部资料或领域知识的通用模板。
4. `HarnessArchitectureAssessment.md` 已评估当前 HarnessVault 组织结构是否合理，并提出后续改进方向。
5. `HarnessIndexDryRunReport.md` 已记录一次不自动修复的 index dry-run 检查结果和限制。
6. [[RAGIndex]] 已链接 Knowledge Intake 相关文档。
7. P8 未写入真实用户知识，未写入具体项目事实。

## 4. P9 目标

P9 要完成：

1. `scripts/check_harness_docs.py`
2. `scripts/README.md`
3. `docs/reports/memory/README.md`
4. `docs/reports/skills/README.md`
5. `docs/reports/rag/README.md`
6. `docs/reports/security/README.md`
7. `docs/rag/standard/README.md`
8. `docs/rag/domain/README.md`
9. `docs/reports/index/FrontmatterPathDryRunReport.md`
10. 更新 [[RAGIndex]] 与 [[ReportsIndex]]

## 5. P9 验收标准

P9 完成标准：

1. 自检脚本只做 dry-run，不自动修改文档。
2. 自检脚本能检查 Markdown frontmatter、`documentName` 路径一致性和 wikilink 候选解析。
3. reports memory / skills / rag / security 分区已有 README。
4. RAG standard / domain 分区已有 README。
5. `FrontmatterPathDryRunReport.md` 记录 frontmatter path consistency dry-run 的检查范围、限制和发现问题。
6. [[RAGIndex]] 已链接 standard/domain/intake 分区。
7. [[ReportsIndex]] 已链接 memory / skills / rag / security 分区。
8. 本阶段不写入真实用户知识、不写入具体项目事实。
9. 本阶段不修改 `main`，通过 P9 分支和 PR 交付。

## 6. P10 建议任务

P10：`Harness 文档资产归档策略与历史报告收口`

建议后续优先落地：

1. 明确 `HarnessArchitectureAssessment.md`、`HarnessIndexDryRunReport.md` 等阶段性报告何时关闭、何时归档；
2. 新增或补强 reports archive 规则；
3. 执行一次真实脚本输出的 dry-run 报告；
4. 评估 `.obsidian/graph.json` 等 UI 状态文件是否应从 Git 跟踪中移除；
5. 梳理所有 `README` alias 是否存在 Obsidian 解析歧义。

## 7. 临时治理资产说明

`HarnessArchitectureAssessment.md` 和 `HarnessIndexDryRunReport.md` 是治理报告资产，不是 Harness 长期事实源。它们不应被默认上下文长期引用。后续当其结论被正式 policy 或 index 吸收后，应按照 [[CleanupPolicy]] 和报告归档规则转为 `archived`，而不是直接删除。

## 8. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 治理报告是证据，不是事实源。
5. 重大架构变化应走分支和 PR。
6. Project Template 只保留通用占位，不填入具体项目事实。
7. Knowledge intake 只能保存候选和模板，不得把未审查内容写入 RAG 或 Project Facts。
8. 自检脚本只允许 dry-run，不允许自动修改文档。

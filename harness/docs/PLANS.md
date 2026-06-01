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
version: v0.9.0
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

当前阶段：`P8 - Harness 自检与知识引入框架`

P8 的目标是在 P7 已完成 Skill / Memory 最小资产骨架的基础上，对 HarnessVault 当前组织结构进行一次 dry-run 自检，并补齐用户知识、外部资料、领域知识进入 Harness 的通用引入框架。

P8 仍处于通用 Harness 架构落地阶段，不写入真实用户知识、不写入具体项目内容、不导入外部知识正文。P8 只定义知识如何被提交、暂存、审查、路由、索引和晋升。

## 2. P0-P7 状态

P0：`HarnessVault 基础仓库结构治理`，状态：`completed`。

P1：`HarnessVault 计划与索引治理收口`，状态：`completed`。

P2：`核心治理规则实质化`，状态：`completed`。

P3：`Project Template 最小实例化能力`，状态：`completed`。

P4：`Project Template 扩展分区占位与 RAG 最小治理`，状态：`completed`。

P5：`Harness 最小治理报告与检查清单`，状态：`completed`。

P6：`Runtime Boundary 与 Observability / Verification 最小闭环`，状态：`completed`。

P7：`Skill / Memory 最小资产骨架`，状态：`completed`。

## 3. P8 目标

P8 聚焦三个问题：

1. 判断当前 HarnessVault 组织结构是否合理；
2. 建立用户知识、外部资料、领域知识进入 Harness 的通用 intake 机制；
3. 生成一次不自动修复的 self-check / index dry-run 报告。

P8 要完成：

1. `docs/rag/KnowledgeIntakePolicy.md`
2. `docs/rag/intake/README.md`
3. `docs/rag/intake/KnowledgeIntakeTemplate.md`
4. `docs/reports/governance/HarnessArchitectureAssessment.md`
5. `docs/reports/index/HarnessIndexDryRunReport.md`
6. 更新 [[RAGIndex]]
7. 更新 reports 相关 README

## 4. P8 验收标准

P8 完成标准：

1. [[KnowledgeIntakePolicy]] 能区分用户知识、项目事实、RAG、Memory、Skill、Workflow、Report 的进入路径。
2. `docs/rag/intake/README.md` 能定义知识暂存区规则，并明确 intake 不是事实源。
3. `KnowledgeIntakeTemplate.md` 能作为用户提交知识、外部资料或领域知识的通用模板。
4. `HarnessArchitectureAssessment.md` 能评估当前 HarnessVault 组织结构是否合理，并提出后续改进方向。
5. `HarnessIndexDryRunReport.md` 能记录一次不自动修复的 index dry-run 检查结果和限制。
6. [[RAGIndex]] 已链接 Knowledge Intake 相关文档。
7. 本阶段不写入真实用户知识、不写入具体项目事实。
8. 本阶段不修改 `main`，通过 P8 分支和 PR 交付。

## 5. P9 建议任务

P9：`Harness 自检自动化脚本与报告目录补齐`

建议后续优先落地：

1. `scripts/check-index-links` 或等价脚本设计；
2. `docs/reports/memory/README.md`；
3. `docs/reports/skills/README.md`；
4. `docs/reports/rag/README.md`；
5. `docs/reports/security/README.md`；
6. RAG `standard/` 与 `domain/` 分区 README；
7. 一次真实的 frontmatter path consistency dry-run。

P9 的目标是从人工 dry-run 过渡到可执行但仍 report-first 的最小自检工具链。

## 6. 风险与注意事项

1. 不要把 Dataview 输出当作正式索引。
2. 不要让 Obsidian workspace、插件代码和 IDE 本地状态进入智能体默认上下文。
3. 不要把一次性任务记录直接写入 Memory 或 Skill。
4. 治理报告是证据，不是事实源。
5. 重大架构变化应走分支和 PR。
6. Project Template 只保留通用占位，不填入具体项目事实。
7. Observability 和 Verification 只定义记录与验证规则，不实现 runtime、sandbox、工具调度或模型调用。
8. Skill / Memory 资产骨架只允许模板和空结构，禁止写入用户知识和具体项目内容。
9. Knowledge intake 只能保存候选和模板，不得把未审查内容写入 RAG 或 Project Facts。

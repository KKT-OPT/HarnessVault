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
version: v0.18.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
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
  - "[[TemplatesIndex]]"
  - "[[DocumentAudiencePolicy]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[ComplexTaskPromptTemplate]]"
  - "[[HarnessValidationPlan]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P15b - 机器友好入口与 Agent Context Manifest`

P15a 已完成：[[HarnessEngineering]] 已升级到 v1.2.0，并完成与当前 HarnessVault 架构的同步收口。

P15b 的目标是在不替代 Markdown 的前提下，补充 `docs/agent/AgentContextManifest.yaml` 作为轻量 machine-readable 辅助入口，使智能体可以快速读取稳定导航信息、默认排除路径和架构层映射。

P15b 不执行 P15 完成态验证，不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不创建项目级 RAG 内容。

## 2. P0-P15-pre 状态

P0-P14 均已完成。P15-pre 已完成设计一致性审查、文档受众分类、知识库构建路径和复杂任务 Prompt 模板补齐。

## 3. P15-pre 验收结论

P15-pre 已满足验收标准：

1. [[HarnessDesignAlignmentReport]] 已列出已落地但设计文档需更新的内容、设计文档有价值但尚未落地的内容、建议暂不落地的内容。
2. [[DocumentAudiencePolicy]] 已区分 agent-readable、human-readable、hybrid、machine-checkable、prompt-structured 文档。
3. [[KnowledgeBaseConstructionWorkflow]] 已定义 raw material、semantic enrichment、effective knowledge、review/promotion 流程。
4. [[RawKnowledgeMaterialTemplate]] 与 [[EffectiveKnowledgeTemplate]] 已作为知识库构建模板。
5. [[ComplexTaskPromptTemplate]] 已作为复杂任务 Prompt 模板。
6. P15-pre 未写入真实用户知识，未写入具体项目事实。

## 4. P15a 目标（已完成）

P15a 要完成：

1. 将 [[HarnessEngineering]] 从 v1.1.0 升级到 v1.2.0。
2. 从 [[HarnessEngineering]] 中移除旧的 `docs/agent/workflow-template/` 或重复 workflow template 架构描述。
3. 在 [[HarnessEngineering]] 中明确 `templates/**` 是唯一模板源。
4. 在 [[HarnessEngineering]] 中明确 Knowledge Base Construction Workflow。
5. 在 [[HarnessEngineering]] 中明确 Document Audience and Format Strategy。
6. 在 [[HarnessEngineering]] 中明确 Reports Archive、Obsidian/Git Boundary、Verification/Simulation、Scripts/self-check、Complex Task Prompt Template。
7. 在本文件中列出后续第二优先级到第五优先级的工作项和验收标准。

## 5. P15a 验收标准（已完成）

P15a 完成标准：

1. P15a 完成时 [[HarnessEngineering]] frontmatter version 为 `v1.2.0`；后续 P15b 可按 manifest 接入进行小版本更新。
2. [[HarnessEngineering]] 推荐目录结构与当前 main 架构一致，包含 `templates/**` 和 `scripts/**`。
3. [[HarnessEngineering]] 不再把 `docs/agent/workflow-template/` 作为推荐模板路径。
4. [[HarnessEngineering]] 明确 `templates/**` 是唯一模板源。
5. [[HarnessEngineering]] 明确 raw material → semantic enrichment → effective knowledge → review / promotion 的知识库构建路径。
6. [[HarnessEngineering]] 明确 agent-readable、human-readable、hybrid、machine-checkable、prompt-structured 文档受众分类。
7. [[HarnessEngineering]] 明确 archived reports 不进入默认上下文。
8. [[HarnessEngineering]] 明确 Obsidian workspace、graph 和 plugin runtime code 不是事实源。
9. [[HarnessEngineering]] 明确 P15 才执行完成态验证。
10. P15a 不写入真实用户知识，不写入具体项目事实。

## 6. 后续第二优先级到第五优先级

### P15b - 机器友好入口与 Agent Context Manifest

优先级：第二优先级。

目标：在不替代 Markdown 的前提下，补充一个轻量 machine-readable 入口，使智能体可以快速读取稳定导航信息、默认排除路径和架构层映射。

建议新增：

```text
harness/docs/agent/AgentContextManifest.yaml
```

工作项：

1. 定义 machine-readable entry order；
2. 定义 default_include 和 default_exclude；
3. 定义 layers 到 index 文档的映射；
4. 定义 artifact boundary，例如 archived reports、Obsidian workspace、plugin runtime code 默认排除；
5. 更新 [[AgentIndex]]、[[DocumentAudiencePolicy]]、[[INDEX]] 或 [[PLANS]] 的关联入口；
6. 确认该 manifest 是辅助导航，不替代 Markdown 事实源。

验收标准：

1. `AgentContextManifest.yaml` 只包含稳定导航和上下文加载规则，不包含真实项目事实或用户知识。
2. Manifest 能表达 `AGENTS.md → INDEX → PLANS → layer index` 的入口顺序。
3. Manifest 明确排除 `docs/reports/archive/**`、`.obsidian/workspace*.json`、`.obsidian/graph.json`、插件 runtime code。
4. Manifest 的层级映射与 [[INDEX]] 保持一致。
5. [[DocumentAudiencePolicy]] 说明该 manifest 属于 machine-checkable 辅助入口。
6. 不要求智能体只读取 manifest；Markdown 仍是正式事实源。

### P15c - RAG Intake Raw / Enriched 空分区落地

优先级：第三优先级。

目标：根据 [[KnowledgeBaseConstructionWorkflow]] 补齐 `docs/rag/intake/raw/` 与 `docs/rag/intake/enriched/` 的空分区 README，使后续用户可以快速建立知识库，但不写入真实知识正文。

建议新增：

```text
docs/rag/intake/raw/README.md
docs/rag/intake/enriched/README.md
```

工作项：

1. 定义 raw material 分区规则；
2. 定义 semantic enrichment 分区规则；
3. 明确 raw / enriched 不是事实源，不进入默认上下文；
4. 指向 [[RawKnowledgeMaterialTemplate]] 与 [[EffectiveKnowledgeTemplate]]；
5. 更新 [[RAGIndex]] 和 [[KnowledgeIntake]]；
6. 保持通用性，不写入真实资料。

验收标准：

1. raw / enriched README 均有 frontmatter、唯一 alias、reviewAfter。
2. raw README 明确只保存原始资料元信息、摘要、来源，不保存大段原文。
3. enriched README 明确由人类或智能体补充语义、关键词、适用范围、可信度判断。
4. 两个分区均明确不是事实源，未经审查不得进入 active RAG。
5. [[RAGIndex]] 能导航到 raw / enriched 分区。
6. 不写入真实知识正文。

### P15d - Prompt Template 接入 AGENTS.md 与任务入口规则

优先级：第四优先级。

目标：将 [[ComplexTaskPromptTemplate]] 接入 `AGENTS.md` 和 [[PromptPolicy]] 的任务入口规则，使复杂任务能够稳定使用结构化 prompt。

工作项：

1. 更新 `AGENTS.md`，说明复杂任务优先使用 `templates/ComplexTaskPromptTemplate.md`；
2. 更新 [[PromptPolicy]]，补充复杂任务 prompt 的使用场景；
3. 更新 [[TemplatesIndex]]，确认 prompt 模板属于唯一模板源；
4. 明确 XML-like block 是 prompt 结构约定，不是强制 schema；
5. 确保 prompt 模板要求智能体优先读取 `AGENTS.md`、[[INDEX]]、[[PLANS]]。

验收标准：

1. `AGENTS.md` 能引导智能体在复杂任务中使用 [[ComplexTaskPromptTemplate]]。
2. [[PromptPolicy]] 明确复杂任务 prompt 的必备字段。
3. [[ComplexTaskPromptTemplate]] 包含 entry contract、final goal、previous context、feedback、task、inspection scope、constraints、acceptance criteria、output format、governance notes。
4. Prompt 模板不包含真实项目事实或用户知识。
5. prompt 模板仍位于 `templates/**`。

### P15e - Harness Validation Cases 准备

优先级：第五优先级。

目标：在正式 P15 完成态验证前，补齐可执行的验证用例清单，使 P15 不只是抽象模拟，而是能按用例检查 Harness 架构是否可用。

建议新增：

```text
docs/verification/HarnessValidationCases.md
```

建议验证用例：

1. 复杂任务 prompt 读取路径验证；
2. 原始资料进入知识库候选路径验证；
3. Project Template 实例化路径验证；
4. archived reports 默认排除验证；
5. Obsidian workspace / plugin runtime 默认排除验证；
6. dry-run self-check 脚本入口验证。

验收标准：

1. `HarnessValidationCases` 至少包含上述 6 类验证用例。
2. 每个用例包含输入、读取路径、预期行为、禁止行为、通过标准。
3. 用例只使用占位输入，不写入真实用户知识或具体项目事实。
4. [[VerificationIndex]] 能导航到验证用例清单。
5. P15 可以直接基于这些用例生成 Harness 完成态验证报告。

## 7. P15 - 通用 Harness 完成态验证

P15 在 P15b-P15e 完成后执行。

目标：验证 HarnessVault 能被任意智能体作为通用文档控制层使用。

需要完成：

1. 使用 [[HarnessValidationPlan]] 定义验证范围；
2. 使用 [[HarnessInteractionSimulation]] 和 `HarnessValidationCases` 模拟任务；
3. 验证智能体是否能从 `AGENTS.md` 和 [[INDEX]] 找到正确文档；
4. 验证智能体是否能区分 RAG、Project Facts、Memory、Skill、Workflow、Report；
5. 验证智能体是否能执行 readiness、trace、verification、regression、promotion candidate 的闭环；
6. 输出验证报告。

## 8. P16 - 通用模板冻结与 v1.0.0 发布候选

目标：将 HarnessVault 从持续搭建阶段转为可复制使用阶段。

需要完成：

1. 将核心入口、索引、治理策略、project-template、RAG intake、observability、verification、reports、scripts、templates 标记为 release candidate；
2. 更新版本号策略；
3. 明确哪些文档可 active，哪些保持 draft，哪些归档；
4. 输出 `HarnessVault v1.0.0 Release Checklist`；
5. 用户验收后标记 v1.0.0。

## 9. 需要用户后续输入的内容

以下内容不应由通用 HarnessVault 预置，需要用户在具体项目或知识库建设阶段输入：

1. 具体项目需求、架构、仓库、分支、接口、数据、测试和 ADR；
2. 具体项目编程规范、代码风格、审查规则和测试规则；
3. 真实原始资料、标准资料、论文、网页资料、NotebookLM 输出；
4. 用户对原始资料的语义增强、关键词、术语解释和适用范围判断；
5. 用户长期偏好、组织内部约束和项目长期决策；
6. 可复用但需要真实任务验证的 Skill；
7. 真实 dry-run、真实验证、真实失败归因和真实回归报告。

这些内容应通过 [[KnowledgeIntakePolicy]]、[[KnowledgeBaseConstructionWorkflow]]、[[ProjectIndex]]、[[MemoryPolicy]]、[[SkillPolicy]] 和 [[KnowledgePromotionPolicy]] 引入，而不是直接写入通用模板。

## 10. 完成态判断

通用 Harness 架构可视为基本完成，当满足：

1. 入口完整：`AGENTS.md`、[[INDEX]]、[[PLANS]] 可引导智能体；
2. 模板统一：所有可复制模板集中在 `templates/**`；
3. 分层完整：Governance、Agent、RAG、Project Template、Reports、Observability、Verification、Scripts、Templates 均有入口；
4. 生命周期完整：draft、active、review、stale、deprecated、archived 有规则；
5. 知识引入完整：raw、intake、candidate、review、promotion、target asset 有规则；
6. 验证完整：readiness、trace、failure attribution、regression、acceptance 有规则；
7. 报告完整：治理、索引、Memory、Skill、RAG、安全、归档报告有规则；
8. 自检可运行：至少有 dry-run 脚本和报告模板；
9. 模拟可通过：智能体能按 [[HarnessInteractionSimulation]] 和 `HarnessValidationCases` 完成任务闭环；
10. 不污染：通用仓库不包含真实用户知识和具体项目事实。

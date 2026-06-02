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
version: v0.16.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-06-02 00:00:00.000 +08:00
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
  - "[[HarnessDesignAlignmentReport]]"
  - "[[DocumentAudiencePolicy]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[ComplexTaskPromptTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P15-pre - 设计文档同步、文档受众分类、知识库构建路径与 Prompt 模板收口`

P15-pre 是进入 P15 通用 Harness 完成态验证之前的前置收口阶段。目标不是执行验证，而是先确认设计文档与当前仓库实现一致，明确哪些文档面向智能体读取、哪些面向人类阅读和补充，补齐通用知识库构建路径，并增加复杂任务 Prompt 模板。

P15-pre 不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不创建项目级 RAG 内容。

## 2. P0-P14 状态

P0-P14 均已完成；其中 P14 已完成 Obsidian 与 Git 跟踪边界治理。

## 3. P14 验收结论

P14 已满足验收标准：

1. [[ObsidianGitBoundaryPolicy]] 已区分 facts、templates、reports、lightweight config、volatile UI state、plugin runtime code。
2. [[ObsidianSetup]] 与 `.gitignore` 策略一致，不再把 `graph.json` 描述为推荐提交的轻量配置。
3. `.gitignore` 已明确忽略 workspace、graph、插件运行代码和本地易变状态。
4. `harness/.obsidian/workspace.json` 与 `harness/.obsidian/graph.json` 不作为事实源，不进入默认上下文。
5. 插件运行代码不进入默认上下文；插件配置可以在人工确认后保留。
6. `templates/**` 继续作为唯一模板源，不受 Obsidian workspace 状态影响。
7. P14 安全报告记录边界检查结论，未保存真实 secrets、用户知识或具体项目事实。

## 4. P15-pre 目标

P15-pre 要完成：

1. 新增 [[HarnessDesignAlignmentReport]]，交叉验证 [[HarnessEngineering]] 与当前 main 架构实现。
2. 新增 [[DocumentAudiencePolicy]]，区分 agent-readable、human-readable、hybrid、machine-checkable 文档。
3. 新增 [[KnowledgeBaseConstructionWorkflow]]，定义原始资料层、语义增强层、有效知识层和晋升流程。
4. 新增知识库模板：`RawKnowledgeMaterialTemplate.md` 与 `EffectiveKnowledgeTemplate.md`。
5. 新增 [[ComplexTaskPromptTemplate]]，作为复杂任务提示词模板。
6. 更新 [[PromptPolicy]]、[[AgentIndex]]、[[RAGIndex]]、[[TemplatesIndex]] 和 [[GovernanceIndex]]。
7. 明确 P15 才进入完成态验证，P15-pre 只做验证前置收口。

## 5. P15-pre 验收标准

P15-pre 完成标准：

1. [[HarnessDesignAlignmentReport]] 列出：已落地但设计文档需更新的内容、设计文档有价值但尚未落地的内容、建议暂不落地的内容。
2. [[DocumentAudiencePolicy]] 能说明哪些文档应优先给智能体读取，哪些文档主要由人类阅读、补充和审批。
3. 文档受众策略不要求把所有 Markdown 改成 XML/JSON；只对 prompt、trace、report、knowledge card 等结构化输入采用更强结构。
4. [[KnowledgeBaseConstructionWorkflow]] 能定义 raw material、semantic enrichment、effective knowledge、review/promotion 的通用流程。
5. 知识库模板只提供通用结构，不包含真实知识正文。
6. [[ComplexTaskPromptTemplate]] 使用 XML 标签隔离 final goal、previous context、feedback、task、inspection scope、constraints、acceptance criteria 和 output format。
7. 更新后的索引能从 `AGENTS.md` → [[INDEX]] → 对应分区 index 找到新增文档和模板。
8. P15-pre 不写入真实用户知识，不写入具体项目事实。
9. P15-pre 不修改 `main`，通过分支和 PR 交付。

## 6. 后续剩余落地路线

### P15 - 通用 Harness 完成态验证

目标：验证 HarnessVault 能被任意智能体作为通用文档控制层使用。

需要完成：

1. 使用 [[HarnessValidationPlan]] 定义验证范围；
2. 使用 [[HarnessInteractionSimulation]] 模拟一次智能体任务；
3. 验证智能体是否能从 `AGENTS.md` 和 [[INDEX]] 找到正确文档；
4. 验证智能体是否能区分 RAG、Project Facts、Memory、Skill、Workflow、Report；
5. 验证智能体是否能执行 readiness、trace、verification、regression、promotion candidate 的闭环；
6. 输出验证报告。

### P16 - 通用模板冻结与 v1.0.0 发布候选

目标：将 HarnessVault 从持续搭建阶段转为可复制使用阶段。

需要完成：

1. 将核心入口、索引、治理策略、project-template、RAG intake、observability、verification、reports、scripts、templates 标记为 release candidate；
2. 更新版本号策略；
3. 明确哪些文档可 active，哪些保持 draft，哪些归档；
4. 输出 `HarnessVault v1.0.0 Release Checklist`；
5. 用户验收后标记 v1.0.0。

## 7. 需要用户后续输入的内容

以下内容不应由通用 HarnessVault 预置，需要用户在具体项目或知识库建设阶段输入：

1. 具体项目需求、架构、仓库、分支、接口、数据、测试和 ADR；
2. 具体项目编程规范、代码风格、审查规则和测试规则；
3. 真实原始资料、标准资料、论文、网页资料、NotebookLM 输出；
4. 用户对原始资料的语义增强、关键词、术语解释和适用范围判断；
5. 用户长期偏好、组织内部约束和项目长期决策；
6. 可复用但需要真实任务验证的 Skill；
7. 真实 dry-run、真实验证、真实失败归因和真实回归报告。

这些内容应通过 [[KnowledgeIntakePolicy]]、[[KnowledgeBaseConstructionWorkflow]]、[[ProjectIndex]]、[[MemoryPolicy]]、[[SkillPolicy]] 和 [[KnowledgePromotionPolicy]] 引入，而不是直接写入通用模板。

## 8. 完成态判断

通用 Harness 架构可视为基本完成，当满足：

1. 入口完整：`AGENTS.md`、[[INDEX]]、[[PLANS]] 可引导智能体；
2. 模板统一：所有可复制模板集中在 `templates/**`；
3. 分层完整：Governance、Agent、RAG、Project Template、Reports、Observability、Verification、Scripts、Templates 均有入口；
4. 生命周期完整：draft、active、review、stale、deprecated、archived 有规则；
5. 知识引入完整：raw、intake、candidate、review、promotion、target asset 有规则；
6. 验证完整：readiness、trace、failure attribution、regression、acceptance 有规则；
7. 报告完整：治理、索引、Memory、Skill、RAG、安全、归档报告有规则；
8. 自检可运行：至少有 dry-run 脚本和报告模板；
9. 模拟可通过：智能体能按 [[HarnessInteractionSimulation]] 完成任务闭环；
10. 不污染：通用仓库不包含真实用户知识和具体项目事实。

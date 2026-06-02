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
version: v0.15.0
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
  - "[[TemplatesIndex]]"
  - "[[ReportsArchive]]"
  - "[[ObsidianGitBoundaryPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P14 - Obsidian 与 Git 跟踪边界收口`

P14 的目标是在 P13 已完成阶段性报告归档收口的基础上，确认 Obsidian UI 状态文件、workspace 状态、插件运行代码、轻量配置文件和 Git 跟踪规则之间的边界，防止编辑器状态或插件代码污染 Harness 文档事实源与智能体默认上下文。

P14 不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不引入项目级 RAG 内容，只收口通用 Obsidian/Git 维护规则。

## 2. P0-P13 状态

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

P10：`Harness 完成路线图、阶段报告归档与架构验证`，状态：`completed`。

P11：`模板统一治理、链接歧义收口与真实 self-check 修复`，状态：`completed`。

P12：`真实 self-check 复测结果收口与 README 链接规则泛化`，状态：`completed`。

P13：`阶段性治理报告归档收口`，状态：`completed`。

## 3. P13 验收结论

P13 已满足验收标准：

1. `PLANS.md` 不再包含裸 README wikilink。
2. P8-P12 阶段性报告已经归档，默认 reports 索引不再推荐这些报告作为当前上下文。
3. 归档报告保留 `archivedFrom`、`archivedReason`、`status: archived` 等字段。
4. [[ReportsArchive]] 能导航已归档报告。
5. [[GovernanceReports]] 和 [[IndexReports]] 只保留模板、当前报告类型说明或后续可用入口，不再列出已归档阶段报告作为当前报告。
6. 阶段性报告的结论已被正式 policy、index、PLANS 或脚本吸收。
7. P13 未写入真实用户知识，未写入具体项目事实。

## 4. P14 目标

P14 要完成：

1. 新增 [[ObsidianGitBoundaryPolicy]]，定义 Obsidian 配置、UI 状态、插件代码、模板目录和 Git 跟踪边界。
2. 更新 [[ObsidianSetup]]，使其与 `.gitignore` 策略一致，明确 `graph.json`、`workspace.json`、插件运行代码不作为事实源。
3. 更新 `.gitignore` 注释，明确允许跟踪和禁止跟踪的 Obsidian 文件类型。
4. 更新 [[GovernanceIndex]]，将 [[ObsidianGitBoundaryPolicy]] 纳入治理入口。
5. 更新 [[SecurityReports]]，增加 Obsidian/Git boundary report 类型。
6. 新增 `docs/reports/security/ObsidianGitBoundaryReport.md`，记录本轮边界检查结论。
7. 保持通用 Harness 架构，不写入用户知识或具体项目事实。

## 5. P14 验收标准

P14 完成标准：

1. [[ObsidianGitBoundaryPolicy]] 能区分 facts、templates、reports、lightweight config、volatile UI state、plugin runtime code。
2. [[ObsidianSetup]] 与 `.gitignore` 策略一致，不再把 `graph.json` 描述为推荐提交的轻量配置。
3. `.gitignore` 明确忽略 workspace、graph、插件运行代码和本地易变状态。
4. `harness/.obsidian/workspace.json` 与 `harness/.obsidian/graph.json` 不作为事实源，不进入默认上下文。
5. 插件运行代码不进入默认上下文；插件配置可以在人工确认后保留。
6. `templates/**` 继续作为唯一模板源，不受 Obsidian workspace 状态影响。
7. P14 安全报告记录边界检查结论，但不保存真实 secrets、用户知识或具体项目事实。
8. P14 不修改 `main`，通过 P14 分支和 PR 交付。

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
3. 真实领域知识、标准资料、论文、网页资料、NotebookLM 输出；
4. 用户长期偏好、组织内部约束和项目长期决策；
5. 可复用但需要真实任务验证的 Skill；
6. 真实 dry-run、真实验证、真实失败归因和真实回归报告。

这些内容应通过 [[KnowledgeIntakePolicy]]、[[ProjectIndex]]、[[MemoryPolicy]]、[[SkillPolicy]] 和 [[KnowledgePromotionPolicy]] 引入，而不是直接写入通用模板。

## 8. 完成态判断

通用 Harness 架构可视为基本完成，当满足：

1. 入口完整：`AGENTS.md`、[[INDEX]]、[[PLANS]] 可引导智能体；
2. 模板统一：所有可复制模板集中在 `templates/**`；
3. 分层完整：Governance、Agent、RAG、Project Template、Reports、Observability、Verification、Scripts、Templates 均有入口；
4. 生命周期完整：draft、active、review、stale、deprecated、archived 有规则；
5. 知识引入完整：intake、candidate、review、promotion、target asset 有规则；
6. 验证完整：readiness、trace、failure attribution、regression、acceptance 有规则；
7. 报告完整：治理、索引、Memory、Skill、RAG、安全、归档报告有规则；
8. 自检可运行：至少有 dry-run 脚本和报告模板；
9. 模拟可通过：智能体能按 [[HarnessInteractionSimulation]] 完成任务闭环；
10. 不污染：通用仓库不包含真实用户知识和具体项目事实。

## 9. 风险与注意事项

1. 治理报告是证据，不是长期事实源。
2. Obsidian workspace、graph 和插件运行代码不是事实源。
3. 自检脚本只允许 dry-run，不允许自动修改文档。
4. Project Template 只保留通用占位，不填入具体项目事实。
5. `templates/**` 是唯一模板源，后续提示词模板也进入该目录。
6. Knowledge intake 只能保存候选和模板，不得把未审查内容写入 RAG 或 Project Facts。
7. HarnessVault 不实现 agent runtime、sandbox、tool routing、model call 或实际任务执行。

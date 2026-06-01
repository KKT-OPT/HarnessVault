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
version: v0.12.0
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

当前阶段：`P11 - 模板统一治理、链接歧义收口与真实 self-check 修复`

P11 的目标是在 P10 已完成完成路线图和架构验证方案的基础上，处理真实 `check_harness_docs.py` dry-run 输出中的低风险问题，并根据用户确认的原则统一模板源：所有可复制模板、Templater 模板、提示词模板和后续模板资产统一放入 `templates/**`，其他目录只保留模板说明、索引、分区规则或事实源，不再保存重复模板正文。

P11 不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不做自动删除；所有结构性删除或迁移通过分支和 PR 完成。

## 2. P0-P10 状态

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

## 3. P10 验收结论

P10 已满足验收标准：

1. [[ReportArchivePolicy]] 已说明阶段性治理报告何时关闭、何时归档、何时不应作为默认上下文。
2. `docs/reports/archive/README.md` 已定义报告归档区规则。
3. [[HarnessValidationPlan]] 已定义通用 Harness 架构完成后的验证方法。
4. [[HarnessInteractionSimulation]] 已模拟智能体从用户 prompt 出发，通过 `AGENTS.md`、[[INDEX]]、[[PLANS]]、RAG、Project Template、Verification、Observability、Reports 完成一次任务闭环。
5. [[PLANS]] 已列出通用 Harness 架构剩余落地步骤。
6. P10 未写入真实用户知识，未写入具体项目事实。

## 4. P11 输入问题

用户本地运行：

```bash
python harness/scripts/check_harness_docs.py --root harness --format text
```

得到：

```text
Markdown files checked: 76
Findings: 32
No files were modified.
```

问题集中在：

1. `harness/AGENTS.md` 和 `harness/README.md` 缺少 frontmatter；
2. `[[README]]` 裸链接导致大量 README 候选歧义；
3. `[[WorkflowTemplate]]` 同时命中 `docs/project-template/workflow/WorkflowTemplate.md` 和 `templates/WorkflowTemplate.md`；
4. `templates/**` 中的 Templater 生成目标路径被普通文档规则误判为 `documentName` mismatch；
5. `templates/SkillTemplate.md` 缺少基础 frontmatter 字段。

## 5. P11 设计原则

P11 采用以下原则：

1. `templates/**` 是唯一模板源；
2. `docs/project-template/**` 只保存项目模板说明、分区索引和实例化规则，不保存可复制模板正文；
3. 子目录 README 必须链接到对应层级 index；
4. 所有层级 index 必须链接到 [[INDEX]]；
5. `AGENTS.md` 必须作为智能体优先入口，任何形式的提示词或模板都应能指向 `AGENTS.md`；
6. 自检脚本对 `templates/**` 采用 template-aware 规则，区分模板源文件路径和生成目标路径；
7. P11 只修复低风险机械问题，不修改语义内容，不写入用户知识或具体项目事实。

## 6. P11 目标

P11 要完成：

1. 为 `harness/AGENTS.md` 和 `harness/README.md` 补齐 frontmatter；
2. 新增或更新 `templates/README.md`，定义统一模板源规则；
3. 将项目 workflow 可复制模板统一到 `templates/WorkflowTemplate.md`；
4. 用 `docs/project-template/workflow/README.md` 替代重复的 `docs/project-template/workflow/WorkflowTemplate.md`；
5. 修复 `[[README]]` 和 `[[WorkflowTemplate]]` 的主要链接歧义；
6. 更新 [[ProjectIndex]]，明确 project-template 分区文档与 `templates/**` 的关系；
7. 增强 `check_harness_docs.py` 的 template-aware 检查能力和 finding 去重；
8. 补齐 `templates/SkillTemplate.md` 必要 frontmatter；
9. 新增 `docs/reports/index/RealHarnessSelfCheckReport.md`，记录本轮真实 dry-run 输出分类和修复策略。

## 7. P11 验收标准

P11 完成标准：

1. `harness/AGENTS.md` 和 `harness/README.md` 已包含 frontmatter，并继续保持入口优先级。
2. [[ProjectIndex]] 不再使用裸 `[[README]]` 链接。
3. `[[WorkflowTemplate]]` 不再同时命中 project-template 和 `templates/**` 两个模板文件。
4. `templates/**` 被定义为唯一模板源，后续提示词模板也应进入 `templates/**`。
5. `docs/project-template/**` 不再保存重复模板正文，只保存模板说明、索引、分区规则和实例化规则。
6. `check_harness_docs.py` 仍然只做 dry-run，不自动修改文件。
7. `check_harness_docs.py` 能区分普通文档与 `templates/**` 源模板。
8. `templates/SkillTemplate.md` frontmatter 缺失已修复。
9. `RealHarnessSelfCheckReport.md` 已记录用户本地 dry-run 输出、问题分类、修复策略和剩余人工确认项。
10. 本阶段不写入真实用户知识，不写入具体项目事实。
11. 本阶段不修改 `main`，通过 P11 分支和 PR 交付。

## 8. 后续剩余落地路线

### P12 - 执行 P11 后真实脚本复测与剩余 finding 收口

目标：在用户本地重新运行脚本，确认 P11 修复效果。

需要完成：

1. 用户在本地运行 `python harness/scripts/check_harness_docs.py --root harness --format text`；
2. 将新输出保存为新的 self-check report；
3. 判断剩余 findings 是否为 false positive、模板例外、脚本能力缺口或真实问题；
4. 修复已确认的低风险问题；
5. 保持 no silent mutation。

### P13 - 阶段性治理报告归档收口

目标：处理 P8-P11 形成的阶段性报告资产。

需要完成：

1. 审查 `HarnessArchitectureAssessment.md`、`HarnessIndexDryRunReport.md`、`FrontmatterPathDryRunReport.md`、`RealHarnessSelfCheckReport.md`；
2. 将已经被 policy / index / PLANS 吸收的结论标记为 closed；
3. 按 [[ReportArchivePolicy]] 归档阶段性报告；
4. 确保归档报告不进入默认上下文；
5. 保留历史追溯，不直接删除。

### P14 - Obsidian 与 Git 跟踪边界收口

目标：确认 Obsidian UI 状态文件、workspace 状态和插件边界。

需要完成：

1. 评估 `.obsidian/graph.json` 是否已正确移出 Git tracking；
2. 确认 `.obsidian/workspace.json` 不作为事实源；
3. 确认插件运行代码不进入默认上下文；
4. 梳理剩余 alias 和 Obsidian wikilink 歧义；
5. 必要时更新 `.gitignore` 和 Obsidian 说明文档。

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

## 9. 需要用户后续输入的内容

以下内容不应由通用 HarnessVault 预置，需要用户在具体项目或知识库建设阶段输入：

1. 具体项目需求、架构、仓库、分支、接口、数据、测试和 ADR；
2. 具体项目编程规范、代码风格、审查规则和测试规则；
3. 真实领域知识、标准资料、论文、网页资料、NotebookLM 输出；
4. 用户长期偏好、组织内部约束和项目长期决策；
5. 可复用但需要真实任务验证的 Skill；
6. 真实 dry-run、真实验证、真实失败归因和真实回归报告。

这些内容应通过 [[KnowledgeIntakePolicy]]、[[ProjectIndex]]、[[MemoryPolicy]]、[[SkillPolicy]] 和 [[KnowledgePromotionPolicy]] 引入，而不是直接写入通用模板。

## 10. 完成态判断

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

## 11. 风险与注意事项

1. 治理报告是证据，不是长期事实源。
2. 阶段性报告应关闭和归档，不应长期进入默认上下文。
3. 自检脚本只允许 dry-run，不允许自动修改文档。
4. Project Template 只保留通用占位，不填入具体项目事实。
5. `templates/**` 是唯一模板源，后续提示词模板也进入该目录。
6. Knowledge intake 只能保存候选和模板，不得把未审查内容写入 RAG 或 Project Facts。
7. HarnessVault 不实现 agent runtime、sandbox、tool routing、model call 或实际任务执行。

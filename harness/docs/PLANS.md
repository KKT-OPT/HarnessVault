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
version: v0.13.0
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
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 阶段计划

## 1. 当前阶段

当前阶段：`P12 - 真实 self-check 复测结果收口与 README 链接规则泛化`

P12 的目标是在 P11 已完成模板统一治理和主要链接歧义收口的基础上，处理用户本地复测后剩余 findings，并将 README 链接治理和 `templates/**` 检查规则泛化，避免因后续增加、删除或重命名知识库、报告、项目模板分区而产生大量返工。

P12 不写入真实用户知识，不写入具体项目事实，不导入外部知识正文，不大规模重命名目录文件；本阶段优先通过唯一 alias、路径说明和脚本规则泛化消除当前误报与歧义。

## 2. P0-P11 状态

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

## 3. P11 验收结论

P11 已满足验收标准：

1. `AGENTS.md` 和 `README.md` 已包含 frontmatter，并保持 `AGENTS.md` 作为智能体优先入口。
2. `templates/**` 已定义为唯一模板源。
3. `docs/project-template/**` 不再保存重复 workflow 模板正文。
4. [[ProjectIndex]] 不再使用裸 `README` wikilink。
5. `WorkflowTemplate` 的重复模板源已收口。
6. `check_harness_docs.py` 已支持 template-aware 检查和 finding 去重。
7. [[RealHarnessSelfCheckReport]] 已记录 P11 前真实 dry-run 输出分类和修复策略。
8. P11 未写入真实用户知识，未写入具体项目事实。

## 4. P12 输入问题

用户在 P11 合并后本地复测 `check_harness_docs.py`，剩余 findings 可归为两类：

1. 裸 README wikilink 导致的候选歧义；
2. `templates/README.md` 作为模板索引被脚本误判为模板文件。

P12 不把本次复测数字写成长期架构事实。具体运行结果只进入 self-check report；[[PLANS]] 只保存阶段目标、验收标准和通用治理规则。

## 5. P12 设计原则

P12 采用以下原则：

1. 根目录 `README.md` 作为 vault 说明文档保留。
2. 子目录 README 可以继续作为目录说明文件存在，但必须具备唯一 alias，并避免使用裸 `README` wikilink。
3. 后续如果某个子目录 README 长期造成 Obsidian 链接歧义，可再按分区改名，例如 `REPORTS_README.md`、`RAG_README.md`，但 P12 不做大规模重命名。
4. `templates/**` 可以包含模板文件和模板索引；`type: template` 才要求 `templateName`、`templateTarget`、`templateEngine`、`templatePurpose`。
5. `type: index` 的 `templates/README.md` 应按普通 index 检查，而不是按模板文件检查。
6. 禁止使用裸 `[[README]]`；需要引用 README 时，使用唯一 alias 或路径文本。
7. 自检脚本继续保持 dry-run，只读，不自动修改文档。

## 6. P12 目标

P12 要完成：

1. 修复 [[PLANS]] 和 [[RealHarnessSelfCheckReport]] 中剩余的裸 README wikilink 描述。
2. 更新 `check_harness_docs.py`，使 `templates/**` 下的 index 文档不再被误判为 template。
3. 新增或更新 README 链接治理规则，明确裸 README wikilink 禁止使用。
4. 新增 `docs/reports/index/P12SelfCheckCloseoutReport.md`，记录 P12 复测结果分类和修复策略。
5. 更新 reports index，挂接 P12 self-check closeout report。
6. 保持通用 Harness 架构，不写死具体知识库扩展或具体项目事实。

## 7. P12 验收标准

P12 完成标准：

1. 自检脚本不再把 `templates/README.md` 误判为 `type: template` 文件。
2. `check_harness_docs.py` 对 `templates/**` 的规则为：`type: template` 才要求模板字段，`type: index` 使用普通必填字段。
3. `PLANS.md` 不再包含裸 `README` wikilink。
4. `RealHarnessSelfCheckReport.md` 不再包含裸 `README` wikilink。
5. 新增或更新的 README 链接治理规则不依赖当前固定目录数量。
6. P12 复测结果分类进入 report，不成为长期架构事实。
7. 本阶段不大规模重命名子目录 README，避免后续扩展知识库时产生不必要返工。
8. 本阶段不写入真实用户知识，不写入具体项目事实。
9. 本阶段不修改 `main`，通过 P12 分支和 PR 交付。

## 8. 后续剩余落地路线

### P13 - 阶段性治理报告归档收口

目标：处理 P8-P12 形成的阶段性报告资产。

需要完成：

1. 审查阶段性 self-check、dry-run、architecture assessment 报告；
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

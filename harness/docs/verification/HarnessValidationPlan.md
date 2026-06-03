---
documentName: docs/verification/HarnessValidationPlan.md
title: Harness Validation Plan
aliases:
  - HarnessValidationPlan
  - Harness Validation
  - Harness 验证计划
tags:
  - harness
  - verification
  - validation
version: v0.1.1
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义通用 Harness 架构完成后的验证方法和完成判据。
scope: HarnessVault verification。
prerequisites:
  - docs/verification/VerificationIndex.md
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[VerificationIndex]]"
  - "[[HarnessEngineering]]"
  - "[[HarnessValidationCases]]"
  - "[[HarnessInteractionSimulation]]"
  - "[[ReadinessCheckPolicy]]"
  - "[[RegressionPolicy]]"
  - "[[TraceSchema]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Validation Plan

## 1. 目的

本文档定义通用 Harness 架构完成后的验证方法和完成判据。

验证目标不是测试某个具体项目功能，而是确认任意智能体能否通过 HarnessVault 的入口、索引、RAG、Project Template、Workflow、Verification、Observability、Reports 和 Governance 完成一次受控任务闭环。

## 2. 验证原则

1. 不依赖特定 agent runtime；
2. 不写入真实用户知识；
3. 不写入具体项目事实；
4. 使用模拟项目和占位输入；
5. 全流程可追踪；
6. 失败必须能归因；
7. 结果必须能形成 report。

## 3. 验证范围

| 层级 | 验证问题 |
|---|---|
| Entry | 智能体是否能从 `AGENTS.md`、[[INDEX]]、[[PLANS]] 进入任务 |
| Context | 是否按 [[ContextLoadingPolicy]] 加载最小必要上下文 |
| RAG | 是否能区分 intake、standard、domain 和 active RAG |
| Project Template | 是否能将模板实例化为模拟项目结构 |
| Skill | 是否能识别 Skill 只可候选或模板化使用 |
| Memory | 是否能避免写入真实 Memory |
| Workflow | 是否能记录任务计划、执行、验收和候选晋升 |
| Observability | 是否能生成 trace 摘要和失败归因 |
| Verification | 是否能执行 readiness、acceptance、regression 规则 |
| Governance | 是否能遵守安全、归档、清理和知识晋升规则 |
| Reports | 是否能输出报告而不是静默修改 |

## 4. 验证用例

详细、可重复执行的 P15 验证用例清单见 [[HarnessValidationCases]]。本节保留验证类别摘要，正式 P15 报告应逐项引用 [[HarnessValidationCases]] 的输入、读取路径、预期行为、禁止行为和通过标准。

### 4.1 文档查找用例

输入：用户要求智能体查找某类知识。

期望：智能体通过 `AGENTS.md` → [[INDEX]] → [[RAGIndex]] → intake / standard / domain 分区定位知识入口，并能说明是否缺少真实知识。

### 4.2 项目实例化用例

输入：用户要求基于 Project Template 创建模拟项目文档结构。

期望：智能体读取 [[ProjectIndex]]，复制或说明 `docs/project-template/` 到模拟 `docs/project/` 的步骤，不写入真实项目事实。

### 4.3 任务执行闭环用例

输入：用户给出一条模拟任务 prompt。

期望：智能体完成 readiness check、计划、执行说明、验收、trace 摘要、failure attribution 或 regression 记录。

### 4.4 知识引入用例

输入：用户提供一段领域知识。

期望：智能体不直接写入 RAG，而是使用 [[KnowledgeIntakeTemplate]] 形成候选，并说明审查和晋升路径。

### 4.5 报告归档用例

输入：用户要求处理旧 dry-run 报告。

期望：智能体读取 [[ReportArchivePolicy]]，判断应关闭、归档或保留，不直接删除。

## 5. 通过标准

Harness 验证通过，当：

1. 智能体能找到正确入口；
2. 智能体能解释各层边界；
3. 智能体不会把 intake 当作事实源；
4. 智能体不会把 report 当作事实源；
5. 智能体不会把具体项目事实写入通用 HarnessVault；
6. 智能体能生成 workflow / trace / report 结构；
7. 智能体能执行 readiness 和 regression 判断；
8. 智能体能提出候选晋升而不是直接写入长期资产；
9. 验证结果可形成报告。

## 6. 失败处理

验证失败时应根据 [[FailureAttributionPolicy]] 归因，常见失败包括：

1. 入口加载失败；
2. 索引找不到目标文档；
3. 上下文加载过多或过少；
4. 错把候选当事实；
5. 错把报告当事实；
6. 未执行 readiness；
7. 未生成 trace；
8. 未记录 regression；
9. 直接写入用户知识或具体项目事实。

## 7. 关联文档

- [[VerificationIndex]]
- [[HarnessEngineering]]
- [[HarnessValidationCases]]
- [[HarnessInteractionSimulation]]
- [[ReadinessCheckPolicy]]
- [[RegressionPolicy]]
- [[TraceSchema]]

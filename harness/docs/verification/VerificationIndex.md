---
documentName: docs/verification/VerificationIndex.md
title: Verification Index
aliases:
  - VerificationIndex
  - Verification 文档索引
  - 验证索引
tags:
  - harness
  - verification
  - index
version: v0.2.1
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的 verification 文档，定义 readiness、acceptance、regression 和架构验证入口。
scope: HarnessVault verification。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/RuntimeBoundaryPolicy.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[RuntimeBoundaryPolicy]]"
  - "[[ReadinessCheckPolicy]]"
  - "[[RegressionPolicy]]"
  - "[[HarnessValidationPlan]]"
  - "[[HarnessValidationCases]]"
  - "[[HarnessInteractionSimulation]]"
  - "[[ObservabilityIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Verification Index

## 1. 层级定位

Verification Layer 负责定义 agent runtime 执行前、执行后、修复后和 Harness 架构完成态的验证规则。

HarnessVault 不运行测试、不执行 benchmark、不调用 runtime。HarnessVault 只定义 readiness、acceptance、regression、failure repair loop 和 Harness 架构验证的文档规则。

## 2. 文档列表

| 文档 | 状态 | 用途 |
|---|---|---|
| [[ReadinessCheckPolicy]] | draft | 定义执行前任务、上下文、权限、分支、验收准备检查 |
| [[RegressionPolicy]] | draft | 定义修复后复测、回归验证、失败闭环和验收收口规则 |
| [[HarnessValidationPlan]] | draft | 定义通用 Harness 架构完成后的验证方法和完成判据 |
| [[HarnessValidationCases]] | draft | 定义 P15 完成态验证可直接使用的通用 Harness 验证用例清单 |
| [[HarnessInteractionSimulation]] | draft | 模拟智能体如何基于 HarnessVault 完成一次任务闭环 |

## 3. 验证闭环

```text
task grounding
→ readiness check
→ runtime execution
→ trace capture
→ acceptance check
→ failure attribution
→ repair
→ regression check
→ close
```

## 4. Harness 架构验证闭环

```text
entry discovery
→ context routing
→ knowledge routing
→ project-template routing
→ readiness
→ trace summary
→ verification
→ report
→ candidate promotion
→ archive / close
```

## 5. 与 runtime 的边界

| 内容 | Runtime 负责 | HarnessVault 负责 |
|---|---|---|
| 测试执行 | 运行命令、返回结果 | 定义应记录的测试摘要和验收规则 |
| benchmark | 执行评测 | 记录评测条件与结论摘要 |
| readiness | 检查环境和权限 | 定义检查清单 |
| regression | 复测和比较 | 定义复测触发条件和记录格式 |
| acceptance | 实际验收执行 | 定义验收标准结构和闭环规则 |
| harness validation | 模拟任务执行 | 定义验证用例、通过标准和失败归因 |

## 6. 关联文档

- [[HarnessEngineering]]
- [[RuntimeBoundaryPolicy]]
- [[ReadinessCheckPolicy]]
- [[RegressionPolicy]]
- [[HarnessValidationPlan]]
- [[HarnessValidationCases]]
- [[HarnessInteractionSimulation]]
- [[ObservabilityIndex]]

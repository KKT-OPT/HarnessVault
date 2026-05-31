---
documentName: docs/observability/ObservabilityIndex.md
title: Observability Index
aliases:
  - ObservabilityIndex
  - Observability 文档索引
  - 可观测性索引
tags:
  - harness
  - observability
  - index
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的 observability 文档，定义任务 trace、操作事件和失败归因记录入口。
scope: HarnessVault observability。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/RuntimeBoundaryPolicy.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[RuntimeBoundaryPolicy]]"
  - "[[TraceSchema]]"
  - "[[FailureAttributionPolicy]]"
  - "[[VerificationIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Observability Index

## 1. 层级定位

Observability Layer 负责定义智能体任务执行过程中的 trace、操作事件、证据、失败、成本、耗时和人工介入记录结构。

HarnessVault 不采集 runtime 原始 trace，不实现监控系统。HarnessVault 只定义 runtime 输出进入文档系统时应采用的摘要结构和治理边界。

## 2. 文档列表

| 文档 | 状态 | 用途 |
|---|---|---|
| [[TraceSchema]] | draft | 定义任务 trace、operation event、evidence、cost、human intervention 的最小记录结构 |
| [[FailureAttributionPolicy]] | draft | 定义失败归因维度、记录方式和修复闭环入口 |

## 3. 与 runtime 的边界

| 内容 | Runtime 负责 | HarnessVault 负责 |
|---|---|---|
| 原始 trace | 采集、存储、导出 | 不直接保存大对象 |
| 操作事件 | 生成事件 | 定义摘要字段 |
| 成本 / 耗时 | 采集 metrics | 记录摘要与风险 |
| 失败详情 | 产生日志和错误 | 归因分类与证据链接 |
| 人工介入 | 请求权限或确认 | 记录介入原因和结论 |

## 4. 关联文档

- [[HarnessEngineering]]
- [[RuntimeBoundaryPolicy]]
- [[TraceSchema]]
- [[FailureAttributionPolicy]]
- [[VerificationIndex]]

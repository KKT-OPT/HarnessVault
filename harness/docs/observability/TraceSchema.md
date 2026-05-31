---
documentName: docs/observability/TraceSchema.md
title: Trace Schema
aliases:
  - TraceSchema
  - Trace Schema
  - 任务轨迹结构
tags:
  - harness
  - observability
  - trace
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 agent runtime 输出进入 HarnessVault 时的最小 trace 摘要结构。
scope: HarnessVault observability。
prerequisites:
  - docs/observability/ObservabilityIndex.md
relatedDocuments:
  - "[[ObservabilityIndex]]"
  - "[[RuntimeBoundaryPolicy]]"
  - "[[FailureAttributionPolicy]]"
  - "[[WorkflowTemplate]]"
  - "[[GovernanceReportTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Trace Schema

## 1. 目的

本文档定义 agent runtime 执行结果进入 HarnessVault 时应记录的最小 trace 摘要结构。

HarnessVault 不保存完整 raw trace、完整上下文窗口、完整终端日志或敏感信息。Trace Schema 只用于保存可审查、可验证、可归因的摘要证据。

## 2. Trace Metadata

| 字段 | 含义 | 示例 |
|---|---|---|
| traceId | trace 唯一标识 | `<trace-id>` |
| taskId | 对应任务或 workflow id | `<task-id>` |
| runtime | 执行 runtime | `Codex / Claude Code / Hermes / OpenClaw / other` |
| branch | 执行分支 | `<branch>` |
| mode | 执行模式 | `read-only / write / submit-pr` |
| startedAt | 开始时间 | `<timestamp>` |
| endedAt | 结束时间 | `<timestamp>` |
| status | 执行状态 | `success / failed / partial / aborted` |

## 3. Context Snapshot

记录执行时加载的关键上下文，不记录完整上下文内容。

| 字段 | 含义 |
|---|---|
| entryDocs | 入口文档列表 |
| policyDocs | 关键 policy 列表 |
| projectDocs | 项目事实文档列表 |
| codeScope | 代码读取或修改范围 |
| excludedContext | 明确排除的上下文 |

## 4. Operation Events

每个关键操作记录一行摘要：

| 字段 | 含义 |
|---|---|
| eventId | 事件 id |
| eventType | `read / write / command / test / search / commit / pr / approval / report` |
| target | 文件、命令、工具或文档 |
| intent | 操作目的 |
| result | `success / failed / skipped` |
| evidence | 证据链接或摘要 |
| risk | `low / medium / high` |

## 5. Tool and Runtime Summary

| 字段 | 含义 |
|---|---|
| toolsUsed | 使用的工具列表 |
| commandsRun | 命令摘要，不粘贴大段输出 |
| filesChanged | 修改文件列表 |
| testsRun | 测试摘要 |
| permissionsRequested | 权限请求摘要 |
| humanInterventions | 人工介入摘要 |

## 6. Cost and Time Summary

| 字段 | 含义 |
|---|---|
| elapsedTime | 总耗时 |
| modelCalls | 模型调用次数，若 runtime 可提供 |
| toolCalls | 工具调用次数 |
| tokenSummary | token 摘要，若 runtime 可提供 |
| costSummary | 成本摘要，若 runtime 可提供 |

## 7. Failure Summary

当任务失败或部分成功时，记录：

| 字段 | 含义 |
|---|---|
| failureType | 失败类型 |
| failureStage | 失败阶段 |
| failureEvidence | 失败证据 |
| suspectedCause | 初步归因 |
| retryable | `yes / no / unknown` |
| nextAction | 建议下一步 |

详细归因遵循 [[FailureAttributionPolicy]]。

## 8. Promotion Candidates

Trace 可以产生候选，但不能直接写入长期资产：

1. Memory Candidate；
2. Skill Candidate；
3. RAG Candidate；
4. Project Fact Candidate；
5. Governance Fix Candidate。

候选晋升必须遵守 [[KnowledgePromotionPolicy]]。

## 9. 禁止记录

Trace 文档中不得保存：

1. secret、token、password、private key；
2. 未脱敏日志；
3. 完整模型上下文；
4. 完整 raw terminal transcript；
5. 大段代码；
6. 未审查外部网页全文；
7. 插件运行代码。

## 10. 关联文档

- [[ObservabilityIndex]]
- [[RuntimeBoundaryPolicy]]
- [[FailureAttributionPolicy]]
- [[WorkflowTemplate]]
- [[GovernanceReportTemplate]]

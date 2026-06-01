---
documentName: docs/governance/ReportArchivePolicy.md
title: Report Archive Policy
aliases:
  - ReportArchivePolicy
  - Report Archive
  - 报告归档规则
tags:
  - harness
  - governance
  - reports
  - archive
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义阶段性治理报告、dry-run 报告和历史报告的关闭、归档和默认上下文排除规则。
scope: HarnessVault reports governance。
prerequisites:
  - docs/governance/CleanupPolicy.md
  - docs/reports/README.md
relatedDocuments:
  - "[[GovernanceIndex]]"
  - "[[CleanupPolicy]]"
  - "[[ScheduledGovernance]]"
  - "[[ReportsIndex]]"
  - "[[ReportsArchive]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Report Archive Policy

## 1. 目的

本文档定义 HarnessVault 阶段性治理报告、dry-run 报告和历史报告的关闭、归档和默认上下文排除规则。

报告是治理证据，不是长期事实源。报告中的结论只有被写入正式 policy、index、PLANS 或模板后，才成为 Harness 文档事实。

## 2. 报告状态

| 状态 | 含义 | 默认上下文 |
|---|---|---|
| draft | 报告草稿或结构性示例 | 否 |
| active | 当前阶段仍在使用的报告 | 谨慎 |
| reviewed | 已经人工审查 | 谨慎 |
| closed | 结论已处理或明确不处理 | 否 |
| archived | 历史保留 | 否 |

## 3. 关闭条件

报告满足以下任一条件时，应标记为 `closed`：

1. 报告建议已被正式文档吸收；
2. 报告建议被明确拒绝；
3. 报告只用于阶段性验证，阶段已结束；
4. 后续报告已经替代当前报告；
5. 报告仅为结构性示例。

## 4. 归档条件

报告满足以下条件时，应进入 archive：

1. 状态已为 `closed`；
2. 不再作为当前任务输入；
3. 仍有历史追溯价值；
4. 归档不会破坏索引链路；
5. 已更新对应 reports index。

## 5. 默认上下文规则

智能体默认不得加载：

1. archived report；
2. closed report；
3. 结构性示例报告；
4. 被正式 policy 吸收后的旧 dry-run 报告。

除非用户明确要求追溯历史，否则不应读取 archived reports。

## 6. P8 / P9 阶段报告处理建议

以下报告属于阶段性治理资产：

1. [[HarnessArchitectureAssessment]]；
2. [[HarnessIndexDryRunReport]]；
3. [[FrontmatterPathDryRunReport]]。

它们不应长期作为默认事实源。后续在 P12 或 P15 前，应根据本规则关闭并归档。

## 7. 归档流程

```text
report reviewed
→ conclusions absorbed / rejected / deferred
→ status: closed
→ move or link from archive section
→ status: archived
→ remove from default recommended context
```

## 8. 禁止事项

1. 禁止直接删除仍有追溯价值的报告。
2. 禁止把 archived report 当作当前事实源。
3. 禁止把 report 建议绕过人工审查直接写入正式文档。
4. 禁止在报告中保存 secret 或未脱敏日志。

## 9. 关联文档

- [[GovernanceIndex]]
- [[CleanupPolicy]]
- [[ScheduledGovernance]]
- [[ReportsIndex]]
- [[ReportsArchive]]

---
documentName: docs/reports/archive/README.md
title: Reports Archive README
aliases:
  - ReportsArchive
  - Reports Archive
  - 报告归档区
tags:
  - harness
  - reports
  - archive
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 reports archive 分区规则；用于保存 closed / archived 报告。
scope: HarnessVault reports archive。
prerequisites:
  - docs/governance/ReportArchivePolicy.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[ReportArchivePolicy]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Reports Archive README

## 1. 定位

`docs/reports/archive/` 用于保存已经关闭或归档的治理报告、dry-run 报告和历史审查记录。

Archive 报告是历史证据，不是当前事实源，不应进入智能体默认上下文。

## 2. 准入条件

进入本目录的报告应满足：

1. 已经审查；
2. 已经关闭或明确需要历史保留；
3. 不再作为当前任务输入；
4. 结论已被正式文档吸收、拒绝或延期；
5. 不包含 secret 或未脱敏日志。

## 3. 命名建议

```text
YYYYMMDD-archived-<report-name>.md
```

## 4. 禁止事项

1. 禁止把 archive 报告作为默认上下文。
2. 禁止直接删除仍有追溯价值的报告。
3. 禁止把 archive 报告中的旧结论当作当前事实。

## 5. 关联文档

- [[ReportsIndex]]
- [[ReportArchivePolicy]]
- [[CleanupPolicy]]

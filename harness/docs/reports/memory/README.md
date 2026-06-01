---
documentName: docs/reports/memory/README.md
title: Memory Reports README
aliases:
  - MemoryReports
  - Memory Reports README
  - Memory 报告
tags:
  - harness
  - reports
  - memory
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 Memory 报告分区规则；当前不保存真实 Memory 审查结果。
scope: HarnessVault memory reports。
prerequisites:
  - docs/agent/MemoryPolicy.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[MemoryPolicy]]"
  - "[[MemoryGovernance]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Memory Reports README

## 1. 定位

`docs/reports/memory/` 用于保存 Memory 候选、污染、过期、重复、归档和晋升审查报告。

当前通用 HarnessVault 只建立报告分区规则，不保存真实 Memory 审查结果。

## 2. 报告类型

1. Memory candidate review；
2. Memory pollution check；
3. Memory duplicate check；
4. Memory archive report；
5. Memory promotion report。

## 3. 报告规则

1. 报告是证据，不是事实源。
2. 报告不得直接写入 active Memory。
3. 报告建议必须经人工审查后才能执行。
4. 报告关闭后可按 [[CleanupPolicy]] 归档。

## 4. 关联文档

- [[ReportsIndex]]
- [[MemoryPolicy]]
- [[MemoryGovernance]]
- [[CleanupPolicy]]

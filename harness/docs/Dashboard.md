---
documentName: docs/Dashboard.md
title: Harness Dashboard
aliases:
  - Dashboard
  - Harness Dashboard
  - 仪表盘
tags:
  - harness
  - dashboard
  - obsidian
  - dataview
version: v0.1.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-29 00:00:00.000 +08:00
status: draft
type: report
purpose: 使用 Obsidian Dataview 为 HarnessVault 提供动态文档治理视图。
scope: HarnessVault Obsidian vault。
prerequisites:
  - docs/INDEX.md
  - docs/PLANS.md
relatedDocuments:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
  - docs/PLANS.md
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-29 00:00:00.000 +08:00
---

# Harness Dashboard

> 本文档是 Obsidian Dataview 辅助视图，不替代 [[INDEX]]。正式文档导航仍以 [[INDEX]] 为准。

## 1. Draft Documents

```dataview
TABLE version, updatedAt, reviewAfter, owner, purpose
FROM "docs"
WHERE status = "draft"
SORT updatedAt DESC
```

## 2. Review Due

```dataview
TABLE status, reviewAfter, owner, purpose
FROM "docs"
WHERE reviewAfter AND date(reviewAfter) <= date(today)
SORT reviewAfter ASC
```

## 3. Governance Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE contains(tags, "governance")
SORT file.name ASC
```

## 4. Architecture Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE type = "architecture-design"
SORT file.name ASC
```

## 5. Index Documents

```dataview
TABLE version, status, updatedAt, purpose
FROM "docs"
WHERE type = "index"
SORT file.name ASC
```

## 6. Plan Documents

```dataview
TABLE version, status, updatedAt, purpose
FROM "docs"
WHERE type = "plan"
SORT file.name ASC
```

## 7. Missing Review Date

```dataview
TABLE status, owner, updatedAt, purpose
FROM "docs"
WHERE !reviewAfter
SORT file.path ASC
```

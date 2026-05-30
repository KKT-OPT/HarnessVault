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
version: v0.2.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-30 00:00:00.000 +08:00
status: draft
type: report
purpose: 使用 Obsidian Dataview 为 HarnessVault 提供动态文档治理视图。
scope: HarnessVault Obsidian vault。
prerequisites:
  - docs/INDEX.md
  - docs/PLANS.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[GovernanceIndex]]"
  - "[[AgentIndex]]"
  - "[[RAGIndex]]"
  - "[[ProjectIndex]]"
  - "[[ObsidianSetup]]"
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

## 3. Index Documents

```dataview
TABLE version, status, updatedAt, purpose
FROM "docs"
WHERE type = "index"
SORT file.path ASC
```

## 4. Policy Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE type = "policy"
SORT file.path ASC
```

## 5. Governance Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE contains(tags, "governance")
SORT file.path ASC
```

## 6. Agent Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE contains(tags, "agent")
SORT file.path ASC
```

## 7. RAG Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE contains(tags, "rag")
SORT file.path ASC
```

## 8. Project Template Documents

```dataview
TABLE version, status, updatedAt, reviewAfter
FROM "docs"
WHERE contains(tags, "project-template")
SORT file.path ASC
```

## 9. Missing Review Date

```dataview
TABLE status, owner, updatedAt, purpose
FROM "docs"
WHERE !reviewAfter
SORT file.path ASC
```

## 10. Missing Owner

```dataview
TABLE status, updatedAt, purpose
FROM "docs"
WHERE !owner
SORT file.path ASC
```

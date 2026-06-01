---
documentName: docs/reports/rag/README.md
title: RAG Reports README
aliases:
  - RAGReports
  - RAG Reports README
  - RAG 报告
tags:
  - harness
  - reports
  - rag
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 RAG 报告分区规则；当前不保存真实 RAG 审查结果。
scope: HarnessVault RAG reports。
prerequisites:
  - docs/rag/KnowledgeBasePolicy.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[RAGIndex]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# RAG Reports README

## 1. 定位

`docs/reports/rag/` 用于保存 RAG 来源、审查、过期、未审查知识、知识引入和知识晋升报告。

当前通用 HarnessVault 只建立报告分区规则，不保存真实 RAG 审查结果。

## 2. 报告类型

1. RAG source review；
2. RAG stale review；
3. Knowledge intake review；
4. RAG promotion report；
5. External source risk report。

## 3. 报告规则

1. 报告是证据，不是事实源。
2. 报告不得直接写入 active RAG。
3. 外部资料报告必须经过人工审查后才能进入 RAG。
4. 报告关闭后可按 [[CleanupPolicy]] 归档。

## 4. 关联文档

- [[ReportsIndex]]
- [[RAGIndex]]
- [[KnowledgeBasePolicy]]
- [[KnowledgeIntakePolicy]]
- [[CleanupPolicy]]

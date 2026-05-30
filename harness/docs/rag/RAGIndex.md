---
documentName: docs/rag/RAGIndex.md
title: RAG Index
aliases:
  - RAGIndex
  - RAG 文档索引
  - 知识库索引
tags:
  - harness
  - rag
  - index
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-30 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的 RAG 知识库文档。
scope: HarnessVault RAG。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# RAG Index

## 1. 层级定位

RAG Knowledge Layer 用于保存稳定、经过审查、可检索的知识库内容。

RAG 不保存任务历史，不直接保存一次性 workflow，不替代 Project Facts。

## 2. 知识库治理文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[KnowledgeBasePolicy]] | draft | 定义 RAG 知识库的来源、审查、更新和只读规则 |
| [[KnowledgePromotionPolicy]] | draft | 定义 Workflow / Memory / Skill 晋升为 RAG 的规则 |

## 3. 当前知识库分区

| 分区 | 状态 | 用途 |
|---|---|---|
| `docs/rag/standard/` | planned | 文档、代码、测试、审查等规范知识 |
| `docs/rag/domain/` | planned | 领域知识、方法论和外部资料整理 |

## 4. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[INDEX]]
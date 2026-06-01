---
documentName: docs/rag/standard/README.md
title: RAG Standard README
aliases:
  - RAGStandard
  - RAG Standard README
  - 规范知识库
tags:
  - harness
  - rag
  - standard
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 RAG standard 分区规则；当前不保存真实规范知识正文。
scope: HarnessVault RAG standard。
prerequisites:
  - docs/rag/KnowledgeBasePolicy.md
relatedDocuments:
  - "[[RAGIndex]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgeIntakePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# RAG Standard README

## 1. 定位

`docs/rag/standard/` 用于保存经过审查的通用规范知识，例如文档规范、编码规范、测试规范、审查规范和治理规范。

当前通用 HarnessVault 只建立分区规则，不保存真实规范知识正文。

## 2. 准入规则

进入本分区的知识必须：

1. 来源明确；
2. 经过审查；
3. 可跨项目复用；
4. 不属于具体项目事实；
5. 不属于一次性任务记录；
6. 已更新 [[RAGIndex]] 或本分区索引。

## 3. 候选来源

未审查内容应先进入：

```text
docs/rag/intake/
```

通过 [[KnowledgeIntakePolicy]] 审查后，才可晋升到本分区。

## 4. 关联文档

- [[RAGIndex]]
- [[KnowledgeBasePolicy]]
- [[KnowledgeIntakePolicy]]

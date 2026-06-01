---
documentName: docs/rag/domain/README.md
title: RAG Domain README
aliases:
  - RAGDomain
  - RAG Domain README
  - 领域知识库
tags:
  - harness
  - rag
  - domain
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 RAG domain 分区规则；当前不保存真实领域知识正文。
scope: HarnessVault RAG domain。
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

# RAG Domain README

## 1. 定位

`docs/rag/domain/` 用于保存经过审查的稳定领域知识、方法论、外部资料整理和跨项目可复用的知识内容。

当前通用 HarnessVault 只建立分区规则，不保存真实领域知识正文。

## 2. 准入规则

进入本分区的知识必须：

1. 来源明确；
2. 经过人工审查；
3. 内容稳定；
4. 适合跨任务或跨项目复用；
5. 不属于具体项目事实；
6. 不包含敏感信息；
7. 已设置 reviewAfter。

## 3. 候选来源

未审查领域知识应先进入：

```text
docs/rag/intake/
```

通过 [[KnowledgeIntakePolicy]] 审查后，才可晋升到本分区。

## 4. 关联文档

- [[RAGIndex]]
- [[KnowledgeBasePolicy]]
- [[KnowledgeIntakePolicy]]

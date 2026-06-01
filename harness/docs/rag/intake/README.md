---
documentName: docs/rag/intake/README.md
title: Knowledge Intake README
aliases:
  - KnowledgeIntake
  - Intake README
  - 知识暂存区
tags:
  - harness
  - rag
  - intake
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义知识暂存区规则；intake 不是事实源。
scope: HarnessVault RAG intake。
prerequisites:
  - docs/rag/KnowledgeIntakePolicy.md
relatedDocuments:
  - "[[KnowledgeIntakePolicy]]"
  - "[[KnowledgeIntakeTemplate]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Knowledge Intake README

## 1. 定位

`docs/rag/intake/` 是知识暂存区，用于保存尚未审查的知识候选模板或候选记录。

intake 不是事实源，不进入默认上下文，不直接作为 RAG、Memory、Skill 或 Project Facts 使用。

## 2. 允许内容

允许存放：

1. 用户输入知识的候选记录；
2. 外部资料摘要候选；
3. NotebookLM / Web / PDF 资料整理候选；
4. RAG Candidate；
5. Project Fact Candidate；
6. Skill Candidate；
7. Memory Candidate。

## 3. 当前模板

| 文档 | 用途 |
|---|---|
| [[KnowledgeIntakeTemplate]] | 知识引入候选模板 |

## 4. 禁止事项

1. 禁止把 intake 内容作为事实源。
2. 禁止未经审查直接晋升。
3. 禁止保存敏感信息。
4. 禁止保存真实用户知识到通用 HarnessVault。
5. 禁止保存具体项目事实到通用 HarnessVault。

## 5. 关联文档

- [[KnowledgeIntakePolicy]]
- [[KnowledgeIntakeTemplate]]
- [[KnowledgeBasePolicy]]
- [[KnowledgePromotionPolicy]]

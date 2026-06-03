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
version: v0.1.1
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义知识暂存区规则；intake 不是事实源。
scope: HarnessVault RAG intake。
prerequisites:
  - docs/rag/KnowledgeIntakePolicy.md
relatedDocuments:
  - "[[KnowledgeIntakePolicy]]"
  - "[[KnowledgeIntakeTemplate]]"
  - "[[RAGRawIntake]]"
  - "[[RAGEnrichedIntake]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[EffectiveKnowledgeTemplate]]"
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

## 2. 子分区

| 分区 | 用途 | 事实源 |
|---|---|---|
| [[RAGRawIntake]] | 保存原始资料元信息、短摘要、来源和候选路由 | 否 |
| [[RAGEnrichedIntake]] | 保存语义增强、关键词、适用范围和可信度判断 | 否 |

raw / enriched 均是候选分区。未经人工审查和 promotion，不得进入 active RAG，不得作为长期事实依据。

## 3. 允许内容

允许存放：

1. 用户输入知识的候选记录；
2. 外部资料摘要候选；
3. NotebookLM / Web / PDF 资料整理候选；
4. raw material 元信息、短摘要和来源候选；
5. semantic enrichment 候选；
6. RAG Candidate；
7. Project Fact Candidate；
8. Skill Candidate；
9. Memory Candidate。

## 4. 当前模板

| 文档 | 用途 |
|---|---|
| [[KnowledgeIntakeTemplate]] | 知识引入候选模板 |
| [[RawKnowledgeMaterialTemplate]] | 原始资料元信息和短摘要候选模板 |
| [[EffectiveKnowledgeTemplate]] | 审查后的有效知识文档模板 |

## 5. 禁止事项

1. 禁止把 intake 内容作为事实源。
2. 禁止未经审查直接晋升。
3. 禁止把 raw / enriched 候选直接写入 active RAG。
4. 禁止保存大段原文、完整外部资料正文或敏感信息。
5. 禁止保存真实用户知识到通用 HarnessVault。
6. 禁止保存具体项目事实到通用 HarnessVault。

## 6. 关联文档

- [[KnowledgeIntakePolicy]]
- [[KnowledgeIntakeTemplate]]
- [[RAGRawIntake]]
- [[RAGEnrichedIntake]]
- [[RawKnowledgeMaterialTemplate]]
- [[EffectiveKnowledgeTemplate]]
- [[KnowledgeBasePolicy]]
- [[KnowledgePromotionPolicy]]

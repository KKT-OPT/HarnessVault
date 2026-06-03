---
documentName: docs/rag/KnowledgeBaseConstructionWorkflow.md
title: Knowledge Base Construction Workflow
aliases:
  - KnowledgeBaseConstructionWorkflow
  - Knowledge Base Construction
  - 知识库构建流程
tags:
  - harness
  - rag
  - knowledge-base
  - workflow
version: v0.1.1
createdAt: 2026-06-02 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义从原始资料到有效知识库文档的通用构建流程。
scope: HarnessVault RAG construction。
prerequisites:
  - docs/rag/KnowledgeIntakePolicy.md
  - docs/rag/KnowledgeBasePolicy.md
relatedDocuments:
  - "[[RAGIndex]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
  - "[[RAGRawIntake]]"
  - "[[RAGEnrichedIntake]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[EffectiveKnowledgeTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Knowledge Base Construction Workflow

## 1. 目的

本文档定义从原始资料到有效知识库文档的通用构建流程，使用户可以快速建立知识库，同时避免未审查资料直接污染 RAG。

通用 HarnessVault 不保存真实知识正文，只提供流程和模板。

## 2. 分层模型

| 层级 | 目录建议 | 内容 | 是否事实源 |
|---|---|---|---|
| Raw Material Layer | `docs/rag/intake/raw/` | 原始资料摘要、链接、PDF/网页/笔记元信息 | 否 |
| Semantic Enrichment Layer | `docs/rag/intake/enriched/` | 用户或智能体补充的术语、关键词、适用范围、可信度判断 | 否 |
| Effective Knowledge Layer | `docs/rag/domain/` 或 `docs/rag/standard/` | 审查后的有效知识文档 | 是 |
| Review / Promotion Layer | `docs/reports/rag/` | 审查、冲突、晋升和归档报告 | 证据，不是事实源 |

## 3. 构建流程

```text
raw material
→ raw material template
→ semantic enrichment
→ effective knowledge draft
→ human review
→ promotion to RAG domain / standard
→ index update
→ reviewAfter scheduling
```

## 4. 人类负责的内容

人类更适合补充：

1. 原始资料来源可信度；
2. 使用场景；
3. 术语解释；
4. 哪些内容重要，哪些可以忽略；
5. 领域判断；
6. 与项目事实的边界；
7. 是否允许晋升为有效知识。

## 5. 智能体负责的内容

智能体可以辅助：

1. 将原始资料整理为 `RawKnowledgeMaterialTemplate`；
2. 提取关键词、别名、主题；
3. 识别候选知识点；
4. 根据模板生成 effective knowledge draft；
5. 检查是否已有重复知识；
6. 生成 review report；
7. 更新索引草案。

智能体不得：

1. 未经审查直接把 raw material 写入 active RAG；
2. 把具体项目事实写入通用 RAG；
3. 把外部资料原文大段复制为知识库正文；
4. 将 intake 内容作为事实源使用。

## 6. 目录建议

通用模板仓库只保留模板和规则。真实知识库建设时可使用：

```text
docs/rag/intake/raw/
docs/rag/intake/enriched/
docs/rag/domain/
docs/rag/standard/
docs/reports/rag/
```

`docs/rag/intake/raw/README.md` 和 `docs/rag/intake/enriched/README.md` 只定义空分区规则。两者不是事实源，不进入默认上下文，未经审查不得进入 active RAG。

## 7. 模板

| 模板 | 用途 |
|---|---|
| [[RawKnowledgeMaterialTemplate]] | 记录原始资料元信息和摘要 |
| [[EffectiveKnowledgeTemplate]] | 生成审查后的有效知识文档 |

## 8. 关联文档

- [[RAGIndex]]
- [[KnowledgeIntakePolicy]]
- [[KnowledgeBasePolicy]]
- [[KnowledgePromotionPolicy]]
- [[RAGRawIntake]]
- [[RAGEnrichedIntake]]
- [[RawKnowledgeMaterialTemplate]]
- [[EffectiveKnowledgeTemplate]]

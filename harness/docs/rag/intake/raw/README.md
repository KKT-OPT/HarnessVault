---
documentName: docs/rag/intake/raw/README.md
title: RAG Raw Intake README
aliases:
  - RAGRawIntake
tags:
  - harness
  - rag
  - intake
  - raw
version: v0.1.0
createdAt: 2026-06-03 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 raw material 分区规则；当前不保存真实原始资料正文。
scope: HarnessVault RAG raw intake。
prerequisites:
  - docs/rag/KnowledgeBaseConstructionWorkflow.md
  - docs/rag/KnowledgeIntakePolicy.md
relatedDocuments:
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[KnowledgeIntake]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# RAG Raw Intake README

## 1. 定位

`docs/rag/intake/raw/` 是 raw material 候选分区，用于保存原始资料的元信息、短摘要、来源、风险标注和后续路由建议。

本分区不是事实源，不进入默认上下文，不属于 active RAG。通用 HarnessVault 只保留空分区规则，不保存真实原始资料正文。

## 2. 允许内容

允许保存：

1. 原始资料来源类型、位置、作者或组织、发布时间和收集时间；
2. 经过转述的短摘要；
3. 使用权、敏感性、版权风险和可信度的初步标注；
4. 候选关键词、别名、标准术语和领域术语；
5. 是否可能进入 RAG domain、RAG standard、Project Facts、Skill 或 Memory 的路由建议。

## 3. 禁止事项

禁止：

1. 保存大段原文、完整文章、完整 PDF 正文或长篇外部资料摘录；
2. 把 raw material 当作事实源引用；
3. 未经审查直接晋升到 active RAG；
4. 在通用 HarnessVault 中保存真实用户知识、具体项目事实、敏感信息或私有资料正文；
5. 用模型推断替代来源标注和人工审查。

## 4. 模板入口

新增 raw material 候选时，应优先使用 [[RawKnowledgeMaterialTemplate]]。

生成后的候选文档仍保持 candidate 状态，只能作为后续 semantic enrichment、review 或 promotion 的输入。

## 5. 晋升路径

标准路径：

```text
raw material metadata
→ semantic enrichment
→ effective knowledge draft
→ human review
→ promotion to docs/rag/domain/ or docs/rag/standard/
```

raw 分区中的内容未经审查不得进入 active RAG，也不得作为 Memory、Skill 或 Project Facts 的长期事实依据。

## 6. 关联文档

- [[KnowledgeBaseConstructionWorkflow]]
- [[KnowledgeIntakePolicy]]
- [[RawKnowledgeMaterialTemplate]]
- [[KnowledgeIntake]]

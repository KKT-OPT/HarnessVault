---
documentName: docs/rag/intake/enriched/README.md
title: RAG Enriched Intake README
aliases:
  - RAGEnrichedIntake
tags:
  - harness
  - rag
  - intake
  - enriched
version: v0.1.0
createdAt: 2026-06-03 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 semantic enrichment 分区规则；当前不保存真实增强知识正文。
scope: HarnessVault RAG enriched intake。
prerequisites:
  - docs/rag/KnowledgeBaseConstructionWorkflow.md
  - docs/rag/KnowledgeIntakePolicy.md
relatedDocuments:
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[EffectiveKnowledgeTemplate]]"
  - "[[KnowledgeIntake]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# RAG Enriched Intake README

## 1. 定位

`docs/rag/intake/enriched/` 是 semantic enrichment 候选分区，用于保存人类或智能体在 raw material 基础上补充的语义、关键词、适用范围和可信度判断。

本分区不是事实源，不进入默认上下文，不属于 active RAG。通用 HarnessVault 只保留空分区规则，不保存真实增强知识正文。

## 2. 允许内容

允许保存：

1. 人类或智能体补充的术语解释、标准术语、别名和关键词；
2. 适用范围、不适用范围、领域边界和项目事实边界判断；
3. 来源可信度、稳定性、时效性、冲突风险和审查建议；
4. 与现有 RAG、Project Facts、Skill 或 Memory 的重复和冲突检查结果；
5. 是否生成 effective knowledge draft 的路由建议。

## 3. 禁止事项

禁止：

1. 把 enrichment 内容当作事实源引用；
2. 未经人工审查直接写入 `docs/rag/domain/` 或 `docs/rag/standard/`；
3. 在通用 HarnessVault 中保存真实用户知识、具体项目事实、敏感信息或私有资料正文；
4. 用未经验证的模型总结覆盖来源事实；
5. 保存无法追溯到 raw material 或明确人工输入的增强结论。

## 4. 模板入口

enriched 候选通常由 [[RawKnowledgeMaterialTemplate]] 生成的 raw material 候选发展而来。

当候选内容准备进入审查后的有效知识草案时，应使用 [[EffectiveKnowledgeTemplate]]，并在人工审查通过后再晋升到 `docs/rag/domain/` 或 `docs/rag/standard/`。

## 5. 晋升路径

标准路径：

```text
raw material candidate
→ semantic enrichment candidate
→ effective knowledge draft
→ human review
→ promotion to active RAG partition
```

enriched 分区中的内容未经审查不得进入 active RAG，也不得作为 Memory、Skill 或 Project Facts 的长期事实依据。

## 6. 关联文档

- [[KnowledgeBaseConstructionWorkflow]]
- [[KnowledgeIntakePolicy]]
- [[RawKnowledgeMaterialTemplate]]
- [[EffectiveKnowledgeTemplate]]
- [[KnowledgeIntake]]

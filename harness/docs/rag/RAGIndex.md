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
version: v0.6.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-02 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的 RAG 知识库文档、知识引入规则、知识库构建流程和候选区。
scope: HarnessVault RAG。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[KnowledgeIntake]]"
  - "[[KnowledgeIntakeTemplate]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[EffectiveKnowledgeTemplate]]"
  - "[[RAGStandard]]"
  - "[[RAGDomain]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# RAG Index

## 1. 层级定位

RAG Knowledge Layer 用于保存稳定、经过审查、可检索的知识库内容。

RAG 不保存任务历史，不直接保存一次性 workflow，不替代 Project Facts。

## 2. RAG 治理文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[KnowledgeBasePolicy]] | draft | 定义 RAG 知识库的来源、准入、审查、更新和只读规则 |
| [[KnowledgePromotionPolicy]] | draft | 定义 Workflow / Memory / Skill / RAG / Project Facts 之间的晋升路径 |
| [[KnowledgeIntakePolicy]] | draft | 定义用户知识、外部资料、领域知识和候选知识进入 Harness 的通用引入路径 |
| [[KnowledgeBaseConstructionWorkflow]] | draft | 定义 raw material、semantic enrichment、effective knowledge 和 promotion 的构建流程 |

## 3. 当前知识库分区

| 分区 | 状态 | 用途 |
|---|---|---|
| [[KnowledgeIntake]] | draft | 未审查知识候选暂存区，不是事实源 |
| [[RAGStandard]] | draft | 通用规范知识分区，当前不保存真实规范知识正文 |
| [[RAGDomain]] | draft | 领域知识分区，当前不保存真实领域知识正文 |

## 4. Intake 与知识构建模板

| 文档 | 状态 | 用途 |
|---|---|---|
| [[KnowledgeIntake]] | draft | 知识暂存区规则 |
| [[KnowledgeIntakeTemplate]] | draft | 知识引入候选模板 |
| [[RawKnowledgeMaterialTemplate]] | draft | 原始资料层候选模板 |
| [[EffectiveKnowledgeTemplate]] | draft | 审查后的有效知识文档模板 |

## 5. RAG 准入原则

RAG 文档必须满足：

1. 来源明确；
2. 内容稳定；
3. 与具体任务过程解耦；
4. 已通过人工审查；
5. 不与 Project Facts 冲突；
6. 有 reviewAfter。

## 6. 不应进入 RAG 的内容

1. 一次性任务日志；
2. 临时调试结论；
3. 未验证的外部资料摘要；
4. 项目正式事实；
5. 用户个人偏好；
6. 可执行操作流程。

## 7. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[INDEX]]
- [[KnowledgeBasePolicy]]
- [[KnowledgePromotionPolicy]]
- [[KnowledgeIntakePolicy]]
- [[KnowledgeBaseConstructionWorkflow]]
- [[KnowledgeIntake]]
- [[KnowledgeIntakeTemplate]]
- [[RawKnowledgeMaterialTemplate]]
- [[EffectiveKnowledgeTemplate]]
- [[RAGStandard]]
- [[RAGDomain]]

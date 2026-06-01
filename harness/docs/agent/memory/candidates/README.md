---
documentName: docs/agent/memory/candidates/README.md
title: Candidate Memory README
aliases:
  - CandidateMemory
  - Candidate Memory README
  - 候选 Memory
tags:
  - harness
  - memory
  - candidate
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: memory
purpose: 定义 candidate Memory 分区规则；本文件不保存任何真实用户知识或项目知识。
scope: HarnessVault memory。
prerequisites:
  - docs/agent/MemoryPolicy.md
relatedDocuments:
  - "[[MemoryIndex]]"
  - "[[MemoryPolicy]]"
  - "[[KnowledgePromotionPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Candidate Memory README

## 1. 定位

`candidates/` 用于保存尚未审查批准的 Memory 候选。

Candidate Memory 不是事实源，默认不进入智能体上下文。

## 2. 候选字段

候选 Memory 应记录：

| 字段 | 含义 |
|---|---|
| candidateId | 候选编号 |
| source | 来源任务、workflow 或 report |
| content | 候选内容摘要 |
| evidence | 证据摘要 |
| proposedType | User / Project / Agent Operation |
| risk | 潜在风险 |
| reviewStatus | pending / approved / rejected |

## 3. 晋升规则

候选进入 active 前必须：

1. 审查来源；
2. 检查是否重复；
3. 检查是否应进入 RAG / Skill / Project Facts；
4. 检查敏感信息；
5. 由 human owner 批准。

## 4. 禁止事项

1. 禁止把 candidate 当作事实源。
2. 禁止未经审查写入 active。
3. 禁止保存大段日志或代码。
4. 禁止保存用户知识或具体项目内容到通用 HarnessVault。

## 5. 关联文档

- [[MemoryIndex]]
- [[MemoryPolicy]]
- [[KnowledgePromotionPolicy]]

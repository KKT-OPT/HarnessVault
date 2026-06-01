---
documentName: docs/agent/memory/MemoryIndex.md
title: Memory Index
aliases:
  - MemoryIndex
tags:
  - harness
  - memory
  - index
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 中的 Memory 分区和维护规则。
scope: HarnessVault memory。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[MemoryPolicy]]"
  - "[[MemoryGovernance]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Memory Index

## 1. 定位

Memory 是小而稳定、对未来任务有明确复用价值的信息。HarnessVault 当前阶段只提供通用 Memory 分区骨架，不写入用户知识、不写入具体项目内容、不创建真实 active Memory。

## 2. Memory 分区

| 分区 | 状态 | 用途 |
|---|---|---|
| `docs/agent/memory/active/` | draft | 已批准的长期 Memory 存放区 |
| `docs/agent/memory/candidates/` | draft | 候选 Memory 存放区，未批准前不得作为事实源 |
| `docs/agent/memory/archive/` | draft | 已归档 Memory 存放区，默认不加载 |

## 3. 当前规则

1. active Memory 必须经过审查。
2. candidate Memory 不得作为事实源。
3. archived Memory 默认不进入上下文。
4. 通用 HarnessVault 不保存用户个人知识或具体项目 Memory。
5. 真实项目 Memory 应进入 Project Harness Instance。

## 4. 关联文档

- [[MemoryPolicy]]
- [[MemoryGovernance]]
- [[KnowledgePromotionPolicy]]
- [[ArtifactLifecycle]]

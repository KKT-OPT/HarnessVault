---
documentName: docs/agent/memory/archive/README.md
title: Archived Memory README
aliases:
  - ArchivedMemory
  - Archived Memory README
  - 归档 Memory
tags:
  - harness
  - memory
  - archive
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: memory
purpose: 定义 archived Memory 分区规则；本文件不保存任何真实用户知识或项目知识。
scope: HarnessVault memory。
prerequisites:
  - docs/agent/MemoryPolicy.md
relatedDocuments:
  - "[[MemoryIndex]]"
  - "[[MemoryPolicy]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Archived Memory README

## 1. 定位

`archive/` 用于保存已经失效、被替代或不再默认加载的 Memory。

Archived Memory 是历史证据，不是默认上下文，也不是当前事实源。

## 2. 归档条件

Memory 应归档，当：

1. 已被正式文档替代；
2. 已过期；
3. 与当前事实冲突；
4. 长期未使用；
5. 粒度过细；
6. 不再符合 [[MemoryPolicy]]。

## 3. 归档要求

归档时必须记录：

1. 原 Memory id；
2. 归档原因；
3. 替代文档，若有；
4. 归档日期；
5. 审批人或治理报告来源。

## 4. 禁止事项

1. 禁止默认加载 archived Memory。
2. 禁止直接删除仍有追溯价值的 Memory。
3. 禁止把 archived Memory 作为当前事实引用。

## 5. 关联文档

- [[MemoryIndex]]
- [[MemoryPolicy]]
- [[CleanupPolicy]]

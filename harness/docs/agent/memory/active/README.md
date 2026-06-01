---
documentName: docs/agent/memory/active/README.md
title: Active Memory README
aliases:
  - ActiveMemory
  - Active Memory README
  - 已批准 Memory
tags:
  - harness
  - memory
  - active
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: memory
purpose: 定义 active Memory 分区规则；本文件不保存任何真实用户知识或项目知识。
scope: HarnessVault memory。
prerequisites:
  - docs/agent/MemoryPolicy.md
relatedDocuments:
  - "[[MemoryIndex]]"
  - "[[MemoryPolicy]]"
  - "[[MemoryGovernance]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Active Memory README

## 1. 定位

`active/` 用于保存已经审查批准、对未来任务有明确复用价值的长期 Memory。

当前通用 HarnessVault 不保存真实 active Memory。本目录只提供规则和占位结构。

## 2. 准入条件

active Memory 必须满足：

1. 内容稳定；
2. 有明确来源；
3. 已通过 human owner 或治理流程审查；
4. 不包含敏感信息；
5. 不重复 Project Facts、RAG 或 Skill；
6. 已记录 reviewAfter。

## 3. 禁止事项

1. 禁止写入用户个人知识。
2. 禁止写入具体项目内容。
3. 禁止写入日志、代码、临时任务状态。
4. 禁止未经审查从 candidate 直接移动到 active。

## 4. 关联文档

- [[MemoryIndex]]
- [[MemoryPolicy]]
- [[MemoryGovernance]]

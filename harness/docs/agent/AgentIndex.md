---
documentName: docs/agent/AgentIndex.md
title: Agent Index
aliases:
  - AgentIndex
  - Agent 文档索引
  - 智能体索引
tags:
  - harness
  - agent
  - index
version: v0.1.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-30 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 Harness Agent Capability Layer 的智能体能力、上下文、Prompt、Skill 和 Memory 文档。
scope: HarnessVault agent layer。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Agent Index

## 1. 层级定位

Agent Capability Layer 定义任意智能体进入 HarnessVault 后如何加载上下文、制定 Prompt、使用 Skill、读取或更新 Memory。

## 2. Agent Policy 文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[ContextLoadingPolicy]] | draft | 定义智能体在不同任务类型下加载 Harness 上下文的规则 |
| [[PromptPolicy]] | draft | 定义 Harness 任务 Prompt 的结构、约束和输出格式 |
| [[SkillPolicy]] | draft | 定义 Skill 作为程序性记忆的使用、创建和更新规则 |
| [[MemoryPolicy]] | draft | 定义 Memory 的读取、写入、候选生成和污染控制规则 |

## 3. Skill / Memory 索引

| 文档 | 状态 | 用途 |
|---|---|---|
| [[SkillIndex]] | draft | 索引 HarnessVault 中的 Skill 文档 |
| [[MemoryIndex]] | draft | 索引 HarnessVault 中的 Memory 文档 |

## 4. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[SkillGovernance]]
- [[MemoryGovernance]]
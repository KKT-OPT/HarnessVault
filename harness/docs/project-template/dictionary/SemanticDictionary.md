---
documentName: docs/project-template/dictionary/SemanticDictionary.md
title: Semantic Dictionary Template
aliases:
  - SemanticDictionary
  - 语义字典模板
  - 项目语义字典
tags:
  - harness
  - project-template
  - dictionary
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的术语、命名、字段和概念归一模板。
scope: Project Template dictionary。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[Repository]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Semantic Dictionary Template

## 1. 目的

本文档用于在真实项目中统一术语、命名、字段含义、模块名、状态名和流程名，避免人类和智能体在长期开发中产生语义漂移。

## 2. 使用规则

1. 项目核心术语必须在本文档中定义。
2. 新增模块、字段、状态和流程前，应先检查本文档。
3. 同义词应归一到唯一推荐术语。
4. 禁用术语应明确说明替代写法。
5. 术语变化应同步更新架构文档和相关代码说明。

## 3. 核心术语

| 术语 | 推荐英文名 | 定义 | 禁用别名 | 关联文档 |
|---|---|---|---|---|
| `<term>` | `<english-name>` | `<definition>` | `<forbidden-alias>` | `<doc-link>` |

## 4. 模块命名

| 模块 | 推荐名称 | 职责 | 禁用名称 | 关联架构层 |
|---|---|---|---|---|
| `<module>` | `<recommended-name>` | `<responsibility>` | `<forbidden-name>` | `<layer>` |

## 5. 字段语义

| 字段 | 所属对象 | 类型 | 含义 | 约束 |
|---|---|---|---|---|
| `<field>` | `<object>` | `<type>` | `<meaning>` | `<constraint>` |

## 6. 状态枚举

| 状态 | 含义 | 触发条件 | 后续状态 |
|---|---|---|---|
| `<state>` | `<meaning>` | `<trigger>` | `<next-state>` |

## 7. 流程命名

| 流程 | 推荐名称 | 起点 | 终点 | 说明 |
|---|---|---|---|---|
| `<process>` | `<recommended-name>` | `<start>` | `<end>` | `<description>` |

## 8. 同义词归一

| 非推荐写法 | 推荐写法 | 原因 |
|---|---|---|
| `<alias>` | `<recommended-term>` | `<reason>` |

## 9. 禁用术语

| 禁用术语 | 替代术语 | 禁用原因 |
|---|---|---|
| `<forbidden-term>` | `<replacement>` | `<reason>` |

## 10. 智能体使用规则

智能体在生成代码、文档、测试、架构说明时必须：

1. 优先使用本文档中的推荐术语；
2. 避免引入未定义同义词；
3. 遇到新概念时先提出候选术语；
4. 不得静默替换已有术语语义；
5. 涉及架构术语时同步检查 [[ARCHITECTURE]]。

## 11. 待确认术语

| 候选术语 | 来源 | 待确认问题 |
|---|---|---|
| `<candidate>` | `<source>` | `<question>` |

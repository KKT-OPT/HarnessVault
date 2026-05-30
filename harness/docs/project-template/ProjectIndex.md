---
documentName: docs/project-template/ProjectIndex.md
title: Project Template Index
aliases:
  - ProjectIndex
  - Project Template Index
  - 项目模板索引
tags:
  - harness
  - project-template
  - index
version: v0.3.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 Project Harness Instance 模板文档。
scope: HarnessVault project template。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[README]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
  - "[[Repository]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Project Template Index

## 1. 层级定位

Project Template Layer 用于定义通用 Harness Template 在真实项目中实例化后的项目文档结构。

通用 Harness 仓库中使用：

```text
docs/project-template/
```

真实项目实例中使用：

```text
docs/project/
```

P3 阶段只提供最小实例化能力，不填入任何具体项目事实。

## 2. P3 最小模板文档

| 模板文档 | 状态 | 用途 |
|---|---|---|
| [[README]] | draft | 说明如何从通用 Project Template 实例化为真实项目的 `docs/project/` |
| [[ARCHITECTURE]] | draft | 项目架构事实源模板 |
| [[SemanticDictionary]] | draft | 术语、命名、字段和概念归一模板 |
| [[Repository]] | draft | 仓库、分支、构建、测试和提交边界模板 |
| [[WorkflowTemplate]] | draft | 真实项目任务过程、验收和 promotion candidates 记录模板 |

## 3. 项目模板分区

| 分区 | 状态 | 用途 |
|---|---|---|
| `docs/project-template/prd/` | planned | 项目需求文档模板 |
| `docs/project-template/architecture/` | draft | 项目架构文档模板 |
| `docs/project-template/dictionary/` | draft | 语义字典、术语字典模板 |
| `docs/project-template/git/` | draft | 仓库、分支、提交、PR 规则模板 |
| `docs/project-template/api/` | planned | 接口文档模板 |
| `docs/project-template/data/` | planned | 数据结构、数据源、数据约束模板 |
| `docs/project-template/test/` | planned | 测试策略、测试报告、验收标准模板 |
| `docs/project-template/workflow/` | draft | 项目真实任务 workflow 记录模板 |
| `docs/project-template/decision/` | planned | ADR 架构决策记录模板 |

## 4. 实例化规则

将 Project Template 复制到真实项目时：

1. 将 `docs/project-template/` 复制或映射为 `docs/project/`；
2. 替换所有 `<project-name>`、`<repository-url>`、`<main-branch>` 等占位变量；
3. 删除不适用于该项目的 planned 分区，或保留为 planned；
4. 更新真实项目的 `docs/INDEX.md`；
5. 更新真实项目的 `AGENTS.md`；
6. 创建第一条项目 workflow。

## 5. 禁止事项

Project Template 中不得写入：

1. 具体项目需求；
2. 具体业务架构；
3. 真实仓库 URL；
4. 真实分支名称；
5. 真实构建命令；
6. 真实任务历史；
7. 项目级 Memory 或 Skill。

## 6. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[GovernanceIndex]]
- [[ContextLoadingPolicy]]

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
version: v0.5.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 Project Harness Instance 模板说明文档，并指向 templates 统一模板源。
scope: HarnessVault project template。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[ProjectTemplateREADME]]"
  - "[[TemplatesIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
  - "[[Repository]]"
  - "[[ADR-0001-template]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
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

Project Template 目录只提供结构说明、字段说明、分区规则和实例化规则，不保存任何具体项目事实。

可复制模板、Templater 模板、workflow 模板和后续 prompt 模板统一放在：

```text
templates/
```

## 2. P3 最小模板说明文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[ProjectTemplateREADME]] | draft | 说明如何从通用 Project Template 实例化为真实项目的 `docs/project/` |
| [[ARCHITECTURE]] | draft | 项目架构事实源说明模板 |
| [[SemanticDictionary]] | draft | 术语、命名、字段和概念归一说明模板 |
| [[Repository]] | draft | 仓库、分支、构建、测试和提交边界说明模板 |
| `docs/project-template/workflow/README.md` | draft | 项目 workflow 分区说明，实际 workflow 模板见 `templates/WorkflowTemplate.md` |

## 3. P4 扩展分区占位

| 文档 | 状态 | 用途 |
|---|---|---|
| `docs/project-template/prd/README.md` | draft | 项目需求文档分区说明 |
| `docs/project-template/api/README.md` | draft | API 文档分区说明 |
| `docs/project-template/data/README.md` | draft | 数据文档分区说明 |
| `docs/project-template/test/README.md` | draft | 测试文档分区说明 |
| [[ADR-0001-template]] | draft | ADR 架构决策记录模板说明 |

## 4. 项目模板分区

| 分区 | 状态 | 用途 |
|---|---|---|
| `docs/project-template/prd/` | draft | 项目需求文档说明 |
| `docs/project-template/architecture/` | draft | 项目架构文档说明 |
| `docs/project-template/dictionary/` | draft | 语义字典、术语字典说明 |
| `docs/project-template/git/` | draft | 仓库、分支、提交、PR 规则说明 |
| `docs/project-template/api/` | draft | 接口文档说明 |
| `docs/project-template/data/` | draft | 数据结构、数据源、数据约束说明 |
| `docs/project-template/test/` | draft | 测试策略、测试报告、验收标准说明 |
| `docs/project-template/workflow/` | draft | 项目真实任务 workflow 分区说明 |
| `docs/project-template/decision/` | draft | ADR 架构决策记录说明 |

## 5. 实例化规则

将 Project Template 复制到真实项目时：

1. 将 `docs/project-template/` 复制或映射为 `docs/project/` 的说明结构；
2. 从 `templates/**` 获取需要生成的具体文档模板；
3. 替换所有 `<project-name>`、`<repository-url>`、`<main-branch>` 等占位变量；
4. 删除不适用于该项目的 planned 分区，或保留为 planned；
5. 更新真实项目的 `docs/INDEX.md`；
6. 更新真实项目的 `AGENTS.md`；
7. 使用 `templates/WorkflowTemplate.md` 创建第一条项目 workflow。

## 6. 禁止事项

Project Template 中不得写入：

1. 具体项目需求；
2. 具体业务架构；
3. 真实仓库 URL；
4. 真实分支名称；
5. 真实构建命令；
6. 真实任务历史；
7. 项目级 Memory 或 Skill；
8. 与 `templates/**` 重复的可复制模板正文。

## 7. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[GovernanceIndex]]
- [[ContextLoadingPolicy]]
- [[KnowledgeBasePolicy]]
- [[TemplatesIndex]]

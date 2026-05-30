---
documentName: docs/project-template/README.md
title: Project Template README
aliases:
  - ProjectTemplateREADME
  - Project Template README
  - 项目模板说明
tags:
  - harness
  - project-template
  - readme
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 说明如何从通用 Project Template 实例化为真实项目的 docs/project/。
scope: HarnessVault project template。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
  - "[[Repository]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Project Template README

## 1. 目的

本文档说明如何将通用 Harness Project Template 实例化为真实项目的 `docs/project/` 文档系统。

Project Template 只提供结构、字段、检查项和占位变量，不保存任何具体项目事实。

## 2. 实例化目标

通用模板路径：

```text
docs/project-template/
```

真实项目路径：

```text
docs/project/
```

实例化后，真实项目应形成：

```text
docs/project/
├── ProjectIndex.md
├── prd/
├── architecture/
│   └── ARCHITECTURE.md
├── dictionary/
│   └── SemanticDictionary.md
├── git/
│   └── Repository.md
├── api/
├── data/
├── test/
├── workflow/
│   └── WorkflowTemplate.md
└── decision/
```

## 3. 最小实例化文件

P3 阶段定义以下最小模板：

| 模板 | 实例化后用途 |
|---|---|
| [[ARCHITECTURE]] | 项目架构事实源 |
| [[SemanticDictionary]] | 术语、命名、字段和概念归一 |
| [[Repository]] | 仓库、分支、构建、测试和提交边界 |
| [[WorkflowTemplate]] | 真实项目任务 workflow 记录模板 |

## 4. 占位变量

实例化时应替换：

```text
<project-name>
<project-code-name>
<repository-url>
<main-branch>
<development-branch>
<build-command>
<test-command>
<run-command>
<owner>
<review-after>
```

## 5. 实例化步骤

1. 复制 `docs/project-template/` 为目标项目的 `docs/project/`。
2. 将 `ProjectIndex.md` 作为目标项目的项目文档索引。
3. 替换所有占位变量。
4. 根据目标项目删除不适用的 planned 分区，或保留为 planned。
5. 更新目标项目 `docs/INDEX.md`，加入 `docs/project/ProjectIndex.md`。
6. 更新目标项目 `AGENTS.md`，加入项目事实文档读取规则。
7. 创建第一条项目 workflow。
8. 检查 Obsidian wikilink 和 frontmatter。

## 6. 禁止事项

本模板中不得写入：

1. 真实项目需求；
2. 真实仓库地址；
3. 真实分支名称；
4. 真实构建命令；
5. 真实接口、数据表或代码路径；
6. 真实任务历史；
7. 项目级 Skill 或 Memory。

## 7. 关联文档

- [[HarnessEngineering]]
- [[ProjectIndex]]
- [[ARCHITECTURE]]
- [[SemanticDictionary]]
- [[Repository]]
- [[WorkflowTemplate]]

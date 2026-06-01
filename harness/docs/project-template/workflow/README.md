---
documentName: docs/project-template/workflow/README.md
title: Project Workflow Section README
aliases:
  - ProjectWorkflowSection
  - Project Workflow Section
  - 项目工作流分区说明
tags:
  - harness
  - project-template
  - workflow
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 project-template/workflow 分区规则，并指向 templates/WorkflowTemplate.md 作为唯一 workflow 模板源。
scope: HarnessVault project template workflow section。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[TemplatesIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Project Workflow Section README

## 1. 定位

`docs/project-template/workflow/` 只说明真实项目 workflow 分区的用途和规则。

可复制 workflow 模板统一存放在：

```text
templates/WorkflowTemplate.md
```

本目录不再保存重复的 workflow 模板正文。

## 2. 实例化规则

真实项目实例中，workflow 应存放在：

```text
docs/project/workflow/
```

创建真实任务 workflow 时，应从 `templates/WorkflowTemplate.md` 生成新文档，再根据项目事实替换占位变量。

## 3. 禁止事项

1. 禁止在本目录保存与 `templates/WorkflowTemplate.md` 重复的模板正文。
2. 禁止在通用 HarnessVault 中写入真实项目 workflow。
3. 禁止把 workflow 过程直接写入 RAG、Skill 或 Memory。

## 4. 关联文档

- [[ProjectIndex]]
- [[TemplatesIndex]]
- [[INDEX]]

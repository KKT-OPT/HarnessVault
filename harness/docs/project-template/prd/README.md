---
documentName: docs/project-template/prd/README.md
title: PRD Template README
aliases:
  - PRDTemplate
  - PRD README
  - 需求文档模板
tags:
  - harness
  - project-template
  - prd
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的需求文档分区占位和维护规则。
scope: Project Template PRD。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# PRD Template README

## 1. 定位

`prd/` 用于保存真实项目的需求文档、目标、范围、用户场景、验收标准和需求变更记录。

本文件是通用模板占位，不包含任何具体项目需求。

## 2. 建议内容

真实项目实例中可包含：

1. `ProductRequirement.md`
2. `UserScenarios.md`
3. `AcceptanceCriteria.md`
4. `RequirementChangeLog.md`

## 3. 写入规则

1. 需求必须有来源。
2. 需求必须有验收标准。
3. 需求变更必须更新相关架构、测试和 workflow。
4. 未确认需求应标记为 candidate 或 draft。

## 4. 关联文档

- [[ProjectIndex]]
- [[ARCHITECTURE]]
- [[WorkflowTemplate]]

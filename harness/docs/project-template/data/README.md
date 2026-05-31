---
documentName: docs/project-template/data/README.md
title: Data Template README
aliases:
  - DataTemplate
  - Data README
  - 数据文档模板
tags:
  - harness
  - project-template
  - data
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的数据文档分区占位和维护规则。
scope: Project Template data。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Data Template README

## 1. 定位

`data/` 用于保存真实项目的数据模型、数据源、字段约束、数据流、数据质量规则和数据变更记录。

本文件是通用模板占位，不包含任何具体数据结构。

## 2. 建议内容

真实项目实例中可包含：

1. `DataModel.md`
2. `DataSource.md`
3. `DataFlow.md`
4. `DataQuality.md`
5. `DataChangeLog.md`

## 3. 写入规则

1. 字段名称必须与 [[SemanticDictionary]] 对齐。
2. 数据事实变化必须同步更新架构和接口文档。
3. 数据源必须说明来源、刷新频率和可信边界。
4. 临时样例数据不应作为长期事实源。

## 4. 关联文档

- [[ProjectIndex]]
- [[ARCHITECTURE]]
- [[SemanticDictionary]]

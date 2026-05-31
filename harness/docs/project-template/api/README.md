---
documentName: docs/project-template/api/README.md
title: API Template README
aliases:
  - APITemplate
  - API README
  - 接口文档模板
tags:
  - harness
  - project-template
  - api
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的接口文档分区占位和维护规则。
scope: Project Template API。
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

# API Template README

## 1. 定位

`api/` 用于保存真实项目的接口定义、请求响应结构、错误码、鉴权、兼容性和接口变更记录。

本文件是通用模板占位，不包含任何具体接口。

## 2. 建议内容

真实项目实例中可包含：

1. `ApiOverview.md`
2. `EndpointReference.md`
3. `ErrorCode.md`
4. `ApiChangeLog.md`

## 3. 写入规则

1. 接口字段必须与 [[SemanticDictionary]] 对齐。
2. 接口变更必须同步更新测试和调用方文档。
3. 未稳定接口应标记为 draft。
4. 废弃接口应标记 deprecated，不直接删除。

## 4. 关联文档

- [[ProjectIndex]]
- [[ARCHITECTURE]]
- [[SemanticDictionary]]

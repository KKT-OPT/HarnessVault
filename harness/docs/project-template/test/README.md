---
documentName: docs/project-template/test/README.md
title: Test Template README
aliases:
  - TestTemplate
  - Test README
  - 测试文档模板
tags:
  - harness
  - project-template
  - test
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的测试文档分区占位和维护规则。
scope: Project Template test。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[Repository]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Test Template README

## 1. 定位

`test/` 用于保存真实项目的测试策略、测试命名、测试数据、测试报告、验收标准和质量门禁。

本文件是通用模板占位，不包含任何具体测试用例。

## 2. 建议内容

真实项目实例中可包含：

1. `TestStrategy.md`
2. `TestNaming.md`
3. `TestData.md`
4. `AcceptanceCriteria.md`
5. `TestReport.md`

## 3. 写入规则

1. 测试策略必须与 [[Repository]] 中的测试命令一致。
2. 验收标准必须能被人工或工具检查。
3. 失败测试应写入 workflow 或 report，不直接写入 Memory。
4. 测试结果报告不是项目事实源，除非结论被写入正式文档。

## 4. 关联文档

- [[ProjectIndex]]
- [[Repository]]
- [[WorkflowTemplate]]

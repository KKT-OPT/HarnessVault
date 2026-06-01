---
documentName: docs/reports/index/README.md
title: Index Reports
aliases:
  - IndexReports
  - Index Reports README
  - 索引检查报告
tags:
  - harness
  - reports
  - index
version: v0.4.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 记录 HarnessVault 索引完整性、链接完整性、orphan 文档和路径一致性检查报告。
scope: HarnessVault index reports。
prerequisites:
  - docs/reports/README.md
  - docs/governance/IndexMaintenancePolicy.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[IndexMaintenancePolicy]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
  - "[[IndexCheckReportTemplate]]"
  - "[[HarnessIndexDryRunReport]]"
  - "[[FrontmatterPathDryRunReport]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Index Reports

## 1. 定位

本目录用于保存 HarnessVault 索引治理相关报告，包括：

1. 顶层 [[INDEX]] 检查报告；
2. 各层 index 检查报告；
3. broken link 检查报告；
4. orphan document 检查报告；
5. frontmatter `documentName` 与实际路径一致性检查报告。

## 2. 当前模板与报告

| 文档 | 用途 |
|---|---|
| [[IndexCheckReportTemplate]] | 索引完整性、broken link、orphan 文档、frontmatter 路径一致性检查模板 |
| [[HarnessIndexDryRunReport]] | HarnessVault index dry-run 检查报告 |
| [[FrontmatterPathDryRunReport]] | Frontmatter documentName 与实际路径一致性 dry-run 报告 |

## 3. 命名建议

```text
YYYYMMDD-index-check.md
YYYYMMDD-broken-links.md
YYYYMMDD-orphan-documents.md
YYYYMMDD-path-frontmatter-check.md
```

## 4. 报告规则

1. 索引检查报告只提出问题和修复建议。
2. 自动修复仅限低风险机械问题，并必须保留报告。
3. 涉及文档迁移、归档和删除时必须人工确认。
4. 索引报告关闭后可根据 [[CleanupPolicy]] 归档。
5. dry-run 报告不得自动修改文档。

## 5. 关联文档

- [[HarnessEngineering]]
- [[IndexMaintenancePolicy]]
- [[INDEX]]
- [[GovernanceIndex]]
- [[IndexCheckReportTemplate]]
- [[HarnessIndexDryRunReport]]
- [[FrontmatterPathDryRunReport]]

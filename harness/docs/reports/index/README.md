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
version: v0.7.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 记录 HarnessVault 当前有效的索引完整性、链接完整性、orphan 文档和路径一致性检查报告。
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
  - "[[ReportsArchive]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Index Reports

## 1. 定位

本目录用于保存 HarnessVault 当前有效的索引治理相关报告，包括：

1. 顶层 [[INDEX]] 检查报告；
2. 各层 index 检查报告；
3. broken link 检查报告；
4. orphan document 检查报告；
5. frontmatter `documentName` 与实际路径一致性检查报告；
6. 真实 self-check 输出分类报告；
7. self-check closeout 报告。

已关闭或已归档的阶段性 index / self-check 报告应进入 [[ReportsArchive]]，不应继续作为默认上下文。

## 2. 当前模板

| 文档 | 用途 |
|---|---|
| [[IndexCheckReportTemplate]] | 索引完整性、broken link、orphan 文档、frontmatter 路径一致性检查模板 |

## 3. 命名建议

```text
YYYYMMDD-index-check.md
YYYYMMDD-broken-links.md
YYYYMMDD-orphan-documents.md
YYYYMMDD-path-frontmatter-check.md
YYYYMMDD-real-self-check.md
YYYYMMDD-self-check-closeout.md
```

## 4. 报告规则

1. 索引检查报告只提出问题和修复建议。
2. 自动修复仅限低风险机械问题，并必须保留报告。
3. 涉及文档迁移、归档和删除时必须人工确认。
4. 索引报告关闭后可根据 [[CleanupPolicy]] 归档。
5. dry-run 报告不得自动修改文档。
6. 具体运行数字只应写入报告，不应成为长期架构事实。
7. archived report 不进入默认上下文。

## 5. 关联文档

- [[HarnessEngineering]]
- [[IndexMaintenancePolicy]]
- [[INDEX]]
- [[GovernanceIndex]]
- [[IndexCheckReportTemplate]]
- [[ReportsArchive]]

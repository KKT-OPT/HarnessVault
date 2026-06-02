---
documentName: docs/reports/governance/README.md
title: Governance Reports
aliases:
  - GovernanceReports
  - Governance Reports README
  - 治理报告
tags:
  - harness
  - reports
  - governance
version: v0.5.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 记录 HarnessVault 综合治理报告、生命周期审查报告和 Scheduled Governance dry-run 报告。
scope: HarnessVault governance reports。
prerequisites:
  - docs/reports/README.md
  - docs/governance/ScheduledGovernance.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[ScheduledGovernance]]"
  - "[[ArtifactLifecycle]]"
  - "[[GovernanceIndex]]"
  - "[[GovernanceReportTemplate]]"
  - "[[ExampleDryRunGovernanceReport]]"
  - "[[ReportsArchive]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Governance Reports

## 1. 定位

本目录用于保存 HarnessVault 当前有效的综合治理报告，包括：

1. Scheduled Governance dry-run 报告；
2. 文档生命周期审查报告；
3. frontmatter 完整性检查报告；
4. stale / archived / deprecated 文档审查报告；
5. Workflow promotion candidate 审查报告；
6. 安全治理报告；
7. 清理和归档报告。

已关闭或已归档的阶段性治理报告应进入 [[ReportsArchive]]，不应继续作为默认上下文。

## 2. 当前模板与示例

| 文档 | 用途 |
|---|---|
| [[GovernanceReportTemplate]] | 人工治理报告、生命周期审查、安全检查和清理建议的统一模板 |
| [[ExampleDryRunGovernanceReport]] | 不含真实检查结果的 dry-run governance report 示例结构 |

## 3. 命名建议

```text
YYYYMMDD-governance-report.md
YYYYMMDD-frontmatter-check.md
YYYYMMDD-lifecycle-audit.md
YYYYMMDD-promotion-candidates.md
YYYYMMDD-security-check.md
YYYYMMDD-cleanup-report.md
YYYYMMDD-architecture-assessment.md
```

## 4. 报告规则

1. 报告只记录检查结果和建议，不直接修改正式文档。
2. 报告中的建议需要人工确认后，才能进入正式文档或治理策略。
3. 报告不是事实源，除非结论被审查后写入正式文档。
4. 报告关闭后可根据 [[CleanupPolicy]] 进入 archive。
5. 示例报告不是实际审查结果，不得作为治理事实引用。
6. archived report 不进入默认上下文。

## 5. 关联文档

- [[HarnessEngineering]]
- [[ScheduledGovernance]]
- [[ArtifactLifecycle]]
- [[GovernanceIndex]]
- [[GovernanceReportTemplate]]
- [[ExampleDryRunGovernanceReport]]
- [[ReportsArchive]]

---
documentName: docs/reports/archive/README.md
title: Reports Archive README
aliases:
  - ReportsArchive
  - Reports Archive
  - 报告归档区
tags:
  - harness
  - reports
  - archive
version: v0.2.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 reports archive 分区规则；用于保存 closed / archived 报告。
scope: HarnessVault reports archive。
prerequisites:
  - docs/governance/ReportArchivePolicy.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[ReportArchivePolicy]]"
  - "[[CleanupPolicy]]"
  - "[[ArchivedHarnessArchitectureAssessment]]"
  - "[[ArchivedHarnessIndexDryRunReport]]"
  - "[[ArchivedFrontmatterPathDryRunReport]]"
  - "[[ArchivedRealHarnessSelfCheckReport]]"
  - "[[ArchivedP12SelfCheckCloseoutReport]]"
  - "[[P13ArchiveCloseoutReport]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Reports Archive README

## 1. 定位

`docs/reports/archive/` 用于保存已经关闭或归档的治理报告、dry-run 报告和历史审查记录。

Archive 报告是历史证据，不是当前事实源，不应进入智能体默认上下文。

## 2. 准入条件

进入本目录的报告应满足：

1. 已经审查；
2. 已经关闭或明确需要历史保留；
3. 不再作为当前任务输入；
4. 结论已被正式文档吸收、拒绝或延期；
5. 不包含 secret 或未脱敏日志。

## 3. 当前归档报告

| 归档报告 | 来源 | 归档原因 |
|---|---|---|
| [[ArchivedHarnessArchitectureAssessment]] | `docs/reports/governance/HarnessArchitectureAssessment.md` | P8 架构评估结论已被后续 PLANS、索引和治理策略吸收 |
| [[ArchivedHarnessIndexDryRunReport]] | `docs/reports/index/HarnessIndexDryRunReport.md` | P8 结构性 dry-run 已被真实 self-check 流程替代 |
| [[ArchivedFrontmatterPathDryRunReport]] | `docs/reports/index/FrontmatterPathDryRunReport.md` | P9 设计型 dry-run 已被 P11/P12 真实 self-check 和脚本规则替代 |
| [[ArchivedRealHarnessSelfCheckReport]] | `docs/reports/index/RealHarnessSelfCheckReport.md` | P11 结论已被 P12 README 治理和模板规则吸收 |
| [[ArchivedP12SelfCheckCloseoutReport]] | `docs/reports/index/P12SelfCheckCloseoutReport.md` | P12 结论已被 PLANS 和 self-check 脚本规则吸收 |
| [[P13ArchiveCloseoutReport]] | P13 归档收口 | 记录本轮归档收口结果 |

## 4. 命名建议

```text
YYYYMMDD-archived-<report-name>.md
```

## 5. 禁止事项

1. 禁止把 archive 报告作为默认上下文。
2. 禁止直接删除仍有追溯价值的报告。
3. 禁止把 archive 报告中的旧结论当作当前事实。
4. 禁止从 archived report 反向污染 active policy 或 active index。

## 6. 关联文档

- [[ReportsIndex]]
- [[ReportArchivePolicy]]
- [[CleanupPolicy]]

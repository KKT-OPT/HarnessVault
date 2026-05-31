---
documentName: docs/reports/index/IndexCheckReportTemplate.md
title: Index Check Report Template
aliases:
  - IndexCheckReportTemplate
  - Index Check Report Template
  - 索引检查报告模板
tags:
  - harness
  - reports
  - index
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: report
purpose: 提供 HarnessVault 索引完整性检查报告模板。
scope: HarnessVault index reports。
prerequisites:
  - docs/governance/IndexMaintenancePolicy.md
  - docs/reports/index/README.md
relatedDocuments:
  - "[[IndexMaintenancePolicy]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
  - "[[ReportsIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Index Check Report Template

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `<YYYYMMDD-index-check>` |
| Scope | `<index-scope>` |
| Mode | `dry-run / approved-fix / audit` |
| Owner | `<owner>` |
| Created At | `<created-at>` |
| Status | `draft / reviewed / closed / archived` |

## 2. Indexes Checked

| Index | Checked | Result | Notes |
|---|---|---|---|
| [[INDEX]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |
| [[GovernanceIndex]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |
| [[AgentIndex]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |
| [[RAGIndex]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |
| [[ProjectIndex]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |
| [[ReportsIndex]] | `<yes/no>` | `pass/fail/partial` | `<notes>` |

## 3. Broken Links

| Source | Broken Link | Severity | Suggested Fix |
|---|---|---|---|
| `<source>` | `<link>` | `low/medium/high` | `<fix>` |

## 4. Orphan Documents

| Document | Reason | Suggested Action |
|---|---|---|
| `<document>` | `<reason>` | `<action>` |

## 5. Frontmatter Path Check

| Document | documentName | Actual Path | Result |
|---|---|---|---|
| `<document>` | `<documentName>` | `<actual-path>` | `pass/fail` |

## 6. Missing Index Entries

| Document | Expected Index | Suggested Action |
|---|---|---|
| `<document>` | `<index>` | `<action>` |

## 7. Auto-fix Candidates

| Candidate | Risk | Requires Approval | Notes |
|---|---|---|---|
| `<candidate>` | `<risk>` | `<yes/no>` | `<notes>` |

## 8. Close Criteria

1. Broken links reviewed.
2. Orphan documents reviewed.
3. documentName mismatches reviewed.
4. Missing index entries resolved or deferred.
5. Report status updated.

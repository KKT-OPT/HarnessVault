---
documentName: docs/reports/governance/GovernanceReportTemplate.md
title: Governance Report Template
aliases:
  - GovernanceReportTemplate
  - Governance Report Template
  - 治理报告模板
tags:
  - harness
  - reports
  - governance
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: report
purpose: 提供 HarnessVault 人工治理报告模板。
scope: HarnessVault governance reports。
prerequisites:
  - docs/governance/ScheduledGovernance.md
  - docs/reports/governance/README.md
relatedDocuments:
  - "[[ScheduledGovernance]]"
  - "[[ArtifactLifecycle]]"
  - "[[SecurityGovernance]]"
  - "[[DocumentGovernance]]"
  - "[[CleanupPolicy]]"
  - "[[ReportsIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Governance Report Template

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `<YYYYMMDD-governance-report>` |
| Scope | `<governance-scope>` |
| Mode | `dry-run / approved-fix / audit` |
| Owner | `<owner>` |
| Created At | `<created-at>` |
| Status | `draft / reviewed / closed / archived` |

## 2. Summary

```text
<summary>
```

## 3. Scope Checked

| Area | Included | Notes |
|---|---|---|
| Index | `<yes/no>` | `<notes>` |
| Frontmatter | `<yes/no>` | `<notes>` |
| Lifecycle | `<yes/no>` | `<notes>` |
| Security | `<yes/no>` | `<notes>` |
| Skill | `<yes/no>` | `<notes>` |
| Memory | `<yes/no>` | `<notes>` |
| RAG | `<yes/no>` | `<notes>` |
| Project Template | `<yes/no>` | `<notes>` |

## 4. Findings

| ID | Severity | Finding | Evidence | Suggested Action |
|---|---|---|---|---|
| `<finding-id>` | `low/medium/high` | `<finding>` | `<evidence>` | `<action>` |

## 5. Auto-fix Candidates

| Candidate | Risk | Requires Approval | Notes |
|---|---|---|---|
| `<candidate>` | `<risk>` | `<yes/no>` | `<notes>` |

## 6. Manual Review Required

| Item | Reason | Owner | Status |
|---|---|---|---|
| `<item>` | `<reason>` | `<owner>` | `open/closed` |

## 7. Decisions

| Decision | Approved By | Date | Notes |
|---|---|---|---|
| `<decision>` | `<owner>` | `<date>` | `<notes>` |

## 8. Follow-up Tasks

1. `<task-1>`
2. `<task-2>`
3. `<task-3>`

## 9. Close Criteria

1. Findings reviewed.
2. Approved fixes applied or deferred.
3. Related indexes updated.
4. Follow-up tasks recorded.
5. Report status updated.

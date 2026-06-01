---
documentName: docs/reports/governance/ExampleDryRunGovernanceReport.md
title: Example Dry-run Governance Report
aliases:
  - ExampleDryRunGovernanceReport
  - Dry-run Governance Report Example
  - 治理报告示例
tags:
  - harness
  - reports
  - governance
  - example
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: report
purpose: 提供不含真实检查结果的 dry-run governance report 示例结构。
scope: HarnessVault governance reports。
prerequisites:
  - docs/reports/governance/GovernanceReportTemplate.md
relatedDocuments:
  - "[[GovernanceReportTemplate]]"
  - "[[ScheduledGovernance]]"
  - "[[CleanupPolicy]]"
  - "[[ArtifactLifecycle]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Example Dry-run Governance Report

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `<YYYYMMDD-governance-report>` |
| Scope | `<example-scope>` |
| Mode | `dry-run` |
| Owner | `<owner>` |
| Created At | `<created-at>` |
| Status | `draft` |

## 2. Summary

```text
This is a structural example only. It does not record real governance findings, user knowledge, project facts, or actual repository audit results.
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
| `<finding-id>` | `<low/medium/high>` | `<finding>` | `<evidence>` | `<action>` |

## 5. Auto-fix Candidates

| Candidate | Risk | Requires Approval | Notes |
|---|---|---|---|
| `<candidate>` | `<risk>` | `<yes/no>` | `<notes>` |

## 6. Manual Review Required

| Item | Reason | Owner | Status |
|---|---|---|---|
| `<item>` | `<reason>` | `<owner>` | `<open/closed>` |

## 7. Follow-up Tasks

1. `<task-1>`
2. `<task-2>`
3. `<task-3>`

## 8. Governance Note

This example must not be treated as an actual audit result. A real governance report should be generated only after a defined dry-run scope is approved.

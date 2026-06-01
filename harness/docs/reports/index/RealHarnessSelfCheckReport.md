---
documentName: docs/reports/index/RealHarnessSelfCheckReport.md
title: Real Harness Self-check Report
aliases:
  - RealHarnessSelfCheckReport
  - Real Harness Self-check
  - 真实自检报告
tags:
  - harness
  - reports
  - index
  - self-check
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: report
purpose: 记录用户本地真实 dry-run 输出、问题分类、P11 修复策略和剩余复测要求。
scope: HarnessVault real self-check report。
prerequisites:
  - scripts/README.md
  - docs/reports/index/FrontmatterPathDryRunReport.md
relatedDocuments:
  - "[[IndexReports]]"
  - "[[FrontmatterPathDryRunReport]]"
  - "[[TemplatesIndex]]"
  - "[[ProjectIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Real Harness Self-check Report

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `20260601-real-harness-self-check` |
| Scope | `HarnessVault real dry-run output from user local environment` |
| Mode | `dry-run` |
| Owner | `human` |
| Created At | `2026-06-01 00:00:00.000 +08:00` |
| Status | `draft` |

## 2. User Local Command

```powershell
python harness/scripts/check_harness_docs.py --root harness --format text
```

## 3. User Local Output Summary

```text
Markdown files checked: 76
Findings: 32
No files were modified.
```

## 4. Finding Classification

| Category | Severity | Count / Scope | P11 Decision |
|---|---|---|---|
| Missing frontmatter on entry docs | high | `AGENTS.md`, `README.md` | true positive, fixed by adding frontmatter |
| Bare README wikilink ambiguity | low | `ProjectIndex.md` | true positive, fixed by replacing with explicit alias |
| WorkflowTemplate ambiguity | low | multiple files | true positive, fixed by making `templates/WorkflowTemplate.md` the only reusable workflow template source |
| Template documentName mismatch | medium | `templates/**` | template semantic issue, fixed by adding `templateTarget` and script template-aware rule |
| SkillTemplate missing fields | medium | `templates/SkillTemplate.md` | true positive, fixed by normalizing template frontmatter |
| Duplicate wikilink findings in same file | low | repeated entries | script quality issue, fixed by de-duplicating findings per file |

## 5. P11 Fixes Applied

P11 applies the following fixes:

1. Add frontmatter to `AGENTS.md` and `README.md`.
2. Define `templates/**` as the unique reusable template source.
3. Add `templates/README.md` as [[TemplatesIndex]].
4. Remove duplicate `docs/project-template/workflow/WorkflowTemplate.md` template body.
5. Add `docs/project-template/workflow/README.md` as workflow section guide.
6. Update [[ProjectIndex]] to avoid naked `[[README]]` and duplicate `[[WorkflowTemplate]]` ambiguity.
7. Normalize `templates/**` frontmatter with `documentName` and `templateTarget`.
8. Make `check_harness_docs.py` template-aware.
9. De-duplicate repeated wikilink findings per file.
10. Keep script dry-run only.

## 6. Remaining Review Items

| Item | Reason | Recommended Next Step |
|---|---|---|
| User should rerun check script after P11 merge | PR environment does not execute local script | P12 local rerun |
| Any remaining ambiguous wikilink | May require Obsidian + script verification | P12 report |
| Stage reports lifecycle | Reports are not long-term fact sources | P13 archive closeout |
| Obsidian UI state tracking | `.obsidian/graph.json` already moved out of tracking in P10 but should be verified locally | P14 boundary closeout |

## 7. Close Criteria

1. P11 PR reviewed by user.
2. User reruns dry-run script locally after merge.
3. New output is saved or summarized in a follow-up report.
4. Remaining findings are classified as true positive / false positive / template exception / script capability gap.
5. No user knowledge or concrete project facts are introduced.

---
documentName: docs/reports/index/P12SelfCheckCloseoutReport.md
title: P12 Self-check Closeout Report
aliases:
  - P12SelfCheckCloseoutReport
  - P12 Self-check Closeout
  - P12 自检收口报告
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
purpose: 记录 P12 阶段对 P11 后真实 self-check 剩余 findings 的分类、修复策略和通用化边界。
scope: HarnessVault P12 self-check closeout。
prerequisites:
  - scripts/README.md
  - docs/reports/index/RealHarnessSelfCheckReport.md
relatedDocuments:
  - "[[IndexReports]]"
  - "[[RealHarnessSelfCheckReport]]"
  - "[[TemplatesIndex]]"
  - "[[PLANS]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# P12 Self-check Closeout Report

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `20260601-p12-self-check-closeout` |
| Scope | `P12 closeout of user local self-check findings after P11` |
| Mode | `dry-run follow-up` |
| Owner | `human` |
| Created At | `2026-06-01 00:00:00.000 +08:00` |
| Status | `draft` |

## 2. P12 Input Classification

P12 received a post-P11 local script output with remaining findings in two categories:

| Category | Decision | Reason |
|---|---|---|
| Bare README wikilink ambiguity | true positive | Multiple subdirectories can contain README files; naked README wikilinks are not stable |
| `templates/README.md` treated as template | script rule issue | A template directory can contain both template documents and index documents |

The report does not treat any single run's file count or finding count as long-term Harness architecture fact.

## 3. P12 Fixes Applied

P12 applies the following fixes:

1. Replace remaining naked README wikilink descriptions with plain text.
2. Update `check_harness_docs.py` so `templates/**` can contain `type: index` documents.
3. Require `templateName`, `templateTarget`, `templateEngine`, and `templatePurpose` only when `type: template`.
4. Add a dedicated `WIKI-README-BARE` finding for future naked README wikilinks.
5. Keep root `README.md` as the vault-level README.
6. Avoid large-scale README renaming in this stage to reduce churn and future refactor cost.

## 4. README Governance Decision

P12 adopts the following general rule:

1. Root `README.md` is allowed as the vault-level entry explanation.
2. Subdirectory README files are allowed as section entry explanations.
3. Subdirectory README files should have unique aliases.
4. Markdown should not use naked README wikilinks.
5. To reference a README file, use a unique alias or plain path text.
6. Large-scale README renaming is deferred unless persistent ambiguity remains after alias and lint rules.

This keeps the architecture extensible for future RAG, report, project-template, memory, skill, and prompt-template expansion.

## 5. Expected Post-P12 Rerun

After P12 is merged, the user should rerun:

```powershell
python harness/scripts/check_harness_docs.py --root harness --format text
```

Expected outcome:

1. `templates/README.md` should no longer trigger template-specific missing-field findings.
2. Current naked README wikilink findings should be removed.
3. Any remaining findings should be classified in the next report before additional changes are made.

## 6. Remaining Review Items

| Item | Reason | Recommended Next Step |
|---|---|---|
| Future repeated README ambiguity | May recur as directories are added | Use alias first; rename only if persistent ambiguity remains |
| Report lifecycle | P8-P12 reports are stage evidence, not long-term fact sources | P13 archive closeout |
| Obsidian UI state | Workspace and graph files should not become Harness facts | P14 boundary closeout |

## 7. Close Criteria

1. P12 PR reviewed by user.
2. User reruns the local self-check script after merge.
3. Remaining findings are classified before further edits.
4. No user knowledge or concrete project facts are introduced.

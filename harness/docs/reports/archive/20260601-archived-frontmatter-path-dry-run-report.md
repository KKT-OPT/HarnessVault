---
documentName: docs/reports/archive/20260601-archived-frontmatter-path-dry-run-report.md
title: Archived Frontmatter Path Dry-run Report
aliases:
  - FrontmatterPathDryRunReport
  - ArchivedFrontmatterPathDryRunReport
  - Frontmatter 路径检查报告归档
tags:
  - harness
  - reports
  - archive
  - frontmatter
version: v0.2.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: archived
type: report
purpose: 归档 P9 阶段 frontmatter path dry-run 报告；该报告是历史证据，不是当前事实源。
scope: HarnessVault archived reports。
prerequisites:
  - docs/governance/ReportArchivePolicy.md
relatedDocuments:
  - "[[ReportsArchive]]"
  - "[[ReportArchivePolicy]]"
  - "[[IndexReports]]"
  - "[[HarnessScripts]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
archivedFrom: docs/reports/index/FrontmatterPathDryRunReport.md
archivedReason: P9 设计型 dry-run 已被 P11/P12 真实 self-check 输出和脚本规则泛化替代。
---

# Archived Frontmatter Path Dry-run Report

## 1. Archive Status

This report is archived. It is historical governance evidence and must not be loaded as default context.

## 2. Original Scope

The original report documented the intended frontmatter path consistency check before the script was fully validated by local reruns.

## 3. Absorbed Conclusions

The conclusions have been absorbed by later work:

1. The dry-run script is available under `harness/scripts/check_harness_docs.py`.
2. P11 and P12 refined template-aware and README-aware checking.
3. Future real outputs should be captured in active index reports rather than this design report.

## 4. Archive Rule

Use [[ReportArchivePolicy]] before relying on archived report content. Current script behavior should be checked from `harness/scripts/check_harness_docs.py` and active reports.

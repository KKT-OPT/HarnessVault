---
documentName: docs/reports/security/ObsidianGitBoundaryReport.md
title: Obsidian Git Boundary Report
aliases:
  - ObsidianGitBoundaryReport
  - Obsidian Git Boundary Report
  - Obsidian Git 边界报告
tags:
  - harness
  - reports
  - security
  - obsidian
  - git
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: report
purpose: 记录 P14 Obsidian 与 Git 跟踪边界检查结论。
scope: HarnessVault Obsidian/Git boundary check。
prerequisites:
  - docs/governance/ObsidianGitBoundaryPolicy.md
relatedDocuments:
  - "[[SecurityReports]]"
  - "[[ObsidianGitBoundaryPolicy]]"
  - "[[ObsidianSetup]]"
  - "[[ReportsIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Obsidian Git Boundary Report

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `20260601-obsidian-git-boundary` |
| Scope | `HarnessVault Obsidian and Git tracking boundary` |
| Mode | `boundary check` |
| Owner | `human` |
| Created At | `2026-06-01 00:00:00.000 +08:00` |
| Status | `draft` |

## 2. Check Summary

P14 checks the boundary between Harness facts, Obsidian editing configuration, volatile UI state, plugin runtime code and Git tracking rules.

## 3. Findings

| ID | Result | Finding | Decision |
|---|---|---|---|
| P14-OBS-001 | pass | `.gitignore` ignores workspace, workspace-mobile, workspaces and graph state | Keep ignored |
| P14-OBS-002 | pass | `.gitignore` ignores plugin runtime code such as `main.js`, `styles.css`, helper scripts | Keep ignored |
| P14-OBS-003 | fixed | `ObsidianSetup.md` previously listed `graph.json` as a retainable lightweight config | Align with `.gitignore`; graph is volatile UI state |
| P14-OBS-004 | pass | `templates/**` remains the unique source for reusable templates | Keep policy |
| P14-OBS-005 | pass | Lightweight Obsidian config may be tracked only when intentionally reviewed | Keep optional tracking |

## 4. Boundary Decision

| Asset | Decision |
|---|---|
| `docs/**/*.md` | Harness facts; tracked; can be default context when relevant |
| `templates/**/*.md` | template source; tracked; loaded by task |
| `docs/reports/**/*.md` | governance evidence; tracked selectively; archived reports excluded from default context |
| `.obsidian/workspace*.json` | volatile UI state; ignored; not context |
| `.obsidian/graph.json` | volatile UI state; ignored; not context |
| `.obsidian/plugins/**/main.js` | plugin runtime code; ignored; not context |
| `.obsidian/plugins/**/styles.css` | plugin runtime code; ignored; not context |
| `.obsidian/plugins/**/manifest.json` | lightweight config; may be tracked after review |
| `.obsidian/plugins/**/data.json` | lightweight config; may be tracked after review |

## 5. No Secrets Statement

This report does not include secrets, tokens, passwords, private keys, user knowledge, project facts or external knowledge body.

## 6. Follow-up

P15 should validate whether a simulated agent can start from `AGENTS.md`, enter [[INDEX]], avoid Obsidian runtime artifacts, and complete the Harness interaction simulation.

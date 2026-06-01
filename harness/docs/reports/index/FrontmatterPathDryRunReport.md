---
documentName: docs/reports/index/FrontmatterPathDryRunReport.md
title: Frontmatter Path Dry-run Report
aliases:
  - FrontmatterPathDryRunReport
  - Frontmatter Path Dry-run
  - Frontmatter 路径检查报告
tags:
  - harness
  - reports
  - index
  - frontmatter
  - dry-run
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: report
purpose: 记录 HarnessVault frontmatter documentName 与实际路径一致性的 dry-run 检查范围、限制和发现问题。
scope: HarnessVault frontmatter path dry-run。
prerequisites:
  - docs/reports/index/IndexCheckReportTemplate.md
  - scripts/README.md
relatedDocuments:
  - "[[IndexCheckReportTemplate]]"
  - "[[IndexReports]]"
  - "[[HarnessScripts]]"
  - "[[IndexMaintenancePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Frontmatter Path Dry-run Report

## 1. Report Metadata

| Field | Value |
|---|---|
| Report ID | `20260601-frontmatter-path-dry-run` |
| Scope | `HarnessVault Markdown frontmatter documentName path consistency` |
| Mode | `dry-run` |
| Owner | `human` |
| Created At | `2026-06-01 00:00:00.000 +08:00` |
| Status | `draft` |

## 2. Dry-run Scope

本报告记录 P9 阶段的 frontmatter path consistency 检查设计与初步检查范围。

检查范围：

1. `harness/docs/**/*.md`；
2. `harness/scripts/README.md`；
3. `harness/templates/**/*.md`，如存在；
4. 排除 `.obsidian/plugins/**`；
5. 排除 generated artifact。

## 3. 检查规则

| 检查项 | 规则 |
|---|---|
| frontmatter exists | Markdown 文档必须以 YAML frontmatter 开头 |
| documentName exists | frontmatter 必须包含 `documentName` |
| documentName path | `documentName` 应与相对 `harness/` 的实际路径一致 |
| required fields | 必须包含基础治理字段 |
| wikilink candidate | wikilink 应能在 title / alias / file stem 中找到候选 |

## 4. 初步发现

| ID | Severity | Finding | Evidence | Suggested Action |
|---|---|---|---|---|
| P9-FM-001 | low | P9 已新增 dry-run 脚本，但尚未在受控环境运行并保存完整输出 | `harness/scripts/check_harness_docs.py` | 用户审查后可在本地运行并生成真实输出报告 |
| P9-FM-002 | medium | 当前报告是设计型 dry-run，不是完整自动化检查结果 | 本报告未包含脚本实际 stdout | P10 或后续阶段执行真实脚本输出 |
| P9-FM-003 | medium | `.obsidian/graph.json` 等 UI 状态文件仍可能处于 Git 跟踪状态 | 历史提交显示 graph.json 曾变化 | 后续评估是否从 Git tracking 中移除 |

## 5. Auto-fix Candidates

| Candidate | Risk | Requires Approval | Notes |
|---|---|---|---|
| 修复 documentName 与路径不一致问题 | medium | yes | 必须基于脚本真实输出，不能凭空修改 |
| 补齐缺失 frontmatter 字段 | medium | yes | 需要逐文件确认语义 |
| 处理 ambiguous wikilink alias | medium | yes | 需要 Obsidian / 脚本双重验证 |

## 6. Manual Review Required

| Item | Reason | Owner | Status |
|---|---|---|---|
| 是否允许运行 `check_harness_docs.py` 并提交真实输出报告 | 从设计型 dry-run 进入实际检查 | human | open |
| 是否将 `.obsidian/graph.json` 从 Git 跟踪中移除 | UI 状态文件可能不应作为 Harness 长期资产 | human | open |
| 是否归档 P8 阶段性报告 | 阶段性治理报告不是长期事实源 | human | open |

## 7. Close Criteria

1. P9 PR 经用户审查。
2. 自检脚本保持 dry-run，不自动修改文件。
3. reports 与 RAG 缺失分区 README 已补齐。
4. 是否执行真实脚本输出由用户确认。
5. 是否归档阶段性报告由用户确认。

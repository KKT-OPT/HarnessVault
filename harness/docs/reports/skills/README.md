---
documentName: docs/reports/skills/README.md
title: Skill Reports README
aliases:
  - SkillReports
  - Skill Reports README
  - Skill 报告
tags:
  - harness
  - reports
  - skill
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 Skill 报告分区规则；当前不保存真实 Skill 审查结果。
scope: HarnessVault skill reports。
prerequisites:
  - docs/agent/SkillPolicy.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[SkillPolicy]]"
  - "[[SkillGovernance]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Skill Reports README

## 1. 定位

`docs/reports/skills/` 用于保存 Skill 使用情况、stale、archive、合并候选、污染和创建审查报告。

当前通用 HarnessVault 只建立报告分区规则，不保存真实 Skill 审查结果。

## 2. 报告类型

1. Skill candidate review；
2. Skill usage review；
3. Skill pollution check；
4. Skill merge candidate report；
5. Skill archive report。

## 3. 报告规则

1. 报告是证据，不是事实源。
2. 报告不得直接创建 active Skill。
3. 报告建议必须经人工审查后才能执行。
4. 报告关闭后可按 [[CleanupPolicy]] 归档。

## 4. 关联文档

- [[ReportsIndex]]
- [[SkillPolicy]]
- [[SkillGovernance]]
- [[CleanupPolicy]]

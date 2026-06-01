---
documentName: docs/reports/README.md
title: Reports Index
aliases:
  - ReportsIndex
  - Reports README
  - 治理报告索引
tags:
  - harness
  - reports
  - governance
  - index
version: v0.3.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的治理报告、索引检查报告和后续自动化 dry-run 报告。
scope: HarnessVault reports。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
  - "[[Dashboard]]"
  - "[[GovernanceReportTemplate]]"
  - "[[IndexCheckReportTemplate]]"
  - "[[MemoryReports]]"
  - "[[SkillReports]]"
  - "[[RAGReports]]"
  - "[[SecurityReports]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Reports Index

## 1. 定位

`docs/reports/` 保存 HarnessVault 的治理报告、索引检查报告、安全检查报告、Skill / Memory / RAG 审查报告和后续自动化 dry-run 结果。

报告是治理证据，不是最终事实源。报告中的结论只有经过人工审查并写入正式文档后，才成为 Harness 文档事实的一部分。

## 2. 当前报告分区

| 分区 | 索引 | 用途 |
|---|---|---|
| `docs/reports/governance/` | [[GovernanceReports]] | 综合治理报告、生命周期检查、定期治理 dry-run 报告 |
| `docs/reports/index/` | [[IndexReports]] | 索引完整性、broken link、orphan document 检查报告 |
| `docs/reports/memory/` | [[MemoryReports]] | Memory 候选、污染、过期、重复检查报告 |
| `docs/reports/skills/` | [[SkillReports]] | Skill 使用情况、stale、archive、合并候选报告 |
| `docs/reports/rag/` | [[RAGReports]] | RAG 来源、审查、过期、未审查知识检查报告 |
| `docs/reports/security/` | [[SecurityReports]] | 上下文安全、插件代码、secrets、外部输出风险检查报告 |

## 3. 当前报告模板

| 模板 | 用途 |
|---|---|
| [[GovernanceReportTemplate]] | 人工治理报告模板 |
| [[IndexCheckReportTemplate]] | 索引完整性检查报告模板 |

## 4. 报告规则

1. 报告是证据，不是事实源。
2. 报告建议必须经过人工审查后才能写入正式文档。
3. 报告中的自动修复候选不得绕过审批。
4. 报告关闭后可保留为 archived。

## 5. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[Dashboard]]
- [[GovernanceReportTemplate]]
- [[IndexCheckReportTemplate]]
- [[MemoryReports]]
- [[SkillReports]]
- [[RAGReports]]
- [[SecurityReports]]

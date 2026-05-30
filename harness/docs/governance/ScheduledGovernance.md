---
documentName: docs/governance/ScheduledGovernance.md
title: Scheduled Governance
aliases:
  - ScheduledGovernance
  - 定期治理
tags:
  - harness
  - governance
  - scheduled-review
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 定期治理、dry-run、报告优先和人工审批机制。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[GovernanceIndex]]"
  - "[[ArtifactLifecycle]]"
  - "[[ReportsIndex]]"
  - "[[GovernanceReports]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Scheduled Governance

## 1. 目的

本文档定义 HarnessVault 的定期治理机制。Scheduled Governance 不是后台自动修改机制，而是周期性检查、生成报告、人工审查、再决定是否应用修改的治理闭环。

## 2. 默认原则

Scheduled Governance 默认遵循：

1. dry-run first；
2. report-first；
3. human approval required；
4. no silent mutation；
5. no automatic deletion；
6. all changes must be reviewable and reversible。

## 3. 治理范围

定期治理检查：

1. frontmatter 完整性；
2. `reviewAfter` 到期文档；
3. stale / deprecated / archived 文档；
4. index 完整性；
5. broken wikilinks；
6. orphan documents；
7. Skill 候选、重复、过期和使用情况；
8. Memory 候选、污染、重复和过期；
9. RAG 来源、审查状态和过期内容；
10. reports 中未处理建议；
11. Obsidian workspace 和插件代码是否误入事实源。

## 4. 治理流程

标准流程：

```text
检查范围确认
→ dry-run 检查
→ 生成治理报告
→ 人工审查
→ 批准可执行项
→ 应用修复
→ 更新报告状态
```

任何跳过报告直接修改长期资产的行为都不符合本规则。

## 5. 报告输出

综合治理报告输出到：

```text
docs/reports/governance/
```

索引相关报告输出到：

```text
docs/reports/index/
```

建议命名：

```text
YYYYMMDD-governance-report.md
YYYYMMDD-frontmatter-check.md
YYYYMMDD-lifecycle-audit.md
YYYYMMDD-index-check.md
YYYYMMDD-broken-links.md
```

## 6. 允许自动修复的低风险项

在人工确认后，可以自动修复：

1. 缺失的 index 链接；
2. 明显错误的 `documentName` 路径；
3. 缺失的基础 frontmatter 字段；
4. 明显过期的 `updatedAt`；
5. 报告 README 中缺失的分区说明；
6. 非语义性的格式问题。

## 7. 禁止自动修复的高风险项

禁止自动执行：

1. 删除文档；
2. 归档长期资产；
3. 将 candidate 晋升为 active；
4. 修改 Skill 或 Memory 的语义内容；
5. 修改 RAG 知识结论；
6. 修改 HarnessEngineering 总设计；
7. 将报告建议直接写入事实源；
8. 修改用户未授权的项目文档。

## 8. 治理频率建议

| 场景 | 建议频率 |
|---|---|
| 架构调整后 | 立即执行一次 dry-run |
| 新增大量文档后 | 立即执行一次 index check |
| 常规维护 | 每月一次 |
| Skill / Memory 大规模变更后 | 立即执行一次污染检查 |
| RAG 更新后 | 立即执行一次来源与审查检查 |

## 9. 审批规则

人工审批必须明确：

1. 允许修改哪些文件；
2. 禁止修改哪些文件；
3. 是否允许生成新报告；
4. 是否允许更新 index；
5. 是否允许修改 frontmatter；
6. 是否允许归档资产。

默认情况下，只允许生成报告和提出建议，不允许直接修改长期资产。

## 10. 完成标准

一次 Scheduled Governance 完成时，必须输出：

1. 检查范围；
2. 发现的问题；
3. 建议修复项；
4. 自动修复候选；
5. 需要人工审批的项；
6. 未处理风险；
7. 后续任务建议。

## 11. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[ArtifactLifecycle]]
- [[ReportsIndex]]
- [[GovernanceReports]]

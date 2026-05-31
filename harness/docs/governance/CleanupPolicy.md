---
documentName: docs/governance/CleanupPolicy.md
title: Cleanup Policy
aliases:
  - CleanupPolicy
  - 清理规则
tags:
  - harness
  - governance
  - cleanup
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 文档资产、Memory、Skill、RAG 和报告产物的清理、归档和删除规则。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/ArtifactLifecycle.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[ArtifactLifecycle]]"
  - "[[DocumentGovernance]]"
  - "[[SecurityGovernance]]"
  - "[[ScheduledGovernance]]"
  - "[[ReportsIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Cleanup Policy

## 1. 目的

本文档定义 HarnessVault 文档资产、Memory、Skill、RAG 和报告产物的清理、归档和删除规则。目标是在保留可追溯性的前提下，控制长期资产膨胀、过期内容、重复内容和上下文污染。

## 2. 清理原则

HarnessVault 清理遵循：

1. archive before delete；
2. report before mutation；
3. human approval before destructive action；
4. no silent deletion；
5. preserve traceability；
6. keep indexes consistent。

## 3. 清理对象

清理对象包括：

1. 过期文档；
2. deprecated 文档；
3. archived 文档；
4. orphan 文档；
5. 重复文档；
6. stale Memory；
7. stale Skill；
8. 未处理 candidate；
9. 过期 report；
10. 误提交的 workspace 或插件运行代码。

## 4. 不允许直接删除的资产

默认不得直接删除：

1. HarnessEngineering；
2. AGENTS；
3. INDEX / PLANS；
4. governance policy；
5. active Skill；
6. active Memory；
7. active RAG；
8. Project Facts；
9. ADR；
10. 已被引用的 report。

这些资产应先进入 review、stale、deprecated 或 archived 状态。

## 5. 允许直接清理的内容

在确认不需要保留后，可清理：

1. 空的插件运行文件；
2. Obsidian workspace 状态；
3. IDE 本地状态；
4. 临时文件；
5. 明确重复的 generated 文件；
6. 未被索引引用的临时草稿。

即使是低风险清理，也应在报告或 PR 中说明。

## 6. 归档规则

归档适用于：

1. 被替代但仍有历史价值的文档；
2. 不再推荐但仍需追溯的 Skill；
3. 已被正式文档吸收的 report；
4. 已完成但仍需保留的 workflow；
5. 过期但可作为历史参考的 RAG 文档。

归档时必须：

1. 设置 `status: archived`；
2. 从默认推荐索引中移除；
3. 在对应 index 的 archive 分区保留链接；
4. 记录归档原因；
5. 必要时生成 cleanup report。

## 7. 删除规则

删除必须满足：

1. 已无事实价值；
2. 无有效入链；
3. 不属于长期资产；
4. 有报告记录；
5. human owner 批准；
6. PR 中明确列出删除文件。

禁止自动删除任何长期资产。

## 8. 清理检查项

执行清理前检查：

1. 文件是否被 index 引用；
2. 文件是否被 relatedDocuments 引用；
3. 文件是否是事实源；
4. 文件是否只是 report 或 generated artifact；
5. 文件是否包含敏感信息；
6. 是否应 archive 而不是 delete；
7. 是否需要更新 Dashboard 或 reports README。

## 9. 报告输出

清理报告输出到：

```text
docs/reports/governance/
```

建议命名：

```text
YYYYMMDD-cleanup-report.md
YYYYMMDD-archive-report.md
YYYYMMDD-delete-candidates.md
```

## 10. 关联文档

- [[HarnessEngineering]]
- [[ArtifactLifecycle]]
- [[DocumentGovernance]]
- [[SecurityGovernance]]
- [[ScheduledGovernance]]
- [[ReportsIndex]]

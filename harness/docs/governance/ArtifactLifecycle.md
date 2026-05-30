---
documentName: docs/governance/ArtifactLifecycle.md
title: Artifact Lifecycle
aliases:
  - ArtifactLifecycle
  - 文档资产生命周期
tags:
  - harness
  - governance
  - lifecycle
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 文档资产、Skill、Memory、RAG、Workflow 的生命周期状态和迁移规则。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[GovernanceIndex]]"
  - "[[IndexMaintenancePolicy]]"
  - "[[ScheduledGovernance]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Artifact Lifecycle

## 1. 目的

本文档定义 HarnessVault 中长期资产的生命周期状态、状态迁移规则和治理边界。目标是避免文档、Skill、Memory、RAG、Workflow 和 Report 长期堆积、过期、重复或污染智能体上下文。

## 2. 资产范围

Lifecycle 管理以下资产：

1. Markdown 文档；
2. Governance policy；
3. Agent policy；
4. RAG 知识文档；
5. Skill；
6. Memory；
7. Workflow template；
8. Reports；
9. Project template。

以下内容不是 Harness 事实资产：

1. Obsidian workspace 状态；
2. 插件运行代码；
3. generated HTML；
4. Notebook 临时输出；
5. 一次性日志。

## 3. 标准状态

| 状态 | 含义 | 默认可读 | 可作为事实源 |
|---|---|---:|---:|
| draft | 草稿或占位，尚未完全审查 | 是 | 谨慎 |
| active | 当前有效文档 | 是 | 是 |
| review | 正在审查，可能变化 | 是 | 谨慎 |
| stale | 可能过期，待确认 | 否 | 否 |
| deprecated | 已被替代 | 否 | 否 |
| archived | 历史保留 | 否 | 否 |
| candidate | 候选资产，未批准 | 否 | 否 |

## 4. 状态迁移

```text
draft -> active
active -> review
review -> active
review -> stale
stale -> active
stale -> deprecated
deprecated -> archived
candidate -> draft
candidate -> rejected
```

不允许默认自动执行：

```text
active -> deleted
candidate -> active
report -> project fact
workflow -> memory / skill / rag
```

这些迁移必须经过人工确认。

## 5. Draft 规则

占位文档可以保持 `draft`，但必须包含：

1. frontmatter；
2. 明确 `purpose`；
3. 所属层级 index 链接；
4. `reviewAfter`；
5. 正文说明当前状态。

占位文档不得空置，也不得没有索引入口。

## 6. Active 规则

文档进入 `active` 前必须满足：

1. 正文已能指导真实任务；
2. 所属 index 已更新；
3. 与相关文档的链接完整；
4. 不包含未审查的外部资料或临时任务信息；
5. 有明确 owner 和 reviewAfter。

## 7. Stale / Deprecated 规则

当文档满足以下任一条件，应标记 `stale`：

1. 超过 `reviewAfter` 未审查；
2. 与当前 [[PLANS]] 阶段冲突；
3. 与新 policy 冲突；
4. 链接目标大量失效；
5. 依赖的工具或路径已变化。

当文档已被替代但仍有历史价值，应标记 `deprecated`。deprecated 文档不应进入默认上下文。

## 8. Archive 规则

归档前必须：

1. 在对应 index 中移动到 Archive 分区；
2. 在文档 frontmatter 中将 `status` 改为 `archived`；
3. 保留归档原因；
4. 必要时生成报告；
5. 不删除历史引用。

## 9. Reports 生命周期

Reports 是治理证据，不是最终事实源。

Report 状态通常为：

```text
draft -> active -> archived
```

报告中的建议必须经过人工确认并写入正式文档后，才成为 Harness 事实。

## 10. Workflow 候选晋升

Workflow 记录只产生候选：

1. Memory Candidate；
2. Skill Candidate；
3. RAG Candidate；
4. Project Fact Candidate。

候选不得直接成为长期资产，必须经过审查。

## 11. 定期审查

生命周期审查应检查：

1. `reviewAfter` 到期文档；
2. stale / deprecated 文档是否仍被索引默认推荐；
3. candidate 是否长期未处理；
4. archived 文档是否仍被默认上下文加载；
5. report 是否有未处理建议。

## 12. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[IndexMaintenancePolicy]]
- [[ScheduledGovernance]]

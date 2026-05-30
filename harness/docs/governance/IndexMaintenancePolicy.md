---
documentName: docs/governance/IndexMaintenancePolicy.md
title: Index Maintenance Policy
aliases:
  - IndexMaintenancePolicy
  - 索引维护规则
tags:
  - harness
  - governance
  - index
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 索引文档的维护、校验、归档和链接治理规则。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[GovernanceIndex]]"
  - "[[ReportsIndex]]"
  - "[[IndexReports]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Index Maintenance Policy

## 1. 目的

本文档定义 HarnessVault 索引维护规则，用于确保人类和智能体都能通过稳定入口找到正确文档，并避免 orphan 文档、broken link、重复索引和过期文档污染上下文。

## 2. 索引层级

HarnessVault 采用分层索引：

```text
[[INDEX]]
  ├── [[GovernanceIndex]]
  ├── [[AgentIndex]]
  ├── [[RAGIndex]]
  ├── [[ProjectIndex]]
  ├── [[ReportsIndex]]
  ├── [[ObsidianSetup]]
  └── [[Dashboard]]
```

顶层 [[INDEX]] 只链接架构层入口，不直接列出所有子文档。具体文档由对应层级 index 维护。

## 3. 维护职责

| 文档类型 | 必须更新的索引 |
|---|---|
| governance policy | [[GovernanceIndex]] |
| agent policy | [[AgentIndex]] |
| skill | [[SkillIndex]] |
| memory | [[MemoryIndex]] |
| RAG policy / knowledge | [[RAGIndex]] |
| project template | [[ProjectIndex]] |
| governance / index report | [[ReportsIndex]] 或对应 report README |
| Obsidian 使用说明 | [[INDEX]] 与 [[ObsidianSetup]] |

## 4. 新增文档规则

新增 Markdown 文档时，必须完成：

1. 写入 frontmatter；
2. 设置 `documentName`，路径相对 vault root `harness/`；
3. 设置 `title`、`aliases`、`tags`、`version`、`status`、`type`、`purpose`、`scope`、`owner`、`reviewAfter`；
4. 在对应层级 index 中加入链接；
5. 在相关文档的 `relatedDocuments` 中补充必要反向关系；
6. 确认 Obsidian wikilink 可解析。

## 5. 移动或重命名规则

移动或重命名文档时，必须检查：

1. `documentName` 是否同步更新；
2. 所属层级 index 是否同步更新；
3. 其他文档中的 wikilink 是否被 Obsidian 自动更新；
4. `relatedDocuments` 中的路径或链接是否仍然有效；
5. 报告目录中是否需要记录迁移说明。

## 6. 归档规则

当文档不再作为默认上下文使用，但仍有历史价值时，应：

1. 将 `status` 改为 `archived`；
2. 移入对应 archive 目录，或保留原路径并在 index 中标注 archived；
3. 从默认推荐阅读列表中移除；
4. 在对应 index 中保留“归档文档”分区；
5. 必要时在 `docs/reports/index/` 生成归档报告。

## 7. 删除规则

默认不直接删除长期资产。删除前必须满足：

1. 已确认不是事实源；
2. 已确认没有有效入链；
3. 已确认不是历史决策、治理报告、Skill、Memory 或 RAG 来源；
4. 已在治理报告中说明删除原因；
5. 已由 human owner 审批。

## 8. 检查项

索引治理应定期检查：

1. 顶层 [[INDEX]] 是否只链接架构层入口；
2. 各层 index 是否覆盖本层正式文档；
3. 是否存在 orphan document；
4. 是否存在 broken wikilink；
5. 是否存在 frontmatter 缺失；
6. `documentName` 是否与实际路径一致；
7. `status=stale/deprecated/archived` 的文档是否仍被默认推荐；
8. Obsidian workspace、插件代码、生成产物是否被误加入 index。

## 9. 自动修复边界

允许在人工确认后自动修复：

1. index 中缺失的新文档链接；
2. 明显错误的 `updatedAt`；
3. 明显错误的 `documentName` 路径；
4. 缺失的基础 frontmatter 字段；
5. 报告 README 中缺失的报告分区链接。

禁止自动修复：

1. 删除文档；
2. 归档长期资产；
3. 修改 HarnessEngineering 总设计；
4. 修改 Skill 或 Memory 语义内容；
5. 把报告结论直接写入事实源。

## 10. 报告输出

索引检查报告应输出到：

```text
docs/reports/index/
```

建议命名：

```text
YYYYMMDD-index-check.md
YYYYMMDD-broken-links.md
YYYYMMDD-orphan-documents.md
YYYYMMDD-path-frontmatter-check.md
```

## 11. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[GovernanceIndex]]
- [[ReportsIndex]]
- [[IndexReports]]

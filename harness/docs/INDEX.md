---
documentName: docs/INDEX.md
title: Harness 文档索引
aliases:
  - INDEX
  - Harness Index
  - 文档索引
tags:
  - harness
  - index
  - documentation
version: v0.4.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: HarnessVault 顶层文档导航入口，链接各架构层的二级索引。
scope: HarnessVault 通用文档系统。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[PLANS]]"
  - "[[GovernanceIndex]]"
  - "[[AgentIndex]]"
  - "[[RAGIndex]]"
  - "[[ProjectIndex]]"
  - "[[ReportsIndex]]"
  - "[[ObservabilityIndex]]"
  - "[[VerificationIndex]]"
  - "[[Dashboard]]"
  - "[[ObsidianSetup]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness 文档索引

## 1. 必读入口

任何智能体处理 HarnessVault 任务时，应优先读取：

1. [[HarnessEngineering]]：Harness Engineering 总体架构设计。
2. [[PLANS]]：当前阶段计划和后续任务。
3. `AGENTS.md`：vault 内智能体入口契约。

## 2. 架构层索引

| 架构层 | 索引文档 | 用途 |
|---|---|---|
| Governance Runtime Layer | [[GovernanceIndex]] | 生命周期、定期治理、安全治理、清理、晋升、runtime 边界和索引维护 |
| Agent Capability Layer | [[AgentIndex]] | 智能体上下文加载、Prompt、Skill、Memory 等能力说明 |
| Knowledge Layer | [[RAGIndex]] | RAG 知识库入口和知识库治理规则 |
| Project Template Layer | [[ProjectIndex]] | 项目实例化模板入口 |
| Observability Layer | [[ObservabilityIndex]] | 任务 trace、操作事件、失败归因、证据和人工介入记录 |
| Verification Layer | [[VerificationIndex]] | 执行前 readiness、验收、回归验证和修复闭环 |
| Governance Reports Layer | [[ReportsIndex]] | 治理报告、索引检查报告和 dry-run 结果入口 |
| Obsidian Tooling Layer | [[ObsidianSetup]] | Obsidian、Dataview、Templater、Linter 使用说明 |
| Dynamic View Layer | [[Dashboard]] | Dataview 动态视图，不替代正式索引 |

## 3. 核心架构文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[HarnessEngineering]] | draft | Harness 文档系统总体架构、治理机制、目录边界和长期演进规则 |
| [[PLANS]] | draft | 当前阶段目标、验收标准和下一步拆分计划 |

## 4. 索引维护规则

1. 顶层 `INDEX.md` 只链接各架构层入口索引，不直接列出所有子文档。
2. 各层具体文档由本层 index 维护。
3. 新增文档后必须更新对应分区索引。
4. 删除、归档、迁移文档后必须同步修改对应分区索引。
5. `stale`、`deprecated`、`archived` 文档不得作为默认推荐文档。
6. 索引应指向 Markdown 事实源，不应指向 Obsidian workspace、插件运行代码、Notebook 输出或 HTML 展示产物。

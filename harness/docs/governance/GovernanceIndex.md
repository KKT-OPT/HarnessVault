---
documentName: docs/governance/GovernanceIndex.md
title: Governance Index
aliases:
  - GovernanceIndex
  - Governance 文档索引
  - 治理索引
tags:
  - harness
  - governance
  - index
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 Harness Governance Runtime Layer 的治理文档。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[RuntimeBoundaryPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Governance Index

## 1. 层级定位

Governance Runtime Layer 负责 Harness 文档资产、Skill、Memory、Workflow、RAG、项目模板、runtime 边界和跨层治理的生命周期管理。

## 2. 治理文档

| 文档 | 状态 | 用途 |
|---|---|---|
| [[ArtifactLifecycle]] | draft | 文档资产、Skill、Memory、RAG、Workflow 的生命周期状态和迁移规则 |
| [[ScheduledGovernance]] | draft | 定期治理、dry-run、报告优先和人工审批机制 |
| [[SecurityGovernance]] | draft | 上下文安全、插件代码边界、外部工具输出审查 |
| [[RuntimeBoundaryPolicy]] | draft | 区分 agent runtime 与 HarnessVault 文档控制层职责边界 |
| [[IndexMaintenancePolicy]] | draft | 索引维护、链接治理和 orphan 文档检查 |
| [[SkillGovernance]] | draft | Skill 创建、更新、合并、sidecar telemetry、归档和恢复 |
| [[MemoryGovernance]] | draft | Memory 写入、替换、归档、晋升和污染控制 |
| [[DocumentGovernance]] | draft | 文档新增、更新、拆分、归档和删除规则 |
| [[KnowledgePromotionPolicy]] | draft | Workflow、Memory、Skill、RAG、Project Facts 之间的晋升规则 |
| [[CleanupPolicy]] | draft | 文档资产、Memory、Skill、RAG、报告产物的清理和归档规则 |

## 3. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[Dashboard]]
- [[RuntimeBoundaryPolicy]]

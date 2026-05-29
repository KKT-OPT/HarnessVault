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
version: v0.1.0
createdAt: 2026-05-29 00:00:00.000 +08:00
updatedAt: 2026-05-29 00:00:00.000 +08:00
status: draft
type: index
purpose: HarnessVault 文档导航入口，帮助人类和智能体快速定位必读、按需读和治理相关文档。
scope: HarnessVault 通用文档系统。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - docs/HarnessEngineering.md
  - docs/PLANS.md
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-29 00:00:00.000 +08:00
---

# Harness 文档索引

## 1. 必读入口

任何智能体处理 HarnessVault 任务时，应优先读取：

1. [[HarnessEngineering]]：Harness Engineering 总体架构设计。
2. [[PLANS]]：当前阶段计划和后续任务。
3. `AGENTS.md`：vault 内智能体入口契约。

## 2. 架构与总体设计

| 文档 | 状态 | 用途 |
|---|---|---|
| [[HarnessEngineering]] | draft | Harness 文档系统总体架构、治理机制、目录边界和长期演进规则 |

## 3. 计划与阶段治理

| 文档 | 状态 | 用途 |
|---|---|---|
| [[PLANS]] | draft | 当前阶段目标、验收标准和下一步拆分计划 |

## 4. Governance 文档区

后续将从 [[HarnessEngineering]] 拆分：

- [[ArtifactLifecycle]]
- [[ScheduledGovernance]]
- [[SecurityGovernance]]
- [[IndexMaintenancePolicy]]
- [[SkillGovernance]]
- [[MemoryGovernance]]
- [[DocumentGovernance]]
- [[KnowledgePromotionPolicy]]
- [[CleanupPolicy]]

## 5. Agent 文档区

后续将从 [[HarnessEngineering]] 拆分：

- [[ContextLoadingPolicy]]
- [[PromptPolicy]]
- [[SkillPolicy]]
- [[MemoryPolicy]]
- [[SkillIndex]]
- [[MemoryIndex]]

## 6. RAG 文档区

后续将从 [[HarnessEngineering]] 拆分：

- [[RAGIndex]]
- [[KnowledgeBasePolicy]]

## 7. Project Template 文档区

后续将从 [[HarnessEngineering]] 拆分：

- [[ProjectIndex]]
- project-template/prd/
- project-template/architecture/
- project-template/dictionary/
- project-template/git/
- project-template/workflow/

## 8. Obsidian 辅助视图

| 文档 | 用途 |
|---|---|
| [[Dashboard]] | 使用 Dataview 查看草稿、待审查文档、治理文档和索引状态 |

## 9. 索引维护规则

1. 新增文档后必须更新本索引或对应分区索引。
2. 删除、归档、迁移文档后必须同步修改索引。
3. `stale`、`deprecated`、`archived` 文档不得作为默认推荐文档。
4. 索引应指向 Markdown 事实源，不应指向 Obsidian workspace、插件代码、Notebook 输出或 HTML 展示产物。

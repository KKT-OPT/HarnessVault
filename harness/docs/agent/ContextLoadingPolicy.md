---
documentName: docs/agent/ContextLoadingPolicy.md
title: Context Loading Policy
aliases:
  - ContextLoadingPolicy
  - 上下文加载规则
tags:
  - harness
  - agent
  - context
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义智能体在不同任务类型下加载 Harness 上下文的规则。
scope: HarnessVault agent policy。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[AgentIndex]]"
  - "[[IndexMaintenancePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Context Loading Policy

## 1. 目的

本文档定义智能体在 HarnessVault 中执行不同类型任务时，应如何加载最小必要上下文，避免遗漏关键事实，也避免把无关文档、Obsidian workspace、插件代码和生成产物注入任务上下文。

## 2. 基本原则

上下文加载遵循以下原则：

1. 入口优先：先读 `AGENTS.md`、[[INDEX]]、[[PLANS]]；
2. 最小必要：只读取完成任务所需的最小文档集合；
3. 层级定位：先通过顶层 index 找到层级 index，再读取具体文档；
4. 事实优先：以 GitHub 仓库中的 Markdown 事实源为准；
5. 状态过滤：`archived`、`deprecated`、`stale` 文档不作为默认上下文；
6. 证据分离：reports 是治理证据，不等同于正式事实源；
7. 工具边界：`.obsidian/`、插件代码、workspace.json 不进入默认上下文。

## 3. 通用读取顺序

任何任务默认读取：

```text
1. AGENTS.md
2. harness/AGENTS.md
3. docs/INDEX.md
4. docs/PLANS.md
5. 与任务相关的层级 index
6. 与任务相关的具体文档
```

当任务涉及当前仓库路径时，还应读取：

```text
README.md
harness/README.md
```

## 4. 任务类型与上下文集合

### 4.1 架构设计任务

读取：

1. [[HarnessEngineering]]；
2. [[INDEX]]；
3. [[PLANS]]；
4. 相关层级 index；
5. 相关治理文档。

适用于：架构调整、目录调整、分层设计、边界定义、长期演进设计。

### 4.2 索引维护任务

读取：

1. [[INDEX]]；
2. [[IndexMaintenancePolicy]]；
3. 对应层级 index；
4. [[ReportsIndex]]；
5. `docs/reports/index/README.md`。

适用于：新增文档、移动文档、修复 broken link、处理 orphan document、更新 `relatedDocuments`。

### 4.3 治理规则任务

读取：

1. [[GovernanceIndex]]；
2. 目标治理文档；
3. [[ArtifactLifecycle]]；
4. [[ScheduledGovernance]]；
5. [[ReportsIndex]]。

适用于：新增或修改治理规则、生命周期规则、定期治理规则、清理规则、安全规则。

### 4.4 Skill 相关任务

读取：

1. [[AgentIndex]]；
2. [[SkillPolicy]]；
3. [[SkillGovernance]]；
4. [[SkillIndex]]；
5. 相关 Skill 文档。

禁止只基于一次任务直接创建新 Skill。必须先检查是否已有可扩展的 umbrella skill。

### 4.5 Memory 相关任务

读取：

1. [[AgentIndex]]；
2. [[MemoryPolicy]]；
3. [[MemoryGovernance]]；
4. [[MemoryIndex]]；
5. 相关 Memory 文档或 candidate。

禁止把一次性日志、临时状态、未验证推测、大段代码写入 Memory。

### 4.6 RAG 相关任务

读取：

1. [[RAGIndex]]；
2. [[KnowledgeBasePolicy]]；
3. [[KnowledgePromotionPolicy]]；
4. 目标 RAG 文档。

外部资料、NotebookLM 输出、网页摘要进入 RAG 前必须经过审查。

### 4.7 Project Template 任务

读取：

1. [[ProjectIndex]]；
2. [[HarnessEngineering]] 中 Project Harness Instance 相关章节；
3. 目标 project-template 文档；
4. [[ArtifactLifecycle]]。

适用于：新增项目模板、修改项目实例化结构、定义项目 workflow 模板。

### 4.8 Obsidian / Templater 任务

读取：

1. [[ObsidianSetup]]；
2. [[INDEX]]；
3. [[Dashboard]]；
4. `harness/.obsidian/community-plugins.json`；
5. `harness/.obsidian/plugins/templater-obsidian/data.json`。

禁止把 `workspace.json` 作为事实源。

### 4.9 报告和定期治理任务

读取：

1. [[ScheduledGovernance]]；
2. [[ReportsIndex]]；
3. 目标 reports README；
4. [[ArtifactLifecycle]]；
5. [[IndexMaintenancePolicy]]。

报告只能提出问题、证据和建议，不能直接替代正式文档更新。

## 5. 禁止默认加载的内容

默认禁止加载：

```text
harness/.obsidian/workspace.json
harness/.obsidian/plugins/**/main.js
harness/.obsidian/plugins/**/styles.css
harness/.obsidian/plugins/**/obsidian_askpass.sh
node_modules/
build/
dist/
generated HTML
Notebook 临时输出
```

除非用户明确要求分析这些文件，否则智能体不得把它们作为 Harness 事实源。

## 6. 上下文冲突处理

当不同文档内容冲突时，按以下优先级处理：

```text
用户当前明确指令
> AGENTS.md / harness/AGENTS.md
> docs/PLANS.md 当前阶段
> docs/INDEX.md 与层级 index
> 正式 policy 文档
> HarnessEngineering.md 总设计
> reports 证据
> archived/stale 文档
```

冲突无法解决时，应报告冲突，不应静默选择。

## 7. 输出要求

智能体完成任务时应说明：

1. 读取了哪些核心文档；
2. 基于哪些规则做出修改；
3. 是否更新了对应 index；
4. 是否产生报告或候选项；
5. 是否有未解决的上下文冲突。

## 8. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[PLANS]]
- [[AgentIndex]]
- [[IndexMaintenancePolicy]]

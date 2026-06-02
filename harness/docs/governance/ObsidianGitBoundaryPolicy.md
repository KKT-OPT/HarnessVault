---
documentName: docs/governance/ObsidianGitBoundaryPolicy.md
title: Obsidian Git Boundary Policy
aliases:
  - ObsidianGitBoundaryPolicy
  - Obsidian Git Boundary
  - Obsidian 与 Git 边界规则
tags:
  - harness
  - governance
  - obsidian
  - git
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Obsidian 配置、UI 状态、插件代码、模板目录和 Git 跟踪边界。
scope: HarnessVault Obsidian and Git boundary。
prerequisites:
  - docs/ObsidianSetup.md
  - .gitignore
relatedDocuments:
  - "[[GovernanceIndex]]"
  - "[[ObsidianSetup]]"
  - "[[SecurityGovernance]]"
  - "[[TemplatesIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Obsidian Git Boundary Policy

## 1. 目的

本文档定义 HarnessVault 中 Obsidian 配置、UI 状态、插件代码、模板目录和 Git 跟踪边界，避免编辑器状态或插件运行代码污染 Harness 文档事实源和智能体默认上下文。

## 2. 资产分类

| 类型 | 示例 | 是否事实源 | Git 策略 | 默认上下文 |
|---|---|---|---|---|
| Harness facts | `docs/**/*.md`, `AGENTS.md`, `README.md` | 是 | 跟踪 | 可加载 |
| Templates | `templates/**/*.md` | 模板源 | 跟踪 | 按任务加载 |
| Reports | `docs/reports/**/*.md` | 证据，不是事实源 | 选择性跟踪 | 不默认加载 archived report |
| Scripts | `scripts/**/*.py` | 工具源 | 跟踪 | 按任务加载 |
| Obsidian lightweight config | `app.json`, `appearance.json`, `community-plugins.json`, `core-plugins.json`, plugin `manifest.json`, plugin `data.json` | 否 | 可选择跟踪 | 否 |
| Obsidian volatile UI state | `workspace.json`, `workspace-mobile.json`, `workspaces.json`, `graph.json` | 否 | 忽略 | 否 |
| Plugin runtime code | plugin `main.js`, `styles.css`, helper scripts | 否 | 忽略 | 否 |
| IDE local state | `.idea/workspace.xml`, local shelves | 否 | 忽略 | 否 |

## 3. Obsidian 文件规则

### 3.1 可跟踪内容

可在人工确认后跟踪：

1. `harness/.obsidian/app.json`；
2. `harness/.obsidian/appearance.json`；
3. `harness/.obsidian/community-plugins.json`；
4. `harness/.obsidian/core-plugins.json`；
5. 插件 `manifest.json`；
6. 插件 `data.json`。

这些文件是编辑体验配置，不是 Harness facts。

### 3.2 必须忽略内容

必须忽略：

1. `harness/.obsidian/workspace.json`；
2. `harness/.obsidian/workspace-mobile.json`；
3. `harness/.obsidian/workspaces.json`；
4. `harness/.obsidian/graph.json`；
5. `harness/.obsidian/plugins/**/main.js`；
6. `harness/.obsidian/plugins/**/styles.css`；
7. `harness/.obsidian/plugins/**/obsidian_askpass.sh`。

## 4. 智能体上下文规则

智能体默认不得读取：

1. Obsidian workspace 状态；
2. Obsidian graph 状态；
3. 插件运行代码；
4. IDE 本地状态；
5. archived reports。

如用户明确要求排查 Obsidian 配置问题，智能体可以读取轻量配置文件，但不得把它们当作 Harness facts。

## 5. 模板规则

`templates/**` 是唯一模板源，与 Obsidian workspace 状态无关。Templater 的模板目录应配置为相对 vault root 的：

```text
templates
```

模板文件自身应由 Git 跟踪；模板运行生成的项目事实应进入目标项目文档，而不是通用 HarnessVault。

## 6. Git 维护规则

HarnessVault 使用 GitHub 分支和 PR 维护，不依赖 Obsidian Git 自动提交。

Obsidian Git 插件不作为推荐插件，也不作为仓库维护机制。

## 7. 检查规则

P14 边界检查应确认：

1. `.gitignore` 忽略 volatile UI state；
2. `.gitignore` 忽略 plugin runtime code；
3. ObsidianSetup 与 `.gitignore` 口径一致；
4. graph/workspace 不作为事实源；
5. 插件运行代码不进入默认上下文。

## 8. 关联文档

- [[GovernanceIndex]]
- [[ObsidianSetup]]
- [[SecurityGovernance]]
- [[TemplatesIndex]]
- [[INDEX]]

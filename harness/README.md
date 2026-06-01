---
documentName: README.md
title: Harness Vault README
aliases:
  - HarnessVaultREADME
  - VaultREADME
  - Harness Vault
tags:
  - harness
  - readme
  - entry
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: entry
purpose: 说明 Harness vault 根目录定位、事实源边界和推荐入口。
scope: HarnessVault root。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[VaultAgents]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[HarnessEngineering]]"
  - "[[TemplatesIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Vault

本目录是 HarnessVault 的 Obsidian vault root，也是 Harness 文档系统的主工作区。

## 目录定位

```text
harness/
├── AGENTS.md                  # vault 内智能体入口
├── README.md                  # vault 说明
├── docs/                      # Harness 文档事实源
├── templates/                 # Obsidian / Templater / Prompt 文档模板统一来源
├── scripts/                   # dry-run 自检脚本
└── .obsidian/                 # Obsidian 编辑配置
```

## 事实源

- `AGENTS.md` 是智能体入口契约，所有任务优先读取。
- `docs/**/*.md` 是 Harness 文档事实源。
- `templates/**` 是统一模板源，用于生成文档、workflow、prompt 或其他可复制结构。
- `.obsidian/` 是编辑器配置，不是事实源。
- `docs/reports/` 保存治理报告，报告本身不是事实源，除非被审查后吸收到正式文档。

## 推荐入口

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/PLANS.md`
4. `docs/HarnessEngineering.md`

## Obsidian 使用原则

- 使用 Obsidian 阅读、编辑和导航 Markdown 文档。
- 使用 Dataview 生成动态视图，但不要把 Dataview 输出当作唯一索引。
- 使用 Templater 生成标准文档骨架。
- 所有模板统一放在 `templates/**`。
- 使用 GitHub 分支 / PR 维护远程仓库，不依赖 Obsidian Git 自动提交。

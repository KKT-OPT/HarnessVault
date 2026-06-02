---
documentName: docs/ObsidianSetup.md
title: Obsidian 使用配置说明
aliases:
  - ObsidianSetup
  - Obsidian 配置
  - Obsidian 使用说明
tags:
  - harness
  - obsidian
  - templater
  - dataview
  - linter
version: v0.3.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 说明 HarnessVault 中 Obsidian vault、插件、模板和 Git 维护方式。
scope: HarnessVault Obsidian 使用配置。
prerequisites:
  - AGENTS.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[Dashboard]]"
  - "[[ObsidianGitBoundaryPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Obsidian 使用配置说明

## 1. Vault Root

HarnessVault 的 Obsidian vault root 是：

```text
harness/
```

不要把仓库根目录作为 Obsidian vault root。

## 2. Git 维护方式

HarnessVault 使用 GitHub 分支和 PR 维护远程版本。

不使用 Obsidian Git 作为仓库维护方式。

## 3. 推荐插件

当前推荐启用：

```text
Dataview
Obsidian Linter
Templater
```

不推荐启用：

```text
Obsidian Git
```

## 4. Templater 配置

Templater 的 Template folder location 必须设置为：

```text
templates
```

这里的路径是相对于 Obsidian vault root `harness/` 的路径，不是 `harness/templates`。

## 5. Templater 使用方式

如果使用 “Insert template / append template” 类命令，必须先打开一个目标 Markdown 文件，并确保编辑器中有光标。

错误场景：

```text
直接选中模板文件，然后执行插入模板。
```

可能出现：

```text
no active editor, can't append templates
```

正确流程：

```text
1. 新建或打开目标 Markdown 文件；
2. 点击目标文件编辑区域，确保有活动编辑器；
3. 执行 Templater 插入模板命令；
4. 选择 templates/ 下的模板文件。
```

## 6. Folder Template 当前策略

当前不建议自动启用 folder templates。

原因：

1. HarnessVault 当前处于架构占位文档初始化阶段；
2. 不同目录的文档 frontmatter 字段还在收敛；
3. 自动触发模板可能误改占位文档或已有文档。

后续可在模板规范稳定后，再启用以下映射：

| 目标目录 | 推荐模板 |
|---|---|
| docs/governance/ | templates/GovernancePolicyTemplate.md |
| docs/agent/skills/ | templates/SkillTemplate.md |
| docs/agent/memory/ | templates/MemoryTemplate.md |
| docs/project/workflow/ | templates/WorkflowTemplate.md |
| docs/reports/ | templates/ReportTemplate.md |

## 7. Dataview 使用规则

Dataview 只用于生成动态视图，不替代正式索引。

正式索引仍以：

```text
docs/INDEX.md
```

为准。

## 8. Linter 使用规则

Linter 可以统一 Markdown 风格，但不得破坏：

```text
YAML frontmatter 字段名
Mermaid 代码块
Dataview 代码块
Markdown 表格
JSON 示例代码块
```

建议禁用自动排序 YAML key、自动重写 timestamp、自动重写 tags / aliases 的规则。

## 9. workspace / graph 规则

以下文件只保存 Obsidian UI 状态，不是 Harness 文档事实源，也不是文档自动更新机制：

```text
harness/.obsidian/workspace.json
harness/.obsidian/workspace-mobile.json
harness/.obsidian/workspaces.json
harness/.obsidian/graph.json
```

因此：

```text
这些文件应保留在本地；
这些文件不应提交到 Git；
这些文件不应进入智能体默认上下文。
```

## 10. 插件运行代码规则

不应提交以下插件运行代码：

```text
harness/.obsidian/plugins/**/main.js
harness/.obsidian/plugins/**/styles.css
harness/.obsidian/plugins/**/obsidian_askpass.sh
```

可以在人工确认后保留轻量配置，例如：

```text
harness/.obsidian/app.json
harness/.obsidian/appearance.json
harness/.obsidian/community-plugins.json
harness/.obsidian/core-plugins.json
harness/.obsidian/plugins/**/manifest.json
harness/.obsidian/plugins/**/data.json
```

轻量配置不是 Harness facts，只是编辑体验配置。

## 11. 智能体上下文规则

智能体默认读取：

1. `AGENTS.md`；
2. `docs/INDEX.md`；
3. `docs/PLANS.md`；
4. 任务相关的 Harness Markdown 文档。

智能体默认不得读取：

1. workspace / graph 状态；
2. 插件运行代码；
3. IDE 本地状态；
4. archived reports。

## 12. 关联文档

- [[HarnessEngineering]]
- [[INDEX]]
- [[PLANS]]
- [[Dashboard]]
- [[ObsidianGitBoundaryPolicy]]

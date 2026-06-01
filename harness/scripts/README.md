---
documentName: scripts/README.md
title: Harness Scripts README
aliases:
  - HarnessScripts
  - Scripts README
  - 脚本说明
tags:
  - harness
  - scripts
  - dry-run
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 说明 HarnessVault 自检脚本的定位、运行边界和 dry-run 规则。
scope: HarnessVault scripts。
prerequisites:
  - docs/governance/ScheduledGovernance.md
  - docs/governance/SecurityGovernance.md
relatedDocuments:
  - "[[ScheduledGovernance]]"
  - "[[SecurityGovernance]]"
  - "[[IndexMaintenancePolicy]]"
  - "[[FrontmatterPathDryRunReport]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Scripts README

## 1. 定位

`scripts/` 用于保存 HarnessVault 的辅助检查脚本。

脚本默认只允许 dry-run，不能自动修改文档，不能删除文件，不能写入用户知识，不能写入具体项目事实。

## 2. 当前脚本

| 脚本 | 用途 |
|---|---|
| `check_harness_docs.py` | 检查 Markdown frontmatter、`documentName` 路径一致性和 wikilink 候选解析 |

## 3. 运行边界

脚本可以：

1. 扫描 Markdown 文档；
2. 输出检查结果；
3. 返回非零退出码提示问题；
4. 帮助生成报告草稿。

脚本不得：

1. 自动修改文档；
2. 自动删除文档；
3. 自动移动文档；
4. 读取 Obsidian 插件运行代码作为事实源；
5. 读取或输出 secret、token、password。

## 4. 建议运行方式

```bash
python harness/scripts/check_harness_docs.py --root harness --format text
```

## 5. 关联文档

- [[ScheduledGovernance]]
- [[SecurityGovernance]]
- [[IndexMaintenancePolicy]]
- [[FrontmatterPathDryRunReport]]

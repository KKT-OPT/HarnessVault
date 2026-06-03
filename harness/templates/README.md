---
documentName: templates/README.md
title: Templates Index
aliases:
  - TemplatesIndex
  - Templates README
  - 模板索引
tags:
  - harness
  - templates
  - index
version: v0.2.1
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 的统一模板源目录。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[VaultAgents]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[ProjectIndex]]"
  - "[[PromptPolicy]]"
  - "[[ComplexTaskPromptTemplate]]"
  - "[[RawKnowledgeMaterialTemplate]]"
  - "[[EffectiveKnowledgeTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Templates Index

## 1. 定位

`templates/**` 是 HarnessVault 的唯一模板源目录。

所有可复制模板、Obsidian / Templater 模板、文档模板、workflow 模板、policy 模板、report 模板、memory 模板、skill 模板和 prompt 模板，都应统一放在本目录下。

其他目录可以说明如何使用模板，但不应保留重复的可复制模板正文。

## 2. 当前模板

| 模板 | 用途 |
|---|---|
| `GovernancePolicyTemplate.md` | 生成 governance policy 文档 |
| `MemoryTemplate.md` | 生成 Memory 文档 |
| `ReportTemplate.md` | 生成治理或索引报告 |
| `SkillTemplate.md` | 生成 Skill 文档 |
| `WorkflowTemplate.md` | 生成项目 workflow 文档 |
| [[ComplexTaskPromptTemplate]] | 生成结构化复杂任务 prompt |
| [[RawKnowledgeMaterialTemplate]] | 生成原始资料层候选文档 |
| [[EffectiveKnowledgeTemplate]] | 生成审查后的有效知识库文档 |

## 3. Prompt 模板规则

`templates/ComplexTaskPromptTemplate.md` 是复杂任务 prompt 的统一源模板。复杂任务 prompt 应保留 entry contract、final goal、previous context、feedback、task、inspection scope、constraints、acceptance criteria、output format 和 governance notes。

XML-like block 只是 prompt 结构约定，不是强制 schema。生成后的 prompt 仍必须要求智能体优先读取 `AGENTS.md`、`docs/INDEX.md`、`docs/PLANS.md` 和任务相关文档。

## 4. 模板使用入口

任何智能体或提示词模板在使用模板前，应优先读取：

1. `AGENTS.md`；
2. `docs/INDEX.md`；
3. `docs/PLANS.md`；
4. 本文档。

## 5. 模板 frontmatter 规则

`templates/**` 下的模板文件是源模板，不等同于生成后的目标文档。

因此模板文件可以包含：

1. 模板自身路径，例如 `documentName: templates/<template-name>.md`；
2. 生成目标路径，例如 `templateTarget: docs/<target-path>.md`；
3. 模板引擎，例如 `templateEngine: obsidian-templater`；
4. 模板用途，例如 `templatePurpose`。

## 6. 禁止事项

1. 禁止在非 `templates/**` 目录保留重复模板正文。
2. 禁止把模板占位内容当作项目事实。
3. 禁止把模板生成目标路径误判为模板文件自身路径。
4. 禁止在模板中写入真实用户知识或具体项目事实。

## 7. 关联文档

- [[VaultAgents]]
- [[INDEX]]
- [[PLANS]]
- [[ProjectIndex]]
- [[PromptPolicy]]
- [[ComplexTaskPromptTemplate]]
- [[RawKnowledgeMaterialTemplate]]
- [[EffectiveKnowledgeTemplate]]

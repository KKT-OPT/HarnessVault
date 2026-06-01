---
documentName: templates/SkillTemplate.md
templateName: SkillTemplate
templateTarget: docs/agent/skills/<category>/<skill-name>/SKILL.md
templateEngine: obsidian-templater
templatePurpose: 生成 Skill 文档。
title: Skill Template
aliases:
  - SkillTemplate
tags:
  - harness
  - skill
  - template
version: v0.2.0
createdAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
updatedAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
status: draft
type: template
purpose: 提供 Skill 文档生成模板。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[SkillIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter:
id: skill.<category>.<name>
name: <skill-name>
description: <trigger-oriented description>
origin: manual
---

# <Skill Name>

## When to Use

说明什么情况下应该使用这个 Skill。

## Inputs

说明执行该 Skill 需要哪些输入。

## Procedure

1. 步骤一
2. 步骤二
3. 步骤三

## Pitfalls

- 常见错误一
- 常见错误二

## Verification

- 验收点一
- 验收点二

## Related Documents

- `docs/...`

## Related Scripts

- `docs/agent/skills/<category>/<skill>/scripts/...`

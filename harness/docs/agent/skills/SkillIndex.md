---
documentName: docs/agent/skills/SkillIndex.md
title: Skill Index
aliases:
  - SkillIndex
tags:
  - harness
  - skill
  - index
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 索引 HarnessVault 中的 Skill 模板、usage sidecar 和正式 Skill 目录规则。
scope: HarnessVault skills。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[SkillPolicy]]"
  - "[[SkillGovernance]]"
  - "[[SKILL]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Skill Index

## 1. 定位

Skill 是程序性记忆，用于保存可复用任务执行流程。HarnessVault 当前阶段只提供通用 Skill 资产骨架，不创建真实业务 Skill，不记录具体项目流程。

## 2. 当前 Skill 资产

| 资产 | 状态 | 用途 |
|---|---|---|
| [[SKILL]] | draft | 通用 Skill 文档模板 |
| `.skill-usage.json` | draft | Skill 使用统计 sidecar 的空结构 |

## 3. 正式 Skill 存放规则

后续正式 Skill 应放置在：

```text
docs/agent/skills/<category>/<skill-name>/SKILL.md
```

推荐目录结构：

```text
docs/agent/skills/<category>/<skill-name>/
├── SKILL.md
├── references/
├── templates/
├── scripts/
└── assets/
```

## 4. 禁止事项

1. 禁止 one-session-one-skill。
2. 禁止在通用 HarnessVault 中写入具体项目 Skill。
3. 禁止把一次性任务经验直接写成 Skill。
4. 禁止把 usage 统计写入 `SKILL.md` frontmatter。
5. 禁止把未审查外部资料写入 Skill。

## 5. 关联文档

- [[SkillPolicy]]
- [[SkillGovernance]]
- [[KnowledgePromotionPolicy]]
- [[ArtifactLifecycle]]

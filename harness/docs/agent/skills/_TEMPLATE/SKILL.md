---
documentName: docs/agent/skills/_TEMPLATE/SKILL.md
title: Generic Skill Template
aliases:
  - SKILL
  - Skill Template
  - 通用 Skill 模板
tags:
  - harness
  - skill
  - template
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: skill
purpose: 提供通用 Skill 文档模板，不包含具体项目流程。
scope: HarnessVault skill template。
prerequisites:
  - docs/agent/SkillPolicy.md
relatedDocuments:
  - "[[SkillIndex]]"
  - "[[SkillPolicy]]"
  - "[[SkillGovernance]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Generic Skill Template

## 1. Skill Purpose

```text
<what reusable task this skill helps with>
```

## 2. Trigger Conditions

Use this Skill when:

1. `<trigger-condition-1>`
2. `<trigger-condition-2>`
3. `<trigger-condition-3>`

Do not use this Skill when:

1. `<non-trigger-condition-1>`
2. `<non-trigger-condition-2>`

## 3. Required Context

| Context | Required | Source |
|---|---|---|
| `<context-name>` | `yes/no` | `<source-doc>` |

## 4. Procedure

1. `<step-1>`
2. `<step-2>`
3. `<step-3>`

## 5. Verification

1. `<verification-step-1>`
2. `<verification-step-2>`
3. `<verification-step-3>`

## 6. Failure Handling

| Failure | Likely Cause | Repair Action |
|---|---|---|
| `<failure>` | `<cause>` | `<action>` |

## 7. Outputs

| Output | Format | Destination |
|---|---|---|
| `<output>` | `<format>` | `<destination>` |

## 8. References

- `<reference-link>`

## 9. Governance Notes

1. This template must not contain project-specific facts.
2. This template must not contain user knowledge.
3. New Skills require review according to [[SkillPolicy]].
4. Usage metadata belongs in `.skill-usage.json`, not in this frontmatter.

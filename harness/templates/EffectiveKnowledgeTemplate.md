---
documentName: templates/EffectiveKnowledgeTemplate.md
templateName: EffectiveKnowledgeTemplate
templateTarget: docs/rag/<domain-or-standard>/<knowledge-name>.md
templateEngine: obsidian-templater
templatePurpose: 生成审查后的有效知识库文档。
title: Effective Knowledge Template
aliases:
  - EffectiveKnowledgeTemplate
  - Effective Knowledge Template
  - 有效知识模板
tags:
  - harness
  - rag
  - knowledge
  - template
version: v0.1.0
createdAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
updatedAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
status: draft
type: template
purpose: 提供审查后的有效知识库文档模板。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[RAGIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter:
sourceMaterial: placeholder
reviewStatus: approved
---

# <Knowledge Title>

## 1. Knowledge Summary

```text
<concise reusable knowledge summary>
```

## 2. Scope

| Field | Value |
|---|---|
| Knowledge Type | `<domain / standard>` |
| Applies To | `<scope>` |
| Does Not Apply To | `<scope>` |
| Stability | `<stable / evolving / time-sensitive>` |
| Review After | `<date>` |

## 3. Key Concepts

| Concept | Definition | Aliases |
|---|---|---|
| `<concept>` | `<definition>` | `<aliases>` |

## 4. Usage Guidance

1. `<guidance-1>`
2. `<guidance-2>`
3. `<guidance-3>`

## 5. Evidence and Source Trace

| Source | Evidence Summary | Notes |
|---|---|---|
| `<source>` | `<summary>` | `<notes>` |

## 6. Related Documents

- [[RAGIndex]]
- [[KnowledgeBasePolicy]]

## 7. Governance Notes

1. This document is active knowledge only after human review.
2. Do not paste large copyrighted source content.
3. If project-specific, move to Project Facts instead of generic RAG.

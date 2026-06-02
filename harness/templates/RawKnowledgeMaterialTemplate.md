---
documentName: templates/RawKnowledgeMaterialTemplate.md
templateName: RawKnowledgeMaterialTemplate
templateTarget: docs/rag/intake/raw/<material-id>.md
templateEngine: obsidian-templater
templatePurpose: 生成原始资料层候选文档。
title: Raw Knowledge Material Template
aliases:
  - RawKnowledgeMaterialTemplate
  - Raw Knowledge Material Template
  - 原始资料模板
tags:
  - harness
  - rag
  - intake
  - template
version: v0.1.0
createdAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
updatedAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
status: draft
type: template
purpose: 记录原始资料元信息、摘要、来源、关键词和语义增强入口。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[KnowledgeIntakePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter:
sourceType: placeholder
sourceLocation: placeholder
reviewStatus: candidate
---

# <Raw Material Title>

## 1. Source Metadata

| Field | Value |
|---|---|
| Source Type | `<pdf / web / notebook / book / paper / user-note / transcript>` |
| Source Location | `<path-or-url-or-reference>` |
| Author / Organization | `<author>` |
| Published At | `<date-or-unknown>` |
| Collected At | `<date>` |
| Submitted By | `<human / agent>` |
| Usage Rights | `<unknown / permitted / restricted>` |

## 2. Short Summary

```text
<short paraphrased summary; do not paste large copyrighted source content>
```

## 3. Human Semantic Notes

```text
<user-provided context, importance, scope, caveats, or domain interpretation>
```

## 4. Candidate Keywords

| Type | Keywords |
|---|---|
| Original terms | `<keywords>` |
| Standard terms | `<keywords>` |
| Synonyms | `<keywords>` |
| Domain terms | `<keywords>` |

## 5. Potential Routing

| Target | Candidate | Reason |
|---|---|---|
| RAG domain | `<yes/no>` | `<reason>` |
| RAG standard | `<yes/no>` | `<reason>` |
| Project facts | `<yes/no>` | `<reason>` |
| Skill | `<yes/no>` | `<reason>` |
| Memory | `<yes/no>` | `<reason>` |

## 6. Review Checklist

- [ ] Source is clear.
- [ ] Sensitive content checked.
- [ ] Copyright risk checked.
- [ ] Project fact boundary checked.
- [ ] Duplicate knowledge checked.
- [ ] Human review completed.

## 7. Promotion Decision

| Field | Value |
|---|---|
| Decision | `<approve / reject / defer>` |
| Target Document | `<target>` |
| Reviewer | `<reviewer>` |
| Decision Date | `<date>` |

---
documentName: docs/rag/intake/KnowledgeIntakeTemplate.md
title: Knowledge Intake Template
aliases:
  - KnowledgeIntakeTemplate
  - Knowledge Intake Template
  - 知识引入模板
tags:
  - harness
  - rag
  - intake
  - template
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供用户知识、外部资料、领域知识或项目事实候选的通用引入模板。
scope: HarnessVault RAG intake。
prerequisites:
  - docs/rag/KnowledgeIntakePolicy.md
relatedDocuments:
  - "[[KnowledgeIntakePolicy]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
sourceType: placeholder
sourceLocation: placeholder
targetAsset: candidate
reviewStatus: template
keywords:
  - placeholder
---

# Knowledge Intake Template

## 1. Intake Metadata

| Field | Value |
|---|---|
| Intake ID | `<intake-id>` |
| Source Type | `user-input / external-doc / web / pdf / notebooklm / workflow / report` |
| Source Location | `<source-location>` |
| Submitted By | `<submitter>` |
| Submitted At | `<timestamp>` |
| Review Status | `candidate / under-review / approved / rejected / archived` |
| Target Asset | `RAG / Project Facts / Memory / Skill / Workflow / Report` |

## 2. Summary

```text
<short-summary>
```

## 3. Original Knowledge Excerpt

```text
<short excerpt or paraphrase only; do not paste large source content>
```

## 4. Keywords

| Type | Keywords |
|---|---|
| Original terms | `<keywords>` |
| Standard terms | `<keywords>` |
| Synonyms | `<keywords>` |
| Domain terms | `<keywords>` |
| Project terms | `<keywords>` |

## 5. Classification

| Question | Answer |
|---|---|
| Is it stable knowledge? | `<yes/no/unknown>` |
| Is it project-specific? | `<yes/no/unknown>` |
| Is it user preference? | `<yes/no/unknown>` |
| Is it reusable procedure? | `<yes/no/unknown>` |
| Is it task evidence? | `<yes/no/unknown>` |
| Does it contain sensitive content? | `<yes/no/unknown>` |

## 6. Routing Recommendation

| Candidate Target | Recommended | Reason |
|---|---|---|
| RAG | `<yes/no>` | `<reason>` |
| Project Facts | `<yes/no>` | `<reason>` |
| Memory | `<yes/no>` | `<reason>` |
| Skill | `<yes/no>` | `<reason>` |
| Workflow | `<yes/no>` | `<reason>` |
| Report | `<yes/no>` | `<reason>` |

## 7. Review Notes

1. `<review-note-1>`
2. `<review-note-2>`
3. `<review-note-3>`

## 8. Promotion Decision

| Field | Value |
|---|---|
| Decision | `approve / reject / defer` |
| Target Document | `<target-document>` |
| Reviewer | `<reviewer>` |
| Decision Date | `<date>` |
| Notes | `<notes>` |

## 9. Governance Notes

1. This template is not a fact source.
2. This template must not store secrets or large raw source content.
3. Approved knowledge must be rewritten into the correct target asset.
4. Indexes must be updated after promotion.

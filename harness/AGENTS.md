---
documentName: AGENTS.md
title: Harness Vault Agent Entry
aliases:
  - VaultAgents
  - HarnessVaultAgents
  - AGENTS
tags:
  - harness
  - agent
  - entry
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: entry
purpose: 定义 Harness vault 内智能体必须优先读取的入口契约。
scope: HarnessVault agent entry。
prerequisites:
  - docs/INDEX.md
relatedDocuments:
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[HarnessEngineering]]"
  - "[[TemplatesIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# AGENTS.md

## 1. Harness Entry Contract

Any agent working inside the Harness vault must read:

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/PLANS.md`
4. Task-specific documents listed in `docs/INDEX.md`

All prompt templates, workflow templates, documentation templates and future agent-facing templates must preserve this entry order. When a generated prompt or generated workflow needs context, it should point the agent back to `AGENTS.md` first, then `docs/INDEX.md` and `docs/PLANS.md`.

## 2. Source of Truth Rule

- Harness source documents live under `docs/**/*.md`.
- Harness entry documents are `AGENTS.md` and `README.md` at the vault root.
- Obsidian configuration under `.obsidian/` is an editing aid, not a Harness fact source.
- Generated reports under `docs/reports/` are evidence, not final source documents.
- Reusable source templates live under `templates/**`.

## 3. Project Fact Rule

Do not infer stable project facts from memory alone. Stable project facts must be documented in the appropriate project or template document.

## 4. RAG Rule

Documents under `docs/rag/` are reviewed knowledge base documents. They are read-only by default unless the user explicitly approves an update.

## 5. Skill Rule

Reusable task procedures live under `docs/agent/skills/`.

Before creating or updating a Skill:

1. Check `docs/agent/skills/SkillIndex.md`.
2. Prefer patching or extending an existing umbrella Skill.
3. Avoid one-session-one-skill pollution.
4. Update the Skill index after approved changes.

## 6. Memory Rule

Memory updates require explicit user approval unless a project-specific governance policy enables automatic candidate generation. Automatic candidates must not directly update active memory.

## 7. Workflow Rule

The generic Harness vault stores workflow templates under `templates/**`. Real project task histories belong to the target project's `docs/project/workflow/` directory.

## 8. Template Rule

All reusable source templates, including document templates, workflow templates, policy templates, report templates, memory templates, skill templates and future prompt templates, belong under `templates/**`.

Other directories may document how templates are used, but should not keep duplicate reusable template bodies.

## 9. Governance Rule

Scheduled governance defaults to dry-run and report-first. Long-term assets must not be physically deleted by automation.

## 10. Completion Rule

A task is not complete until its acceptance criteria are checked and the result is reported clearly.

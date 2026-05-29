# AGENTS.md

## 1. Harness Entry Contract

Any agent working inside the Harness vault must read:

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/PLANS.md`
4. Task-specific documents listed in `docs/INDEX.md`

## 2. Source of Truth Rule

- Harness source documents live under `docs/**/*.md`.
- Obsidian configuration under `.obsidian/` is an editing aid, not a Harness fact source.
- Generated reports under `docs/reports/` are evidence, not final source documents.

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

The generic Harness vault stores workflow templates. Real project task histories belong to the target project's `docs/project/workflow/` directory.

## 8. Governance Rule

Scheduled governance defaults to dry-run and report-first. Long-term assets must not be physically deleted by automation.

## 9. Completion Rule

A task is not complete until its acceptance criteria are checked and the result is reported clearly.

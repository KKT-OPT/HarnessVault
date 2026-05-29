# AGENTS.md

This repository stores the HarnessVault documentation system.

## Harness Vault Root

The Harness vault root is:

```text
harness/
```

Do not treat the repository root as the Harness document root. The repository root only contains GitHub maintenance files and this forwarding entry contract.

## Required Reading Order

Any agent working in this repository must read:

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `harness/docs/INDEX.md`
4. `harness/docs/PLANS.md`
5. Task-specific documents listed in `harness/docs/INDEX.md`

## Hard Constraints

- Do not treat `.obsidian/` workspace state or plugin runtime code as Harness source documents.
- Do not update Skill, Memory, RAG, or Project Facts without checking the governance rules first.
- Do not mark a task complete before checking acceptance criteria.
- For architecture-level changes, prefer a temporary branch and PR rather than direct changes to `main`.

## Current Core Document

- `harness/docs/HarnessEngineering.md`

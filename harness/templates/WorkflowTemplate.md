---
documentName: templates/WorkflowTemplate.md
templateName: WorkflowTemplate
templateTarget: docs/project/workflow/<% tp.date.now("YYYYMMDD") %>-<task-name>.md
templateEngine: obsidian-templater
templatePurpose: 生成项目 workflow 文档。
title: Workflow Template
aliases:
  - WorkflowTemplate
tags:
  - workflow
  - harness
  - template
version: v0.2.0
createdAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
updatedAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
status: draft
type: template
purpose: 提供项目 workflow 文档生成模板。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[ProjectIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter:
---

# <Task Name>

## 1. Metadata

| Field | Value |
|---|---|
| Date | <% tp.date.now("YYYY-MM-DD") %> |
| Stage |  |
| Task |  |
| Owner | human |
| Agent |  |
| Status | draft |

## 2. Final Goal

## 3. Current Task

## 4. Context Loaded

## 5. Execution Plan

## 6. User Approval

## 7. Execution Trace

## 8. Acceptance Criteria

## 9. Validation Result

## 10. Promotion Candidates

### Memory Candidates

### Skill Candidates

### RAG Candidates

### Project Fact Candidates

## 11. Open Questions

## 12. Final Output

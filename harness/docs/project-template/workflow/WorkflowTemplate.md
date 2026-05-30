---
documentName: docs/project-template/workflow/WorkflowTemplate.md
title: Project Workflow Template
aliases:
  - WorkflowTemplate
  - Project Workflow Template
  - 项目任务工作流模板
tags:
  - harness
  - project-template
  - workflow
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的真实项目任务过程、验收和 promotion candidates 记录模板。
scope: Project Template workflow。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
  - "[[Repository]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Project Workflow Template

## 1. Metadata

| Field | Value |
|---|---|
| Project | `<project-name>` |
| Workflow ID | `<YYYYMMDD-stage-task>` |
| Stage | `<stage>` |
| Task | `<task-name>` |
| Owner | `<owner>` |
| Agent | `<agent-name>` |
| Status | `draft / active / closed / archived` |
| Created At | `<created-at>` |
| Updated At | `<updated-at>` |

## 2. Final Goal

```text
<final-goal>
```

## 3. Current Task

```text
<current-task>
```

## 4. Context Loaded

记录本轮任务读取的文档、代码、报告和外部资料。

| 类型 | 路径 / 来源 | 用途 |
|---|---|---|
| Harness Entry | `AGENTS.md` | `<reason>` |
| Index | `docs/INDEX.md` | `<reason>` |
| Plan | `docs/PLANS.md` | `<reason>` |
| Project Fact | `<path>` | `<reason>` |
| Code | `<path>` | `<reason>` |
| Report | `<path>` | `<reason>` |

## 5. Execution Plan

1. `<step-1>`
2. `<step-2>`
3. `<step-3>`

## 6. User Approval

| Item | Status | Notes |
|---|---|---|
| Plan approved | `<yes/no/not-required>` | `<notes>` |
| Write permission | `<yes/no/read-only>` | `<notes>` |
| Submit permission | `<yes/no>` | `<notes>` |
| Main branch modification | `forbidden by default` | `<notes>` |

## 7. Execution Trace

记录关键执行过程，不粘贴大段日志。

| Step | Result | Evidence |
|---|---|---|
| `<step>` | `<result>` | `<evidence>` |

## 8. Acceptance Criteria

1. `<acceptance-criterion-1>`
2. `<acceptance-criterion-2>`
3. `<acceptance-criterion-3>`

## 9. Validation Result

| Criterion | Result | Evidence |
|---|---|---|
| `<criterion>` | `pass/fail/partial` | `<evidence>` |

## 10. Failure / Repair Loop

如果未通过验收，记录：

1. 未通过原因；
2. 修复计划；
3. 重新执行结果；
4. 再次验收结果。

## 11. Promotion Candidates

Workflow 只能产生候选，不得直接写入长期资产。

### 11.1 Memory Candidates

| Candidate | Reason | Evidence | Status |
|---|---|---|---|
| `<candidate>` | `<reason>` | `<evidence>` | `candidate` |

### 11.2 Skill Candidates

| Candidate | Reason | Existing Skill Checked | Status |
|---|---|---|---|
| `<candidate>` | `<reason>` | `<yes/no>` | `candidate` |

### 11.3 RAG Candidates

| Candidate | Source | Review Required | Status |
|---|---|---|---|
| `<candidate>` | `<source>` | `<yes/no>` | `candidate` |

### 11.4 Project Fact Candidates

| Candidate | Target Document | Evidence | Status |
|---|---|---|---|
| `<candidate>` | `<target-doc>` | `<evidence>` | `candidate` |

## 12. Open Questions

1. `<open-question-1>`
2. `<open-question-2>`
3. `<open-question-3>`

## 13. Final Output

```text
<final-output-summary>
```

## 14. Close Rule

任务关闭前必须确认：

1. 是否完成验收标准；
2. 是否更新相关 index；
3. 是否产生 promotion candidates；
4. 是否需要生成治理报告；
5. 是否存在未解决风险。

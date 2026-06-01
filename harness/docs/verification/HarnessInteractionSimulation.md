---
documentName: docs/verification/HarnessInteractionSimulation.md
title: Harness Interaction Simulation
aliases:
  - HarnessInteractionSimulation
  - Agent Harness Simulation
  - 智能体交互模拟
tags:
  - harness
  - verification
  - simulation
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: template
purpose: 模拟智能体如何基于 HarnessVault 入口、索引和治理规则完成一次任务闭环。
scope: HarnessVault verification。
prerequisites:
  - docs/verification/HarnessValidationPlan.md
relatedDocuments:
  - "[[HarnessValidationPlan]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[RAGIndex]]"
  - "[[ProjectIndex]]"
  - "[[ReadinessCheckPolicy]]"
  - "[[TraceSchema]]"
  - "[[RegressionPolicy]]"
  - "[[KnowledgeIntakePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Interaction Simulation

## 1. 目的

本文档用于模拟一个智能体如何在不依赖特定 runtime 的情况下，通过 HarnessVault 的入口和索引完成一次受控任务闭环。

该模拟只使用占位输入，不包含真实用户知识和具体项目事实。

## 2. 模拟用户 Prompt

```text
我准备基于 Harness 模板启动一个新项目。请你读取项目入口文档，判断需要哪些项目事实、哪些知识应进入 RAG，哪些经验应进入 Skill 或 Memory，并给出执行计划、验收标准和后续治理记录。
```

## 3. 智能体读取路径

智能体应按顺序读取：

```text
AGENTS.md
harness/AGENTS.md
docs/INDEX.md
docs/PLANS.md
docs/project-template/ProjectIndex.md
docs/rag/RAGIndex.md
docs/rag/KnowledgeIntakePolicy.md
docs/verification/ReadinessCheckPolicy.md
docs/observability/TraceSchema.md
docs/verification/RegressionPolicy.md
docs/reports/README.md
```

## 4. 预期判断

智能体应判断：

| 输入类型 | 目标位置 | 说明 |
|---|---|---|
| 项目需求、架构、仓库、接口、数据、测试 | `docs/project/` | 具体项目事实，不进入通用 HarnessVault |
| 领域知识、规范、外部资料 | `docs/rag/intake/` | 候选区，审查后进入 RAG |
| 可复用流程 | Skill Candidate | 审查后进入 Skill |
| 长期偏好或约束 | Memory Candidate | 审查后进入 Memory |
| 当前任务过程 | Workflow / Report | 不直接进入 RAG / Skill / Memory |

## 5. Readiness Check 示例

| 检查项 | 结果 | 说明 |
|---|---|---|
| task | pass | 用户目标是启动新项目 Harness 实例 |
| scope | partial | 需要用户明确项目名称、仓库、技术栈和初始需求 |
| context | pass | 已通过 INDEX 和 ProjectIndex 找到模板入口 |
| permission | partial | 尚未授权写入具体项目仓库 |
| validation | partial | 需要用户确认验收标准 |
| safety | pass | 当前只使用通用模板，不写入真实知识 |

## 6. 执行计划示例

1. 读取 Harness 入口和计划；
2. 读取 Project Template；
3. 识别缺失的项目事实；
4. 读取 RAG intake 规则；
5. 将用户输入知识路由为 candidate；
6. 给出项目实例化计划；
7. 输出验收标准；
8. 生成 trace 摘要和 report candidate。

## 7. 验收标准示例

1. 已列出启动项目所需项目事实；
2. 已区分 RAG、Project Facts、Skill、Memory、Workflow、Report；
3. 未把 intake 内容当作事实源；
4. 未把具体项目内容写入通用 HarnessVault；
5. 已给出用户下一步需要提供的信息；
6. 已给出 trace / report / candidate 记录建议。

## 8. Trace 摘要示例

| 字段 | 值 |
|---|---|
| traceId | `<trace-id>` |
| taskId | `<task-id>` |
| runtime | `<runtime>` |
| status | `partial` |
| entryDocs | `AGENTS.md`, `INDEX.md`, `PLANS.md` |
| policyDocs | `KnowledgeIntakePolicy`, `ReadinessCheckPolicy` |
| result | `需要用户补充项目事实后才能实例化` |

## 9. Regression 示例

如果用户补充项目事实后，智能体应重新检查：

1. ProjectIndex 是否需要更新；
2. Project Facts 是否进入真实项目而非通用 HarnessVault；
3. RAG 候选是否仍处于 intake；
4. Memory / Skill 是否仍为 candidate；
5. 是否需要生成报告。

## 10. 失败归因示例

| 失败 | 归因 | 修复 |
|---|---|---|
| 智能体直接把项目事实写入通用 HarnessVault | governance / project-fact boundary failure | 回滚，改写入 Project Harness Instance |
| 智能体把 intake 当作事实源 | RAG boundary failure | 重新读取 [[KnowledgeIntakePolicy]] |
| 智能体没有执行 readiness | verification failure | 执行 [[ReadinessCheckPolicy]] |
| 智能体没有生成 trace | observability failure | 按 [[TraceSchema]] 补摘要 |

## 11. 模拟结论

如果智能体能按照本模拟完成读取、判断、计划、验收、trace、regression 和 candidate routing，则说明 HarnessVault 已具备作为通用 agent-facing 文档控制层的基本可用性。

---
documentName: docs/rag/KnowledgeIntakePolicy.md
title: Knowledge Intake Policy
aliases:
  - KnowledgeIntakePolicy
  - 知识引入规则
  - Knowledge Intake
tags:
  - harness
  - rag
  - knowledge-intake
  - governance
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义用户知识、外部资料、领域知识、项目事实和候选知识进入 Harness 的通用引入路径。
scope: HarnessVault RAG and knowledge intake。
prerequisites:
  - docs/rag/KnowledgeBasePolicy.md
  - docs/governance/KnowledgePromotionPolicy.md
relatedDocuments:
  - "[[RAGIndex]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[KnowledgePromotionPolicy]]"
  - "[[MemoryPolicy]]"
  - "[[SkillPolicy]]"
  - "[[ProjectIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Knowledge Intake Policy

## 1. 目的

本文档定义知识进入 Harness 的通用引入路径，使用户提供的知识、外部资料、领域知识、项目事实、操作经验和任务证据能够被暂存、审查、分类、索引和晋升。

当前 HarnessVault 是通用模板仓库，不保存真实用户知识或具体项目内容。本规则只定义如何引入知识。

## 2. 知识类型与目标资产

| 输入内容 | 默认目标 | 说明 |
|---|---|---|
| 稳定领域知识 | RAG Candidate | 审查后进入 `docs/rag/domain/` |
| 通用规范知识 | RAG Candidate | 审查后进入 `docs/rag/standard/` |
| 项目正式事实 | Project Fact Candidate | 真实项目中进入 `docs/project/` |
| 可复用操作流程 | Skill Candidate | 审查后进入 Skill |
| 长期偏好或约束 | Memory Candidate | 审查后进入 Memory |
| 一次性任务过程 | Workflow / Report | 不直接进入 RAG、Skill、Memory |
| 外部工具输出 | Intake Candidate | 审查后再路由 |

## 3. Intake 暂存区

所有未审查知识应先进入：

```text
docs/rag/intake/
```

intake 是候选区，不是事实源。智能体不得把 intake 内容直接当作长期知识引用。

## 4. 引入流程

标准流程：

```text
用户输入 / 外部资料 / 任务证据
→ KnowledgeIntakeTemplate
→ 来源与风险标注
→ 分类路由
→ 人工审查
→ candidate
→ promotion
→ 目标资产
```

## 5. 用户知识引入规则

用户可以通过以下方式输入知识：

1. 直接提供 Markdown 文档；
2. 上传 PDF、网页摘要、笔记或资料；
3. 在对话中说明长期偏好、项目背景或领域知识；
4. 提供具体项目 facts；
5. 提供可复用操作经验。

智能体应先判断该输入属于：

1. 通用知识；
2. 项目事实；
3. 用户偏好；
4. 任务证据；
5. 操作流程；
6. 外部资料候选。

不得直接写入 active RAG、active Memory 或 active Skill。

## 6. 索引与关键词规则

为了让智能体后续能通过索引或关键词找到用户输入的知识，候选知识必须包含：

1. `title`；
2. `aliases`；
3. `tags`；
4. `sourceType`；
5. `targetAsset`；
6. `keywords`；
7. `relatedDocuments`；
8. `reviewStatus`。

关键词应覆盖：

1. 用户原始表述；
2. 标准术语；
3. 同义词；
4. 项目代号，若属于具体项目；
5. 领域关键词。

## 7. 审查规则

知识晋升前必须检查：

1. 来源是否明确；
2. 是否含敏感信息；
3. 是否是临时任务内容；
4. 是否与现有事实冲突；
5. 是否应进入 Project Facts 而不是 RAG；
6. 是否应进入 Skill 而不是 RAG；
7. 是否应进入 Memory 而不是 RAG；
8. 是否已有同类知识。

## 8. 禁止事项

禁止：

1. 将 intake 内容直接作为事实源；
2. 将用户知识直接写入通用 HarnessVault；
3. 将具体项目 facts 写入通用 RAG；
4. 将未审查外部资料写入 RAG；
5. 将大段日志写入 Memory；
6. 将一次性任务经验写成 Skill；
7. 将敏感信息写入任何长期资产。

## 9. 关联文档

- [[RAGIndex]]
- [[KnowledgeBasePolicy]]
- [[KnowledgePromotionPolicy]]
- [[MemoryPolicy]]
- [[SkillPolicy]]
- [[ProjectIndex]]

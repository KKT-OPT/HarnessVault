---
documentName: docs/rag/KnowledgeBasePolicy.md
title: Knowledge Base Policy
aliases:
  - KnowledgeBasePolicy
  - 知识库治理规则
  - RAG 治理规则
tags:
  - harness
  - rag
  - policy
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness RAG 知识库的来源、准入、审查、更新和只读规则。
scope: HarnessVault RAG。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/rag/RAGIndex.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[RAGIndex]]"
  - "[[KnowledgePromotionPolicy]]"
  - "[[IndexMaintenancePolicy]]"
  - "[[ScheduledGovernance]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Knowledge Base Policy

## 1. 目的

本文档定义 HarnessVault RAG 知识库的来源、准入、审查、更新和只读规则，确保知识库内容稳定、可追溯、可复用，并与任务历史、Memory、Skill 和 Project Facts 保持边界清晰。

## 2. RAG 定义

RAG Knowledge Base 用于保存稳定、经过审查、可检索的知识内容。

RAG 适合保存：

1. 通用文档规范；
2. 编码规范；
3. 测试规范；
4. 审查规范；
5. 领域知识；
6. 方法论；
7. 经过审查的外部资料摘要；
8. 可跨项目复用的稳定知识。

RAG 不保存：

1. 真实项目任务历史；
2. 一次性 workflow；
3. 用户偏好；
4. 可执行操作流程；
5. 项目正式事实；
6. 临时调试结论；
7. 未审查的 NotebookLM 或网页摘要。

## 3. RAG 与其他资产边界

| 内容类型 | 应进入 |
|---|---|
| 稳定领域知识 | RAG |
| 可复用执行流程 | Skill |
| 用户长期偏好 | Memory |
| 项目正式事实 | Project Facts |
| 一次任务过程 | Workflow |
| 检查结果和建议 | Report |
| 外部资料初筛摘要 | Candidate，审查后才可进入 RAG |

## 4. 知识来源

允许来源：

1. 人工整理的稳定知识；
2. 已审查的官方文档；
3. 已审查的标准、论文、规范；
4. 已审查的项目经验总结；
5. 经人工确认的 NotebookLM / 外部工具输出；
6. 从 Workflow、Memory、Skill 晋升而来的稳定知识。

禁止直接作为 RAG 来源：

1. 未验证网页摘要；
2. 原始日志；
3. 一次性对话结论；
4. 模型猜测；
5. 未确认的项目事实；
6. 未授权的私有资料。

## 5. 准入标准

内容进入 RAG 前必须满足：

1. 来源明确；
2. 有审查人或 owner；
3. 内容稳定；
4. 与具体项目任务历史解耦；
5. 不与 Project Facts 冲突；
6. 适合被多个任务复用；
7. 有 `reviewAfter`；
8. 已加入 [[RAGIndex]] 或对应分区索引。

## 6. 更新规则

更新 RAG 文档前必须检查：

1. 是否已有同类知识；
2. 是否应更新原文档而不是新增文档；
3. 是否需要标记旧内容为 stale；
4. 是否影响 Skill、Memory 或 Project Facts；
5. 是否需要生成治理报告。

默认不允许智能体无审查地修改 RAG 正文。

## 7. 只读规则

`docs/rag/` 默认只读。

允许智能体做：

1. 查询；
2. 摘要；
3. 提出更新建议；
4. 生成 RAG candidate；
5. 检查过期和冲突。

默认不允许智能体做：

1. 直接写入新知识；
2. 删除知识；
3. 用未审查外部资料覆盖原文；
4. 把一次性任务结论写入 RAG；
5. 把 Project Facts 写入 RAG。

## 8. 外部工具输出规则

NotebookLM、网页搜索、PDF 摘要、Obsidian 临时笔记等外部输出只能作为候选资料。

进入 RAG 前必须：

1. 标注来源；
2. 人工审查；
3. 删除不稳定或无法验证内容；
4. 转写为 Harness Markdown 文档；
5. 加入 frontmatter；
6. 更新 [[RAGIndex]]。

## 9. 冲突处理

当 RAG 与 Project Facts 冲突时，以 Project Facts 为准。

优先级：

```text
用户当前明确指令
> Project Facts
> active RAG
> Skill / Memory
> reports
> candidates
```

冲突无法解决时，必须报告冲突，不得静默覆盖。

## 10. 审查与过期

RAG 文档必须设置 `reviewAfter`。

过期处理：

1. 到期未审查，标记 stale；
2. 被替代，标记 deprecated；
3. 历史保留，标记 archived；
4. 不再作为默认检索推荐。

## 11. 关联文档

- [[HarnessEngineering]]
- [[RAGIndex]]
- [[KnowledgePromotionPolicy]]
- [[IndexMaintenancePolicy]]
- [[ScheduledGovernance]]

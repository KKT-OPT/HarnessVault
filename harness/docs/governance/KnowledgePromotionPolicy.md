---
documentName: docs/governance/KnowledgePromotionPolicy.md
title: Knowledge Promotion Policy
aliases:
  - KnowledgePromotionPolicy
  - 知识晋升规则
tags:
  - harness
  - governance
  - rag
  - promotion
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Workflow、Memory、Skill、RAG、Project Facts 之间的晋升路径和审查规则。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/ArtifactLifecycle.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[ArtifactLifecycle]]"
  - "[[KnowledgeBasePolicy]]"
  - "[[MemoryPolicy]]"
  - "[[SkillPolicy]]"
  - "[[WorkflowTemplate]]"
  - "[[RAGIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Knowledge Promotion Policy

## 1. 目的

本文档定义 Workflow、Memory、Skill、RAG、Project Facts 之间的晋升路径和审查规则，防止一次性任务过程、未验证经验或外部资料直接污染长期资产。

## 2. 基本原则

知识晋升遵循：

1. evidence first；
2. candidate first；
3. review before promotion；
4. no direct promotion from workflow to active asset；
5. no silent overwrite；
6. no automatic promotion without approval。

## 3. 资产边界

| 来源 | 可晋升目标 | 说明 |
|---|---|---|
| Workflow | Memory Candidate / Skill Candidate / RAG Candidate / Project Fact Candidate | Workflow 只能产生候选 |
| Memory Candidate | active Memory / Project Fact / Skill Candidate | 简短稳定事实或偏好可进入 Memory |
| Skill Candidate | active Skill | 可复用流程可进入 Skill |
| RAG Candidate | active RAG | 稳定知识经审查后进入 RAG |
| Report | Candidate / 正式文档修复项 | Report 只提供证据和建议 |
| Project Fact Candidate | Project Facts | 项目正式事实必须写入 project 文档 |

## 4. 候选类型

### 4.1 Memory Candidate

适用于：

1. 用户长期偏好；
2. 项目长期约束；
3. 智能体操作注意事项；
4. 简短稳定经验。

不得包含大段日志、代码、临时路径或一次性状态。

### 4.2 Skill Candidate

适用于：

1. 重复出现的可复用流程；
2. 有明确触发条件的操作步骤；
3. 可验证的执行清单；
4. 可沉淀为模板或脚本的流程。

不得为一次任务单独创建 one-session-one-skill。

### 4.3 RAG Candidate

适用于：

1. 稳定领域知识；
2. 文档、代码、测试、审查规范；
3. 经审查的外部资料摘要；
4. 可跨项目复用的方法论。

不得包含项目正式事实或未审查外部资料。

### 4.4 Project Fact Candidate

适用于：

1. 需求事实；
2. 架构事实；
3. 仓库事实；
4. 接口事实；
5. 数据事实；
6. 测试事实。

必须写入真实项目的 `docs/project/`，不能写入通用 Harness Template。

## 5. 晋升流程

标准流程：

```text
任务证据
→ candidate
→ 审查
→ 选择目标资产
→ 更新目标文档
→ 更新对应 index
→ 记录来源
```

禁止流程：

```text
workflow → active Memory
workflow → active Skill
workflow → active RAG
report → Project Fact
external summary → active RAG
```

## 6. 审查标准

候选晋升前必须检查：

1. 是否稳定；
2. 是否可复用；
3. 是否有证据；
4. 是否已有同类资产；
5. 是否应更新已有文档而不是新增；
6. 是否与 Project Facts 冲突；
7. 是否需要更新 index；
8. 是否需要报告记录。

## 7. 目标选择规则

| 判断问题 | 目标 |
|---|---|
| 是否是项目正式事实？ | Project Facts |
| 是否是可复用流程？ | Skill |
| 是否是稳定领域知识？ | RAG |
| 是否是简短长期偏好或约束？ | Memory |
| 是否是一次性任务过程？ | Workflow |
| 是否是检查结果或建议？ | Report |

## 8. 拒绝晋升规则

候选应拒绝晋升，当：

1. 只适用于一次任务；
2. 没有证据；
3. 与现有事实冲突且未解决；
4. 已经存在于正式文档；
5. 内容过大，不适合目标资产；
6. 来源不可信；
7. 用户未批准。

## 9. 记录要求

晋升成功后必须记录：

1. 来源；
2. 审查人或 owner；
3. 目标文档；
4. 更新日期；
5. 对应 index；
6. 是否有相关报告。

## 10. 关联文档

- [[HarnessEngineering]]
- [[ArtifactLifecycle]]
- [[KnowledgeBasePolicy]]
- [[MemoryPolicy]]
- [[SkillPolicy]]
- [[WorkflowTemplate]]
- [[RAGIndex]]

---
documentName: docs/observability/FailureAttributionPolicy.md
title: Failure Attribution Policy
aliases:
  - FailureAttributionPolicy
  - Failure Attribution
  - 失败归因规则
tags:
  - harness
  - observability
  - failure-attribution
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 agent 任务失败后的归因维度、证据记录和修复闭环。
scope: HarnessVault observability。
prerequisites:
  - docs/observability/TraceSchema.md
relatedDocuments:
  - "[[ObservabilityIndex]]"
  - "[[TraceSchema]]"
  - "[[VerificationIndex]]"
  - "[[RegressionPolicy]]"
  - "[[RuntimeBoundaryPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Failure Attribution Policy

## 1. 目的

本文档定义 agent 任务失败后的归因维度、证据记录和修复闭环。目标是避免把所有失败简单归因于模型能力不足，而是区分模型、工具、上下文、生命周期、权限、验证、文档事实和用户输入等不同失败来源。

## 2. 失败归因维度

| 维度 | 含义 | 示例 |
|---|---|---|
| model | 模型理解、推理或生成失败 | 误解任务、错误推理 |
| context | 上下文加载、压缩或污染失败 | 未读关键文档、加载过多无关内容 |
| tool | 工具调用、接口、协议或结果解释失败 | 工具参数错误、工具返回不可用 |
| execution | runtime、sandbox、命令或文件操作失败 | 命令失败、权限不足 |
| lifecycle | 计划、阶段、状态、重试或任务闭环失败 | 跳过计划审批、未复测 |
| verification | readiness、验收或回归检查失败 | 没有运行必要测试 |
| governance | 权限、安全、清理、晋升或索引治理失败 | 未授权写入、未更新 index |
| project-fact | 项目事实源不完整或冲突 | 架构文档过期 |
| user-input | 用户任务口径不清或需求变化 | 验收标准缺失 |
| external | 外部依赖、网络、第三方服务失败 | API 不可用 |

## 3. 归因流程

```text
失败事件
→ 收集 trace 摘要
→ 定位失败阶段
→ 选择归因维度
→ 记录证据
→ 判断是否可重试
→ 制定修复动作
→ 进入 regression / acceptance 检查
```

## 4. 证据要求

归因必须包含：

1. 失败发生阶段；
2. 失败操作或文件；
3. 简短错误摘要；
4. 相关 policy 或验收标准；
5. 是否可复现；
6. 是否可重试；
7. 修复建议。

不得粘贴大段日志或敏感信息。

## 5. 常见失败与处理

| 失败类型 | 优先检查 | 修复方向 |
|---|---|---|
| 未读关键文档 | [[ContextLoadingPolicy]] | 补充上下文加载规则 |
| 未更新索引 | [[IndexMaintenancePolicy]] | 更新对应 index |
| 未授权写入 | [[RuntimeBoundaryPolicy]] / [[SecurityGovernance]] | 重新确认权限 |
| 验收失败 | [[ReadinessCheckPolicy]] / [[RegressionPolicy]] | 补充验证或修复 |
| 经验污染 | [[MemoryPolicy]] / [[SkillPolicy]] | 改为 candidate |
| RAG 污染 | [[KnowledgeBasePolicy]] | 退回候选审查 |

## 6. 输出位置

失败归因可以记录在：

1. workflow；
2. trace 摘要；
3. governance report；
4. index check report；
5. regression report。

默认不直接写入 Memory 或 Skill。

## 7. 关联文档

- [[ObservabilityIndex]]
- [[TraceSchema]]
- [[VerificationIndex]]
- [[RegressionPolicy]]
- [[RuntimeBoundaryPolicy]]

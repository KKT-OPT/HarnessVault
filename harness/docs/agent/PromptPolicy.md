---
documentName: docs/agent/PromptPolicy.md
title: Prompt Policy
aliases:
  - PromptPolicy
  - Prompt Policy
  - 提示词规则
tags:
  - harness
  - agent
  - prompt
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-02 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 任务 prompt 的结构、约束和输出格式规则。
scope: HarnessVault agent policy。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[AgentIndex]]"
  - "[[TemplatesIndex]]"
  - "[[ComplexTaskPromptTemplate]]"
  - "[[DocumentAudiencePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Prompt Policy

## 1. 目的

本文档定义 Harness 任务 prompt 的结构、约束和输出格式规则。

复杂任务 prompt 应使用明确分区，避免把任务目标、上下文、反馈、数据和约束混在一起。

## 2. Prompt 入口规则

任何复杂任务 prompt 应要求智能体优先读取：

1. `AGENTS.md`；
2. [[INDEX]]；
3. [[PLANS]]；
4. prompt 中指定的任务相关文档。

## 3. Prompt 结构

复杂任务 prompt 应至少包含：

1. final goal；
2. previous context；
3. current feedback；
4. current task；
5. inspection scope；
6. constraints；
7. acceptance criteria；
8. output format。

推荐使用 [[ComplexTaskPromptTemplate]]。

## 4. XML-like block 使用规则

可以使用 XML-like block 隔离 instruction 和 data，例如：

```xml
<final_goal>...</final_goal>
<constraints>...</constraints>
<acceptance_criteria>...</acceptance_criteria>
```

这不是机器强制 schema，而是提高智能体解析稳定性的结构化 prompt 约定。

## 5. 禁止事项

1. 不要把真实 secrets 写入 prompt 模板。
2. 不要在通用 prompt 模板中写入具体项目事实。
3. 不要让 prompt 绕过 `AGENTS.md` 和 [[INDEX]]。
4. 不要把未审查 intake 内容作为事实源。

## 6. 关联文档

- [[AgentIndex]]
- [[TemplatesIndex]]
- [[ComplexTaskPromptTemplate]]
- [[DocumentAudiencePolicy]]

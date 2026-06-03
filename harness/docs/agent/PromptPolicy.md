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
version: v0.2.1
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
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

## 3. 复杂任务 Prompt 使用场景

以下任务应优先使用 [[ComplexTaskPromptTemplate]]：

1. 跨多个 Harness 文档或架构层的任务；
2. 需要承接 previous context 或用户 feedback 的任务；
3. 修改 AGENTS、INDEX、PLANS、policy、template、manifest 或治理边界的任务；
4. 有明确 constraints、acceptance criteria 或 output format 的任务；
5. 需要说明是否产生 Memory、Skill、RAG、Project Fact candidate 或治理报告的任务。

简单查询、单点说明或无治理影响的小修订不强制套用完整模板，但仍必须遵守入口读取顺序。

## 4. Prompt 必备字段

复杂任务 prompt 应至少包含：

1. entry contract；
2. final goal；
3. previous context；
4. feedback；
5. task；
6. inspection scope；
7. constraints；
8. acceptance criteria；
9. output format；
10. governance notes。

推荐使用 [[ComplexTaskPromptTemplate]]。

## 5. XML-like block 使用规则

可以使用 XML-like block 隔离 instruction 和 data，例如：

```xml
<entry_contract>...</entry_contract>
<final_goal>...</final_goal>
<constraints>...</constraints>
<acceptance_criteria>...</acceptance_criteria>
<governance_notes>...</governance_notes>
```

这不是强制 schema，也不是替代 Markdown 事实源的格式；它只是提高智能体解析稳定性的结构化 prompt 约定。

## 6. 禁止事项

1. 不要把真实 secrets 写入 prompt 模板。
2. 不要在通用 prompt 模板中写入具体项目事实。
3. 不要让 prompt 绕过 `AGENTS.md` 和 [[INDEX]]。
4. 不要把未审查 intake 内容作为事实源。

## 7. 关联文档

- [[AgentIndex]]
- [[TemplatesIndex]]
- [[ComplexTaskPromptTemplate]]
- [[DocumentAudiencePolicy]]

---
documentName: docs/governance/DocumentAudiencePolicy.md
title: Document Audience Policy
aliases:
  - DocumentAudiencePolicy
  - Document Audience
  - 文档受众规则
tags:
  - harness
  - governance
  - documentation
  - agent
version: v0.2.0
createdAt: 2026-06-02 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 文档面向智能体、人类和机器检查的受众分类与格式策略。
scope: HarnessVault document audience governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
relatedDocuments:
  - "[[GovernanceIndex]]"
  - "[[HarnessEngineering]]"
  - "[[PromptPolicy]]"
  - "[[TemplatesIndex]]"
  - docs/agent/AgentContextManifest.yaml
  - "[[KnowledgeBaseConstructionWorkflow]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Document Audience Policy

## 1. 目的

本文档定义 Harness 文档面向智能体、人类和机器检查的受众分类与格式策略。

核心原则：不把所有文档都改成 XML 或 JSON。Markdown 仍是主要维护格式；只有 prompt、trace、report、knowledge card、manifest、sidecar 等需要严格解析的内容才采用更强结构。

## 2. 文档受众分类

| 类型 | 主要读者 | 主要格式 | 说明 |
|---|---|---|---|
| agent-readable | 智能体 | Markdown + frontmatter + 表格 + 明确列表 | 入口、索引、策略、执行规则 |
| human-readable | 人类 | Markdown 叙述 | 设计说明、背景、教程、决策说明 |
| hybrid | 人类 + 智能体 | Markdown + 结构化字段 | 计划、报告、知识卡片、项目事实 |
| machine-checkable | 脚本 / 工具 | JSON / JSONL / YAML / sidecar | usage、manifest、自检结果、可解析数据 |
| prompt-structured | 智能体 | XML-like block + Markdown | 复杂任务 prompt、约束、验收标准 |

`docs/agent/AgentContextManifest.yaml` 属于 machine-checkable 辅助入口。它用于表达稳定导航、默认 include / exclude、架构层到 index 文档的映射和 artifact boundary；它不替代 `AGENTS.md`、[[INDEX]]、[[PLANS]]、层级 index、policy 或模板等 Markdown 事实源，也不得包含真实项目事实或用户知识。

## 3. 智能体优先读取文档

智能体默认优先读取：

1. `AGENTS.md`；
2. [[INDEX]]；
3. [[PLANS]]；
4. 任务相关的层级 index；
5. 任务相关 policy；
6. 任务相关 template；
7. 当前 active report，若任务要求检查报告。

智能体默认不读取：

1. archived reports；
2. Obsidian workspace / graph；
3. plugin runtime code；
4. 大量原始资料正文；
5. 未审查 intake 内容作为事实源。

## 4. 人类主要阅读和补充文档

人类主要维护：

1. 设计文档，例如 [[HarnessEngineering]]；
2. 项目需求和架构；
3. 原始知识材料；
4. 审查意见；
5. 归档或晋升决策；
6. 需要语义判断的字段，例如适用范围、来源可信度、术语解释。

## 5. 结构化文档策略

### 5.1 保持 Markdown 的内容

以下内容优先保持 Markdown：

1. 架构设计；
2. 治理策略；
3. README / index；
4. 人类说明；
5. 知识解释；
6. 报告正文。

### 5.2 使用 XML-like block 的内容

以下内容可使用 XML-like block：

1. complex task prompt；
2. 用户输入拆分；
3. 约束和验收标准；
4. 需要明确隔离 instruction 和 data 的 prompt。

### 5.3 使用 JSON / YAML / sidecar 的内容

以下内容适合 JSON / YAML / sidecar：

1. manifest；
2. usage telemetry；
3. script output；
4. machine-checkable report summary；
5. index cache，若后续引入；
6. frontmatter。

## 6. 删除解释文字的边界

不建议为了智能体读取而删除所有解释文字。解释文字仍有价值：

1. 帮助人类审查；
2. 帮助新智能体理解设计意图；
3. 支持长期维护；
4. 降低误读风险。

但可以对以下文档减少冗余解释：

1. templates；
2. prompt；
3. manifest，例如 `docs/agent/AgentContextManifest.yaml`；
4. checklist；
5. self-check output。

## 7. 关联文档

- [[GovernanceIndex]]
- [[HarnessEngineering]]
- [[PromptPolicy]]
- [[TemplatesIndex]]
- [[KnowledgeBaseConstructionWorkflow]]
- `docs/agent/AgentContextManifest.yaml`

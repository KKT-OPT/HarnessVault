---
documentName: docs/verification/HarnessValidationCases.md
title: Harness Validation Cases
aliases:
  - HarnessValidationCases
  - Harness Validation Cases
  - Harness 验证用例
tags:
  - harness
  - verification
  - validation
  - cases
version: v0.1.0
createdAt: 2026-06-03 00:00:00.000 +08:00
updatedAt: 2026-06-03 00:00:00.000 +08:00
status: draft
type: checklist
purpose: 定义 P15 完成态验证可直接使用的通用 Harness 验证用例清单。
scope: HarnessVault verification cases。
prerequisites:
  - docs/verification/HarnessValidationPlan.md
  - docs/verification/HarnessInteractionSimulation.md
relatedDocuments:
  - "[[VerificationIndex]]"
  - "[[HarnessValidationPlan]]"
  - "[[HarnessInteractionSimulation]]"
  - "[[ReadinessCheckPolicy]]"
  - "[[RegressionPolicy]]"
  - "[[TraceSchema]]"
  - docs/agent/AgentContextManifest.yaml
  - "[[ComplexTaskPromptTemplate]]"
  - "[[RAGIndex]]"
  - "[[ProjectIndex]]"
  - "[[ReportsIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Validation Cases

## 1. 目的

本文档定义 P15 完成态验证可直接使用的通用验证用例清单。

这些用例只验证 HarnessVault 作为通用文档控制层是否可被任意智能体稳定读取、路由、判断和收口。用例不测试具体项目功能，不绑定具体 agent runtime，不写入真实用户知识，不写入具体项目事实。

## 2. 合并边界

可以合并到 main 的内容：

1. 本验证用例清单；
2. 指向本清单的 verification index、plan、simulation、PLANS 和架构说明；
3. 只包含占位输入、读取路径、预期行为、禁止行为和通过标准的通用规则。

不应合并到 main 的内容：

1. 实际 P15 验证运行报告；
2. 临时命令输出、terminal transcript、runtime trace 原文；
3. 真实用户知识、真实项目事实、真实仓库 URL、真实分支、真实构建命令；
4. 为某个 agent runtime 特制的私有测试配置；
5. 临时 scratch 文件、一次性脚本输出和未审查外部资料。

如需保存正式 P15 验证结果，应在 P15 阶段生成 report-first 的治理报告，并经人工审查后再决定是否合并。

## 3. 用例字段

每个用例必须包含：

1. 输入；
2. 读取路径；
3. 预期行为；
4. 禁止行为；
5. 通过标准。

## 4. 用例 1：复杂任务 Prompt 读取路径验证

### 输入

```text
<user asks an agent to continue a multi-step Harness task with previous context, explicit constraints, and acceptance criteria>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `docs/agent/AgentIndex.md`
6. `docs/agent/PromptPolicy.md`
7. `templates/README.md`
8. `templates/ComplexTaskPromptTemplate.md`
9. 任务相关 policy / template / index

### 预期行为

智能体应：

1. 说明该任务属于复杂任务；
2. 使用 [[ComplexTaskPromptTemplate]] 的结构理解 entry contract、final goal、previous context、feedback、task、inspection scope、constraints、acceptance criteria、output format 和 governance notes；
3. 先读取入口、索引和计划，再读取任务相关文档；
4. 在执行前说明验收标准和禁止事项；
5. 只在用户授权范围内修改文件。

### 禁止行为

智能体不得：

1. 跳过 `AGENTS.md`、[[INDEX]] 或 [[PLANS]]；
2. 只凭 previous context 判断当前任务；
3. 把 XML-like block 当作强制 schema 或替代 Markdown 事实源；
4. 在 prompt 模板中写入真实用户知识或具体项目事实；
5. 把复杂任务 prompt 复制到非 `templates/**` 作为新的模板源。

### 通过标准

1. 能定位 [[PromptPolicy]] 和 [[ComplexTaskPromptTemplate]]；
2. 能列出复杂任务 prompt 的 10 个必备字段；
3. 能说明 XML-like block 是 prompt 结构约定，不是强制 schema；
4. 能确认 prompt 模板仍位于 `templates/**`；
5. 不产生真实项目事实、真实用户知识或 runtime 专属配置。

## 5. 用例 2：原始资料进入知识库候选路径验证

### 输入

```text
<user provides a placeholder external source summary and asks whether it can become reusable knowledge>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `docs/rag/RAGIndex.md`
6. `docs/rag/KnowledgeIntakePolicy.md`
7. `docs/rag/KnowledgeBaseConstructionWorkflow.md`
8. `docs/rag/intake/README.md`
9. `docs/rag/intake/raw/README.md`
10. `docs/rag/intake/enriched/README.md`
11. `templates/RawKnowledgeMaterialTemplate.md`
12. `templates/EffectiveKnowledgeTemplate.md`

### 预期行为

智能体应：

1. 将输入判断为候选资料，而不是 active RAG；
2. 路由到 raw material candidate，再进入 semantic enrichment candidate；
3. 说明 raw / enriched 均不是事实源，不进入默认上下文；
4. 指向 [[RawKnowledgeMaterialTemplate]] 和 [[EffectiveKnowledgeTemplate]]；
5. 说明需要人工审查后才能 promotion 到 `docs/rag/domain/` 或 `docs/rag/standard/`。

### 禁止行为

智能体不得：

1. 保存大段原文或完整外部资料正文；
2. 未经审查直接写入 active RAG；
3. 把 intake、raw 或 enriched 内容当作事实源；
4. 将具体项目事实写入通用 HarnessVault；
5. 写入真实用户知识、敏感信息或私有资料正文。

### 通过标准

1. 能区分 raw、enriched、effective knowledge 和 review / promotion；
2. 能说明候选分区不是事实源；
3. 能给出候选文档应使用的模板；
4. 能说明 active RAG 的人工审查门槛；
5. 不创建真实知识正文。

## 6. 用例 3：Project Template 实例化路径验证

### 输入

```text
<user asks to create a project harness instance for <project-name> with placeholder repository and placeholder requirements>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `docs/project-template/ProjectIndex.md`
6. `docs/project-template/README.md`
7. `templates/README.md`
8. `templates/WorkflowTemplate.md`
9. 需要时读取 `docs/project-template/**/README.md`

### 预期行为

智能体应：

1. 说明通用模板路径是 `docs/project-template/`；
2. 说明真实项目实例路径应是目标项目中的 `docs/project/`；
3. 使用 `<project-name>`、`<repository-url>`、`<main-branch>` 等占位变量；
4. 列出需要用户提供的真实项目事实；
5. 说明实例化应发生在具体项目 Harness Instance 中，而不是通用 HarnessVault。

### 禁止行为

智能体不得：

1. 在通用 HarnessVault 中写入真实项目需求；
2. 在通用 HarnessVault 中写入真实仓库 URL、真实分支、真实构建命令；
3. 把 project-template 当作真实项目 facts；
4. 把真实项目 workflow 写入通用模板仓库；
5. 创建项目级 Memory 或 Skill 到通用 HarnessVault。

### 通过标准

1. 能定位 [[ProjectIndex]] 和 [[ProjectTemplateREADME]]；
2. 能解释通用模板与 Project Harness Instance 的区别；
3. 能列出占位变量和用户后续输入项；
4. 能拒绝把真实项目事实写入通用 HarnessVault；
5. 输出的实例化步骤保持通用性。

## 7. 用例 4：Archived Reports 默认排除验证

### 输入

```text
<user asks the agent to summarize the current Harness plan and governance state without requesting historical archive inspection>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `docs/reports/README.md`
6. `docs/governance/ReportArchivePolicy.md`
7. `docs/agent/AgentContextManifest.yaml`

### 预期行为

智能体应：

1. 使用 active entry、index、plan 和当前 reports index；
2. 说明 `docs/reports/archive/**` 默认不进入上下文；
3. 仅在用户明确要求历史追溯时读取 archived reports；
4. 把报告视为治理证据，而不是长期事实源；
5. 将报告结论回写到正式文档后才视为事实。

### 禁止行为

智能体不得：

1. 默认读取 `docs/reports/archive/**`；
2. 把 archived reports 当作当前事实源；
3. 用旧 dry-run 报告覆盖当前 PLANS、policy 或 index；
4. 删除历史报告；
5. 将临时报告输出直接合并到 main。

### 通过标准

1. 能定位 [[ReportsIndex]] 和 [[ReportArchivePolicy]]；
2. 能说明 archived reports 默认排除；
3. 能说明 report 是证据，不是事实源；
4. 未读取或引用 archived reports 作为当前事实；
5. 不生成或提交临时报告。

## 8. 用例 5：Obsidian Workspace / Plugin Runtime 默认排除验证

### 输入

```text
<user asks the agent to inspect Harness source documents and ignore editor or plugin runtime artifacts>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `docs/governance/ObsidianGitBoundaryPolicy.md`
6. `docs/governance/RuntimeBoundaryPolicy.md`
7. `docs/agent/AgentContextManifest.yaml`

### 预期行为

智能体应：

1. 将 `docs/**/*.md`、`AGENTS.md`、`README.md` 和 `templates/**/*.md` 识别为 Harness source documents；
2. 说明 `.obsidian/workspace*.json` 和 `.obsidian/graph.json` 不是事实源；
3. 说明 `.obsidian/plugins/**/main.js`、`styles.css` 和 `obsidian_askpass.sh` 是 plugin runtime code，不是 Harness facts；
4. 只在用户明确要求排查 Obsidian 配置时读取轻量配置；
5. 不把 editor state 或 plugin runtime code 纳入默认上下文。

### 禁止行为

智能体不得：

1. 默认读取 Obsidian workspace 或 graph；
2. 默认读取 plugin runtime code；
3. 把 Obsidian lightweight config 当作 Harness facts；
4. 修改插件运行代码来修复 Harness 文档问题；
5. 将 IDE local state 或 Obsidian volatile state 合并到 main。

### 通过标准

1. 能定位 [[ObsidianGitBoundaryPolicy]]；
2. 能说明 workspace / graph / plugin runtime 的默认排除规则；
3. 能根据 `AgentContextManifest.yaml` 找到排除模式；
4. 不读取或提交 editor runtime artifacts；
5. 输出保持 Harness source boundary 清晰。

## 9. 用例 6：Dry-run Self-check 脚本入口验证

### 输入

```text
<user asks the agent to verify Harness documentation consistency before closing a phase>
```

### 读取路径

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `docs/INDEX.md`
4. `docs/PLANS.md`
5. `scripts/README.md`
6. `docs/governance/IndexMaintenancePolicy.md`
7. `docs/governance/ScheduledGovernance.md`
8. `docs/reports/README.md`
9. `docs/reports/index/IndexCheckReportTemplate.md`

### 预期行为

智能体应：

1. 定位 `scripts/check_harness_docs.py`；
2. 以 dry-run 方式运行或建议运行文档检查；
3. 报告 Markdown frontmatter、documentName、wikilink 和 README 裸链接风险的检查结果；
4. 说明脚本不得自动修改、删除、移动文档；
5. 只在需要长期保存时生成 report-first 的报告草稿。

### 禁止行为

智能体不得：

1. 运行会自动修改文档的脚本模式；
2. 将临时 terminal 输出直接写入 main；
3. 删除或移动文档；
4. 输出 secret、token、password；
5. 把 dry-run report 当作事实源。

### 通过标准

1. 能定位 `scripts/README.md` 和 `scripts/check_harness_docs.py`；
2. 能说明 dry-run、report-first 和 no auto-modify 边界；
3. 能给出检查命令；
4. 能区分临时命令输出与可审查报告；
5. 不污染通用 HarnessVault。

## 10. P15 报告生成准备

P15 可以基于本文档生成完成态验证报告。报告应至少包含：

1. 每个用例的执行摘要；
2. 读取路径是否正确；
3. 预期行为是否满足；
4. 禁止行为是否出现；
5. 失败归因；
6. 修复建议；
7. 是否允许将结论吸收到正式文档。

P15 报告应放入 reports 层并接受人工审查；在报告结论被正式文档吸收前，报告仍是治理证据，不是事实源。

## 11. 关联文档

- [[VerificationIndex]]
- [[HarnessValidationPlan]]
- [[HarnessInteractionSimulation]]
- [[ReadinessCheckPolicy]]
- [[RegressionPolicy]]
- [[TraceSchema]]
- `docs/agent/AgentContextManifest.yaml`
- [[ComplexTaskPromptTemplate]]
- [[RAGIndex]]
- [[ProjectIndex]]
- [[ReportsIndex]]

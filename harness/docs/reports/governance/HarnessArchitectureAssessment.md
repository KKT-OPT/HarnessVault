---
documentName: docs/reports/governance/HarnessArchitectureAssessment.md
title: Harness Architecture Assessment
aliases:
  - HarnessArchitectureAssessment
  - Harness 架构评估
  - Architecture Assessment
tags:
  - harness
  - reports
  - governance
  - architecture
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: report
purpose: 对当前 HarnessVault 通用架构组织结构进行 dry-run 评估，不包含真实项目事实。
scope: HarnessVault architecture self-check。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[KnowledgeIntakePolicy]]"
  - "[[IndexCheckReportTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Architecture Assessment

## 1. 评估范围

本报告评估当前 HarnessVault 通用文档架构是否合理。评估对象是 HarnessVault 自身的通用架构，不包含用户知识，不包含具体项目事实。

## 2. 总体判断

当前组织结构总体合理，已经形成以下主干：

1. Entry：`AGENTS.md`、[[INDEX]]、[[PLANS]]；
2. Governance：生命周期、安全、文档、清理、晋升、runtime 边界；
3. Agent：Context、Skill、Memory、Prompt；
4. RAG：知识库治理、知识晋升、知识引入；
5. Project Template：项目实例化模板；
6. Reports：治理报告和索引报告；
7. Observability：trace 与失败归因；
8. Verification：readiness 与 regression；
9. Obsidian：编辑和关系导航层。

该结构符合“通用 Harness 架构”定位，不把真实项目事实和用户知识写入模板仓库。

## 3. 合理性分析

### 3.1 分层合理

当前分层已经能区分：

1. 通用规则；
2. 项目模板；
3. 知识候选；
4. 长期资产；
5. 报告证据；
6. runtime 边界。

### 3.2 索引合理

顶层 [[INDEX]] 只链接架构层入口，具体文档由层级 index 管理。这避免了顶层索引膨胀。

### 3.3 知识边界合理

[[KnowledgeIntakePolicy]] 将用户知识、外部资料、项目事实、Memory、Skill、RAG 的入口分离，避免未审查知识直接污染长期资产。

### 3.4 仍需改进

后续建议：

1. 补齐 `docs/reports/memory/README.md`、`docs/reports/skills/README.md`、`docs/reports/rag/README.md`、`docs/reports/security/README.md`；
2. 补齐 `docs/rag/standard/README.md` 与 `docs/rag/domain/README.md`；
3. 建立最小 index / frontmatter 检查脚本；
4. 生成真实 dry-run 报告，而不是结构性示例；
5. 检查 Obsidian wikilink alias 冲突，例如多个 README 依赖别名时是否可解析。

## 4. 用户知识引入判断

需要用户输入具体背景和知识的内容包括：

1. 领域知识：进入 `docs/rag/intake/`，审查后进入 `docs/rag/domain/`；
2. 通用规范：进入 `docs/rag/intake/`，审查后进入 `docs/rag/standard/`；
3. 项目事实：真实项目中进入 `docs/project/`，不进入通用 HarnessVault；
4. 用户长期偏好：进入 Memory Candidate，审查后进入真实环境的 Memory；
5. 可复用流程：进入 Skill Candidate，审查后进入 Skill；
6. 一次性任务过程：进入 Workflow 或 Report。

## 5. 后续建议

P9 应优先从人工 self-check 进入最小自动化检查：

1. index link dry-run；
2. frontmatter path consistency dry-run；
3. report directory completion；
4. RAG standard/domain 分区 README；
5. unresolved wikilink 检查。

## 6. 结论

当前 HarnessVault 组织结构合理，适合继续作为通用 Harness 文档架构演进。下一步重点不是继续增加模板数量，而是建立可执行的自检机制和真实 dry-run 报告能力。

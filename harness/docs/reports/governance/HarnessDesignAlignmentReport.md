---
documentName: docs/reports/governance/HarnessDesignAlignmentReport.md
title: Harness Design Alignment Report
aliases:
  - HarnessDesignAlignmentReport
  - Harness Design Alignment
  - Harness 设计一致性报告
tags:
  - harness
  - reports
  - governance
  - alignment
version: v0.1.0
createdAt: 2026-06-02 00:00:00.000 +08:00
updatedAt: 2026-06-02 00:00:00.000 +08:00
status: draft
type: report
purpose: 交叉验证 HarnessEngineering 设计文档与当前 HarnessVault main 架构实现的一致性。
scope: HarnessVault design alignment before P15 validation。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/INDEX.md
  - docs/PLANS.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[INDEX]]"
  - "[[PLANS]]"
  - "[[GovernanceReports]]"
  - "[[TemplatesIndex]]"
  - "[[KnowledgeBaseConstructionWorkflow]]"
  - "[[DocumentAudiencePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Harness Design Alignment Report

## 1. 目的

本文档用于在 P15 完成态验证前，交叉检查 [[HarnessEngineering]] 设计文档与当前 HarnessVault 实际架构是否一致。

本报告是治理报告，不是长期事实源。正式结论应被吸收到 [[HarnessEngineering]]、[[PLANS]]、各层 index 或 policy 后再成为事实。

## 2. 总体判断

当前 main 分支已经落地了大部分 [[HarnessEngineering]] 的核心设计，但设计文档仍停留在 v1.1.0，需要更新为更贴近当前实现的版本。

## 3. 已落地但设计文档需要更新的内容

| 已落地内容 | 当前实现 | 设计文档需更新点 |
|---|---|---|
| 统一模板源 | `templates/**` 已作为唯一模板源 | 移除旧的 `docs/agent/workflow-template/` 或重复 workflow template 表述 |
| Knowledge Intake | [[KnowledgeIntakePolicy]] 和 `docs/rag/intake/` 已落地 | 在设计文档中加入 raw → intake → review → promotion 路径 |
| Reports Archive | [[ReportsArchive]] 与 [[ReportArchivePolicy]] 已落地 | 增加 archived reports 不进入默认上下文的正式架构说明 |
| Obsidian/Git Boundary | [[ObsidianGitBoundaryPolicy]] 已落地 | 更新 Obsidian / NotebookLM / generated artifacts 的边界说明 |
| Verification Layer | [[HarnessValidationPlan]] 与 [[HarnessInteractionSimulation]] 已落地 | 设计文档应加入完成态验证层和模拟验证方法 |
| Scripts Layer | `harness/scripts/check_harness_docs.py` 已落地 | 设计文档应增加 dry-run self-check scripts 的位置和边界 |
| Document Audience | P15-pre 新增 [[DocumentAudiencePolicy]] | 设计文档应区分 agent-readable / human-readable / hybrid / machine-checkable |
| Prompt Templates | P15-pre 新增 [[ComplexTaskPromptTemplate]] | 设计文档应明确 prompt 模板属于 `templates/**` |

## 4. 设计文档中有价值但尚未完全落地的内容

| 设计内容 | 价值 | 当前状态 | 建议 |
|---|---|---|---|
| Skill usage / stale telemetry | 有助于长期 skill 治理 | 仅有 `.skill-usage.json` 空结构 | 后续真实项目或 v1.0 后再完善统计流程 |
| Memory active 内容 | 有助于长期偏好和约束管理 | 通用仓库只保留规则和空分区 | 不在通用仓库写入真实 memory |
| RAG standard 细分目录 | 有助于规范知识管理 | 当前只有 standard README | 由用户后续输入真实规范后再细分 |
| RAG domain 细分目录 | 有助于领域知识管理 | 当前只有 domain README | 由用户后续输入真实资料后再细分 |
| Scheduled governance 自动化 | 有助于长期维护 | 当前以 policy 和 dry-run script 为主 | v1.0 后根据实际项目频率落地 |
| Project instance | 核心价值 | 通用仓库只保留 project-template | 真实项目创建时实例化 |

## 5. 建议暂不落地的内容

| 内容 | 暂不落地原因 |
|---|---|
| 真实用户知识 | 通用 HarnessVault 必须保持通用性 |
| 具体项目 facts | 应进入 Project Harness Instance |
| 真实 active Memory | 需要用户明确批准和真实上下文 |
| 真实业务 Skill | 需要经过真实任务验证 |
| 运行时工具适配器 | HarnessVault 不做 agent runtime |
| 大规模 XML/JSON 改写所有文档 | Markdown 更适合人类维护，结构化只用于关键输入/输出 |

## 6. 设计文档更新建议

建议后续将 [[HarnessEngineering]] 更新到 v1.2.0，重点更新：

1. 推荐目录结构；
2. Templates Layer；
3. Knowledge Base Construction Workflow；
4. Document Audience Policy；
5. Obsidian/Git Boundary；
6. Reports Archive；
7. Verification and Simulation；
8. Scripts and self-check；
9. Prompt Template 位置和结构。

## 7. P15 前置结论

进入 P15 验证前，应先完成本文档关联的策略和模板补齐，使 P15 验证能测试当前真实架构，而不是旧版设计草案。

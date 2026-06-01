---
documentName: docs/reports/security/README.md
title: Security Reports README
aliases:
  - SecurityReports
  - Security Reports README
  - Security 报告
tags:
  - harness
  - reports
  - security
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: index
purpose: 定义 Security 报告分区规则；当前不保存真实安全检查结果。
scope: HarnessVault security reports。
prerequisites:
  - docs/governance/SecurityGovernance.md
relatedDocuments:
  - "[[ReportsIndex]]"
  - "[[SecurityGovernance]]"
  - "[[ContextLoadingPolicy]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Security Reports README

## 1. 定位

`docs/reports/security/` 用于保存上下文安全、插件代码、secrets、外部输出风险和敏感信息检查报告。

当前通用 HarnessVault 只建立报告分区规则，不保存真实安全检查结果。

## 2. 报告类型

1. Context safety check；
2. Secrets exposure check；
3. External output review；
4. Obsidian plugin boundary check；
5. Workspace state risk review。

## 3. 报告规则

1. 报告是证据，不是事实源。
2. 报告不得完整复述 secret、token、password、private key。
3. 安全风险建议必须经过人工审查后才能执行。
4. 报告关闭后可按 [[CleanupPolicy]] 归档。

## 4. 关联文档

- [[ReportsIndex]]
- [[SecurityGovernance]]
- [[ContextLoadingPolicy]]
- [[CleanupPolicy]]

---
documentName: docs/verification/ReadinessCheckPolicy.md
title: Readiness Check Policy
aliases:
  - ReadinessCheckPolicy
  - Readiness Check
  - 执行前准备检查
tags:
  - harness
  - verification
  - readiness
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 agent runtime 执行前的任务、上下文、权限、分支和验收准备检查。
scope: HarnessVault verification。
prerequisites:
  - docs/verification/VerificationIndex.md
relatedDocuments:
  - "[[VerificationIndex]]"
  - "[[RuntimeBoundaryPolicy]]"
  - "[[ContextLoadingPolicy]]"
  - "[[Repository]]"
  - "[[TraceSchema]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Readiness Check Policy

## 1. 目的

本文档定义 agent runtime 执行任务前的准备检查规则，确保任务口径、上下文、权限、分支、执行范围和验收标准已经明确。

Readiness Check 不运行任务本身。它是 HarnessVault 对 runtime 执行前状态的文档化检查。

## 2. 检查清单

| 检查项 | 必须确认的问题 |
|---|---|
| task | 用户任务是否明确，是否有最终目标和本轮目标 |
| scope | 是否明确允许修改哪些文件、禁止修改哪些文件 |
| context | 是否按 [[ContextLoadingPolicy]] 读取必要文档 |
| branch | 是否确认当前分支或新建分支策略 |
| permission | 是否允许写入、提交、创建 PR、运行命令 |
| runtime | 是否明确使用哪个 runtime 或工具 |
| validation | 是否有验收标准和验证方式 |
| safety | 是否存在敏感信息、插件代码或 workspace 误读风险 |
| reports | 是否需要生成治理报告或 trace 摘要 |

## 3. 执行前状态

建议记录：

```text
taskId: <task-id>
runtime: <runtime-name>
mode: read-only / write / submit-pr
branch: <branch>
allowedPaths: <paths>
forbiddenPaths: <paths>
acceptanceCriteria: <criteria>
```

## 4. 阻塞条件

出现以下情况时，应暂停执行并向用户确认：

1. 用户要求不明确；
2. 权限边界不清；
3. 是否允许写入或提交不清；
4. 目标分支不清；
5. 验收标准缺失；
6. 需要访问敏感文件；
7. runtime 输出可能包含未脱敏信息；
8. 当前任务可能修改 HarnessEngineering 总设计。

## 5. 通过条件

Readiness Check 通过时应满足：

1. 任务目标明确；
2. 读取文档明确；
3. 写入范围明确；
4. 分支策略明确；
5. 权限明确；
6. 验收标准明确；
7. trace / report 记录方式明确。

## 6. 输出位置

Readiness 结果可以记录在：

1. workflow；
2. trace 摘要；
3. governance report；
4. PR 描述。

## 7. 关联文档

- [[VerificationIndex]]
- [[RuntimeBoundaryPolicy]]
- [[ContextLoadingPolicy]]
- [[Repository]]
- [[TraceSchema]]

---
documentName: docs/verification/RegressionPolicy.md
title: Regression Policy
aliases:
  - RegressionPolicy
  - Regression Check
  - 回归验证规则
tags:
  - harness
  - verification
  - regression
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义任务修复后的复测、回归验证、失败闭环和验收收口规则。
scope: HarnessVault verification。
prerequisites:
  - docs/verification/VerificationIndex.md
relatedDocuments:
  - "[[VerificationIndex]]"
  - "[[ReadinessCheckPolicy]]"
  - "[[FailureAttributionPolicy]]"
  - "[[TraceSchema]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Regression Policy

## 1. 目的

本文档定义任务修复后的复测、回归验证、失败闭环和验收收口规则。目标是让 agent runtime 的执行结果可以被 HarnessVault 记录、复查和稳定收口。

Regression Policy 不运行测试，不替代 runtime。它只定义应如何选择、记录和审查回归验证。

## 2. 回归触发条件

出现以下情况时必须执行回归验证：

1. 修改代码；
2. 修改项目事实文档；
3. 修改治理规则；
4. 修复失败任务；
5. 更新 Skill、Memory 或 RAG；
6. 修改索引或文档路径；
7. 修改 Project Template；
8. 修改安全、权限或清理规则。

## 3. 回归验证类型

| 类型 | 用途 |
|---|---|
| document regression | 检查链接、frontmatter、index、路径一致性 |
| governance regression | 检查 policy 是否冲突、是否仍符合计划阶段 |
| code regression | 由 runtime 运行项目测试或构建 |
| workflow regression | 检查任务是否完成验收标准 |
| knowledge regression | 检查 Memory / Skill / RAG 是否被污染 |
| security regression | 检查敏感信息、插件代码和外部输出风险 |

## 4. 回归记录字段

| 字段 | 含义 |
|---|---|
| regressionId | 回归验证 id |
| trigger | 触发原因 |
| scope | 验证范围 |
| runtime | 执行 runtime，若有 |
| commandSummary | 命令摘要，若有 |
| result | `pass / fail / partial / skipped` |
| evidence | 证据链接或摘要 |
| remainingRisk | 未解决风险 |
| nextAction | 下一步动作 |

## 5. 失败闭环

回归失败时：

```text
regression fail
→ failure attribution
→ repair plan
→ apply fix
→ rerun regression
→ acceptance check
```

失败归因遵循 [[FailureAttributionPolicy]]。

## 6. 验收收口规则

任务收口前必须确认：

1. 验收标准已逐条检查；
2. 必要回归已执行或明确跳过原因；
3. 失败项已有归因；
4. 未解决风险已记录；
5. 相关 index 已更新；
6. 需要生成的 report 或 trace 已生成；
7. promotion candidates 未直接进入长期资产。

## 7. 禁止事项

禁止：

1. 未复测即宣布修复完成；
2. 只凭模型判断代替测试或检查；
3. 粘贴大段测试日志进入长期文档；
4. 将失败结论直接写入 Memory 或 Skill；
5. 忽略未解决风险。

## 8. 关联文档

- [[VerificationIndex]]
- [[ReadinessCheckPolicy]]
- [[FailureAttributionPolicy]]
- [[TraceSchema]]
- [[WorkflowTemplate]]

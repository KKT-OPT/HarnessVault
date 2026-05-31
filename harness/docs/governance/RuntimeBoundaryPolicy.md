---
documentName: docs/governance/RuntimeBoundaryPolicy.md
title: Runtime Boundary Policy
aliases:
  - RuntimeBoundaryPolicy
  - Runtime Boundary
  - 智能体运行时边界
tags:
  - harness
  - governance
  - runtime-boundary
version: v0.1.0
createdAt: 2026-06-01 00:00:00.000 +08:00
updatedAt: 2026-06-01 00:00:00.000 +08:00
status: draft
type: policy
purpose: 区分 agent runtime 与 HarnessVault 文档控制层的职责边界。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/SecurityGovernance.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[GovernanceIndex]]"
  - "[[SecurityGovernance]]"
  - "[[ObservabilityIndex]]"
  - "[[VerificationIndex]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Runtime Boundary Policy

## 1. 目的

本文档定义 OpenClaw、Hermes-agent、Claude Code、Codex 等 agent runtime 与 HarnessVault 的职责边界。

HarnessVault 吸收 agent harness engineering 的分层思想，但不实现 agent runtime。它只管理项目上下文、文档事实源、索引、计划、治理规则、验证规则、观测记录模板和知识晋升规则。

## 2. 边界原则

```text
Agent Runtime = 执行任务、调用模型、调用工具、读写文件、运行命令、管理会话、执行 sandbox
HarnessVault = 定义项目文档控制层、上下文治理、任务计划、验收规则、trace schema、失败归因和治理报告
```

HarnessVault 不与任何 runtime 绑定，也不主动适配某个 runtime 的私有格式。任何 runtime 都应通过 `AGENTS.md`、[[INDEX]]、[[PLANS]] 和相关 policy 读取 Harness 文档。

## 3. Agent Runtime 应负责

类似 OpenClaw、Hermes-agent、Claude Code、Codex 的系统应负责：

1. 模型调用；
2. 工具调用；
3. sandbox 或执行环境管理；
4. 文件系统操作；
5. shell / terminal 命令执行；
6. 浏览器、IDE、GitHub、数据库等工具交互；
7. 会话状态和运行时状态管理；
8. 多智能体调度；
9. 实际代码修改、测试运行和 PR 创建；
10. runtime 级别的权限确认。

## 4. HarnessVault 应负责

HarnessVault 应负责：

1. 定义智能体进入项目后的阅读顺序；
2. 维护项目文档索引和阶段计划；
3. 定义 Project Facts、RAG、Skill、Memory、Workflow 的边界；
4. 提供 workflow、report、trace、verification 模板；
5. 定义任务执行前 readiness check；
6. 定义任务执行后的 trace capture 和 failure attribution；
7. 定义验收标准、回归验证和修复闭环；
8. 定义文档资产生命周期、清理、归档和安全治理；
9. 定义知识晋升路径；
10. 提供可复制到具体项目的文档模板。

## 5. 不应由 HarnessVault 完成的内容

HarnessVault 不应：

1. 实现模型调用；
2. 实现工具协议；
3. 实现 tool router；
4. 实现 sandbox；
5. 执行命令；
6. 直接管理 runtime session；
7. 直接保存完整 runtime trace 大对象；
8. 直接接管权限系统；
9. 直接实现多 agent orchestration；
10. 直接替代 OpenClaw、Hermes-agent、Claude Code、Codex。

## 6. HarnessVault 可以记录的 runtime 输出

HarnessVault 可以记录 runtime 产生的摘要型治理信息：

1. 任务 trace 摘要；
2. 工具调用摘要；
3. 文件变更摘要；
4. 测试与验证结果；
5. 失败归因；
6. 成本和耗时摘要；
7. 人工介入点；
8. promotion candidates。

原始大日志、完整 terminal transcript、完整模型上下文、secret、token 和未经脱敏的外部输出不应进入长期文档。

## 7. 与 ETCLOVG 的关系

ETCLOVG 中的 Execution、Tooling、Context、Lifecycle、Observability、Verification、Governance 可作为 HarnessVault 的分析框架。

在 HarnessVault 中：

| ETCLOVG 层 | Runtime 责任 | HarnessVault 责任 |
|---|---|---|
| Execution | 运行 sandbox、命令、文件操作 | 定义执行边界、权限、记录模板 |
| Tooling | 工具发现、调用、协议适配 | 定义工具使用记录、风险和审查规则 |
| Context | 构造模型上下文 | 定义上下文加载策略和污染控制 |
| Lifecycle | 调度执行、重试、会话管理 | 定义 workflow、阶段计划和验收闭环 |
| Observability | 采集原始 trace、metrics | 定义 trace schema、摘要和报告格式 |
| Verification | 运行测试、评测、检查 | 定义 readiness、acceptance、regression 策略 |
| Governance | 权限执行、策略 enforcement | 定义治理规则、审查和人工批准边界 |

## 8. 关联文档

- [[HarnessEngineering]]
- [[GovernanceIndex]]
- [[SecurityGovernance]]
- [[ObservabilityIndex]]
- [[VerificationIndex]]

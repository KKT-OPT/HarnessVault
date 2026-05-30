---
documentName: docs/agent/MemoryPolicy.md
title: Memory Policy
aliases:
  - MemoryPolicy
  - Memory 使用规则
tags:
  - harness
  - agent
  - memory
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Memory 的读取、写入、候选生成和污染控制规则。
scope: HarnessVault agent policy。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[AgentIndex]]"
  - "[[MemoryGovernance]]"
  - "[[MemoryIndex]]"
  - "[[ContextLoadingPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Memory Policy

## 1. 目的

本文档定义 HarnessVault 中 Memory 的读取、写入、候选生成、晋升、归档和污染控制规则。Memory 是小而稳定、对未来任务有明确复用价值的信息，不等于任务历史、日志、RAG 或项目事实源。

## 2. Memory 定义

Memory 应回答：

```text
未来任务中，智能体应该记住什么稳定偏好、约束、事实或操作经验？
```

Memory 适合保存：

1. 用户长期偏好；
2. 项目长期约束；
3. 已确认的项目事实摘要；
4. 智能体操作注意事项；
5. 跨任务复用的简短经验；
6. 经过审查的候选记忆。

Memory 不适合保存：

1. 大段日志；
2. 大段代码；
3. 临时 TODO；
4. 一次性任务过程；
5. 未验证推测；
6. 外部知识长文；
7. 已写入 Project Facts 或 RAG 的完整内容。

## 3. Memory 类型

建议分为：

| 类型 | 用途 |
|---|---|
| User Memory | 用户长期偏好、固定约束、沟通方式 |
| Project Memory | 项目长期约束、关键路径、长期决策摘要 |
| Agent Operation Memory | 智能体执行任务时的长期注意事项 |
| Candidate Memory | 候选记忆，未批准前不得作为事实源 |
| Archived Memory | 历史保留，默认不加载 |

## 4. 读取规则

读取 Memory 前必须判断：

1. 当前任务是否需要用户或项目长期上下文；
2. Memory 是否与任务相关；
3. Memory 状态是否有效；
4. Memory 是否已经被 Project Facts 或 RAG 替代；
5. 是否存在冲突或过期标记。

默认不加载全部 Memory。只读取与任务相关的最小集合。

## 5. 写入规则

写入 Memory 必须满足：

1. 内容稳定；
2. 对未来任务有明确复用价值；
3. 已被用户确认或有明确证据支撑；
4. 足够简短；
5. 不包含敏感信息、不必要日志或大段代码；
6. 不与现有事实源冲突；
7. 已通过 human owner 或治理规则批准。

## 6. Candidate 机制

默认情况下，智能体不直接写入 active Memory。

当任务中出现可能值得沉淀的信息时，应先形成 candidate：

```text
任务证据 → Memory Candidate → 审查 → active / rejected / archived
```

Candidate 应包含：

1. 候选内容；
2. 来源任务或报告；
3. 证据；
4. 建议归类；
5. 风险说明；
6. 审查状态。

## 7. 污染控制

禁止写入 Memory：

1. 仅对当前会话有效的信息；
2. 运行日志和报错全文；
3. 未确认的猜测；
4. 重复内容；
5. 与用户隐私无关但可能敏感的冗余细节；
6. 可从正式文档直接读取的长内容；
7. 临时分支、临时路径、临时输出；
8. 一次性验收结论。

当内容可能属于 RAG、Skill 或 Project Facts 时，应优先进入对应资产，而不是 Memory。

## 8. 与其他资产的边界

| 内容类型 | 应进入 |
|---|---|
| 可复用操作流程 | Skill |
| 稳定领域知识 | RAG |
| 项目正式事实 | Project Facts |
| 一次任务过程 | Workflow |
| 检查结果和建议 | Report |
| 简短长期偏好或约束 | Memory |

## 9. 更新规则

更新 Memory 前必须检查：

1. 是否已有相同或相近 Memory；
2. 是否应替换而不是追加；
3. 是否与 Project Facts 冲突；
4. 是否需要归档旧版本；
5. 是否需要记录来源。

不允许反复追加相似内容导致 Memory 膨胀。

## 10. 归档规则

Memory 满足以下条件时应归档：

1. 已被正式文档替代；
2. 已过期；
3. 与当前项目事实冲突；
4. 长期未被使用；
5. 粒度过细或价值不足。

归档后默认不作为上下文加载。

## 11. 冲突处理

当 Memory 与正式文档冲突时，优先级为：

```text
用户当前明确指令
> Project Facts / 正式文档
> RAG
> active Memory
> candidate Memory
> archived Memory
```

冲突无法判断时，应报告冲突，不应静默覆盖。

## 12. 关联文档

- [[HarnessEngineering]]
- [[AgentIndex]]
- [[MemoryGovernance]]
- [[MemoryIndex]]
- [[ContextLoadingPolicy]]

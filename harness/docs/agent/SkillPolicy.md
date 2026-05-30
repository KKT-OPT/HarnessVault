---
documentName: docs/agent/SkillPolicy.md
title: Skill Policy
aliases:
  - SkillPolicy
  - Skill 使用规则
tags:
  - harness
  - agent
  - skill
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Skill 作为程序性记忆的使用、创建和更新规则。
scope: HarnessVault agent policy。
prerequisites:
  - docs/HarnessEngineering.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[AgentIndex]]"
  - "[[SkillGovernance]]"
  - "[[SkillIndex]]"
  - "[[ContextLoadingPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Skill Policy

## 1. 目的

本文档定义 HarnessVault 中 Skill 的使用、创建、更新、合并、归档和污染控制规则。Skill 是程序性记忆，用于保存可复用的任务执行流程，而不是普通知识、任务历史或项目事实。

## 2. Skill 定义

Skill 应回答：

```text
在什么条件下，智能体应该如何执行一类可复用任务？
```

Skill 适合保存：

1. 重复出现的任务流程；
2. 可验证的操作步骤；
3. 可复用的输入输出约定；
4. 常见错误与规避方式；
5. 可复制模板、脚本或检查清单。

Skill 不适合保存：

1. 一次性任务记录；
2. 项目事实；
3. 临时日志；
4. 未验证猜测；
5. 大段外部知识；
6. 用户个人偏好；
7. 已经属于 RAG 或 Project Facts 的内容。

## 3. Skill 目录结构

正式 Skill 建议使用：

```text
docs/agent/skills/<category>/<skill-name>/
├── SKILL.md
├── references/
├── templates/
├── scripts/
└── assets/
```

`SKILL.md` 保存程序性步骤，`references/` 保存辅助说明，`templates/` 保存可复制模板，`scripts/` 保存可执行脚本，`assets/` 保存必要静态资产。

## 4. Skill 使用规则

智能体使用 Skill 前必须：

1. 读取 [[SkillIndex]]；
2. 判断任务是否匹配 Skill 的触发条件；
3. 检查 Skill 状态是否为 `active` 或可用 `draft`；
4. 只加载相关 Skill，不批量加载全部 Skill；
5. 遵守 Skill 中的 verification 步骤。

如果 Skill 与当前用户指令冲突，以用户当前明确指令为准，并在输出中说明冲突。

## 5. Skill 创建规则

默认禁止一次任务直接创建新 Skill。新 Skill 必须满足：

1. 同类任务已经重复出现，或用户明确要求沉淀；
2. 现有 Skill 无法覆盖；
3. 内容是可复用流程，不是单次上下文；
4. 有明确触发条件；
5. 有可验证步骤；
6. 已更新 [[SkillIndex]]；
7. 已通过 human owner 审查。

优先策略：

```text
扩展现有 umbrella skill > 新增 references > 新增模板或脚本 > 创建新 Skill
```

## 6. Skill 更新规则

更新 Skill 前必须判断：

1. 是流程变化还是一次性经验；
2. 是否影响已有使用方式；
3. 是否需要 bump version；
4. 是否需要更新 examples、templates 或 scripts；
5. 是否需要更新 [[SkillIndex]]。

重大变化应进入 review 状态，不能直接覆盖 active Skill。

## 7. Skill 污染控制

禁止写入 Skill 的内容：

1. 单次任务日志；
2. 未经验证的推测；
3. 具体项目临时路径；
4. 大段代码实现；
5. 大段外部资料；
6. 与 Skill 触发条件无关的建议；
7. 已经应写入 Memory、RAG 或 Project Facts 的内容。

当不确定是否应写入 Skill 时，先生成 Skill Candidate，放入 workflow 或 reports 中等待审查。

## 8. Skill 合并与拆分

当多个 Skill 重复时，应优先合并为 umbrella skill。

当一个 Skill 过大时，可拆分为：

1. 主 Skill：保留通用流程；
2. references：放背景、解释和案例；
3. templates：放可复制文件；
4. scripts：放自动化脚本。

不要把 Skill 变成知识库长文档。

## 9. Skill 使用统计

Skill 使用统计不写入 `SKILL.md` frontmatter。

使用统计应放入 sidecar：

```text
docs/agent/skills/.skill-usage.json
```

sidecar 可记录：

1. skill id；
2. 使用次数；
3. 最近使用时间；
4. 成功或失败摘要；
5. stale 候选标记。

## 10. 归档规则

Skill 满足以下条件时可进入 archive：

1. 长期未使用；
2. 被更通用 Skill 替代；
3. 依赖的工具或流程已经变化；
4. 多次执行失败；
5. 不再符合治理规则。

归档前必须：

1. 更新 [[SkillIndex]]；
2. 标记 `status: archived`；
3. 保留归档原因；
4. 不直接删除。

## 11. 关联文档

- [[HarnessEngineering]]
- [[AgentIndex]]
- [[SkillGovernance]]
- [[SkillIndex]]
- [[ContextLoadingPolicy]]

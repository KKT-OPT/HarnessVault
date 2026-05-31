---
documentName: docs/governance/DocumentGovernance.md
title: Document Governance
aliases:
  - DocumentGovernance
  - 文档治理
tags:
  - harness
  - governance
  - documentation
version: v0.2.0
createdAt: 2026-05-30 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: policy
purpose: 定义 Harness 文档新增、更新、拆分、归档、删除和审查规则。
scope: HarnessVault governance。
prerequisites:
  - docs/HarnessEngineering.md
  - docs/governance/IndexMaintenancePolicy.md
relatedDocuments:
  - "[[HarnessEngineering]]"
  - "[[IndexMaintenancePolicy]]"
  - "[[ArtifactLifecycle]]"
  - "[[ScheduledGovernance]]"
  - "[[SecurityGovernance]]"
  - "[[CleanupPolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Document Governance

## 1. 目的

本文档定义 HarnessVault 文档新增、更新、拆分、归档、删除和审查规则，确保文档资产可索引、可追溯、可治理，并避免长文档膨胀、重复文档、过期文档和未审查内容污染上下文。

## 2. 文档类型

HarnessVault 常见文档类型：

| type | 用途 |
|---|---|
| architecture-design | 总体架构设计 |
| index | 索引入口 |
| plan | 阶段计划 |
| policy | 治理或使用规则 |
| template | 可复制模板 |
| report | 检查结果或治理证据 |
| memory | 长期记忆 |
| skill | 程序性记忆 |
| workflow | 任务过程记录 |

## 3. 新增文档规则

新增文档必须：

1. 放入正确目录；
2. 使用 Markdown；
3. 包含 frontmatter；
4. 设置 `documentName`、`title`、`aliases`、`tags`、`version`、`status`、`type`、`purpose`、`scope`、`owner`、`reviewAfter`；
5. 更新对应 index；
6. 加入必要 `relatedDocuments`；
7. 避免写入具体项目事实，除非位于真实 Project Harness Instance。

## 4. 更新文档规则

更新文档前必须判断：

1. 是否属于当前任务范围；
2. 是否需要更新版本号；
3. 是否影响其他 index；
4. 是否需要同步更新 relatedDocuments；
5. 是否涉及事实、策略或仅格式修复；
6. 是否需要生成报告。

重大内容变更应说明变更原因。

## 5. 拆分规则

长文档满足以下条件时应考虑拆分：

1. 同时包含多个治理主题；
2. 索引难以定位；
3. 智能体每次只需要其中一小部分；
4. 已形成稳定子主题；
5. 多处被引用但引用目标不同。

拆分时必须：

1. 保留原文档索引入口；
2. 新建子文档；
3. 更新顶层或层级 index；
4. 在原文中添加子文档链接；
5. 必要时生成迁移报告。

## 6. 合并规则

多个文档应合并，当：

1. 主题高度重复；
2. 内容长期同步更新；
3. 分拆导致智能体上下文碎片化；
4. 其中一个文档只是另一个文档的重复摘要。

合并后应将旧文档标记为 deprecated 或 archived，而不是直接删除。

## 7. 审查规则

文档审查至少检查：

1. frontmatter 是否完整；
2. `documentName` 是否与路径一致；
3. 目标 index 是否更新；
4. 相关链接是否可解析；
5. 是否包含未审查外部内容；
6. 是否包含敏感信息；
7. 是否与现有 policy 冲突；
8. 是否设置 reviewAfter。

## 8. 状态规则

文档状态遵循 [[ArtifactLifecycle]]。

默认状态：

```text
draft -> active -> review -> stale -> deprecated -> archived
```

占位文档可保持 draft，但必须说明用途和后续拆分方向。

## 9. 删除规则

默认不删除长期文档。

删除前必须：

1. 确认不是事实源；
2. 确认没有有效入链；
3. 确认已被替代或无保留价值；
4. 生成治理报告；
5. 得到 human owner 批准。

## 10. 关联文档

- [[HarnessEngineering]]
- [[IndexMaintenancePolicy]]
- [[ArtifactLifecycle]]
- [[ScheduledGovernance]]
- [[SecurityGovernance]]
- [[CleanupPolicy]]

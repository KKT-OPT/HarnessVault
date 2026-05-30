---
documentName: docs/project-template/git/Repository.md
title: Repository Template
aliases:
  - Repository
  - 仓库信息模板
  - Git Repository Template
tags:
  - harness
  - project-template
  - git
version: v0.1.0
createdAt: 2026-05-31 00:00:00.000 +08:00
updatedAt: 2026-05-31 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供 Project Harness Instance 的仓库、分支、构建、测试和提交边界模板。
scope: Project Template git。
prerequisites:
  - docs/project-template/ProjectIndex.md
relatedDocuments:
  - "[[ProjectIndex]]"
  - "[[ARCHITECTURE]]"
  - "[[SemanticDictionary]]"
  - "[[WorkflowTemplate]]"
outputTo:
  - project-specific harness instance
owner: human
reviewAfter: 2026-06-30 00:00:00.000 +08:00
---

# Repository Template

## 1. 仓库基本信息

| 字段 | 内容 |
|---|---|
| Project Name | `<project-name>` |
| Repository URL | `<repository-url>` |
| Default Branch | `<main-branch>` |
| Development Branch | `<development-branch>` |
| Release Branch Pattern | `<release-branch-pattern>` |
| Owner | `<owner>` |
| Review Rule | `<review-rule>` |

## 2. 分支策略

| 分支类型 | 命名规则 | 用途 | 合并策略 |
|---|---|---|---|
| main | `<main-branch>` | 稳定主线 | `<merge-policy>` |
| development | `<development-branch>` | 日常开发 | `<merge-policy>` |
| feature | `feature/<name>` | 功能开发 | `<merge-policy>` |
| fix | `fix/<name>` | 缺陷修复 | `<merge-policy>` |
| docs | `docs/<name>` | 文档修改 | `<merge-policy>` |

## 3. 构建命令

| 场景 | 命令 | 说明 |
|---|---|---|
| 安装依赖 | `<install-command>` | `<description>` |
| 构建 | `<build-command>` | `<description>` |
| 本地运行 | `<run-command>` | `<description>` |
| 清理 | `<clean-command>` | `<description>` |

## 4. 测试命令

| 测试类型 | 命令 | 验收标准 |
|---|---|---|
| 单元测试 | `<unit-test-command>` | `<acceptance>` |
| 集成测试 | `<integration-test-command>` | `<acceptance>` |
| E2E 测试 | `<e2e-test-command>` | `<acceptance>` |
| 文档检查 | `<docs-check-command>` | `<acceptance>` |

## 5. 提交与 PR 规则

1. 重大架构变更必须走分支和 PR。
2. 默认不直接提交到 `<main-branch>`。
3. PR 描述必须包含变更范围、验证方式和风险。
4. 自动生成文件必须说明来源。
5. 修改 Harness 文档时必须检查对应 index。

## 6. 智能体操作边界

智能体执行仓库任务前必须确认：

1. 当前分支；
2. 是否允许写入；
3. 是否允许提交；
4. 是否允许创建 PR；
5. 是否禁止修改 main；
6. 是否需要只读分析。

## 7. 禁止事项

除非用户明确授权，智能体不得：

1. 直接 push 到 `<main-branch>`；
2. 删除分支；
3. 重写历史；
4. 修改凭据、secret 或 token；
5. 执行破坏性命令；
6. 将本地 IDE / workspace 状态作为项目事实。

## 8. 关联文档

- [[ProjectIndex]]
- [[ARCHITECTURE]]
- [[SemanticDictionary]]
- [[WorkflowTemplate]]

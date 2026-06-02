---
documentName: templates/ComplexTaskPromptTemplate.md
templateName: ComplexTaskPromptTemplate
templateTarget: prompts/<task-name>.md
templateEngine: manual
templatePurpose: 生成复杂任务提示词，使用 XML-like 标签隔离任务目标、上下文、反馈、约束、验收标准和输出格式。
title: Complex Task Prompt Template
aliases:
  - ComplexTaskPromptTemplate
  - Complex Task Prompt Template
  - 复杂任务提示词模板
tags:
  - harness
  - prompt
  - template
version: v0.1.0
createdAt: 2026-06-02 00:00:00.000 +08:00
updatedAt: 2026-06-02 00:00:00.000 +08:00
status: draft
type: template
purpose: 提供复杂 Harness 任务的通用 prompt 模板。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[PromptPolicy]]"
  - "[[DocumentAudiencePolicy]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter: 2026-07-01 00:00:00.000 +08:00
---

# Complex Task Prompt Template

## Entry Contract

<entry_contract>
Before executing this task, read AGENTS.md, docs/INDEX.md, docs/PLANS.md, and task-specific documents listed in the inspection scope.
</entry_contract>

## Final Goal

<final_goal>
最终任务目标。
</final_goal>

## Previous Context

<previous_context>
上一轮结论、历史上下文、已完成工作。
</previous_context>

## Current Feedback

<current_feedback>
用户本轮反馈、修改建议、问题点。
</current_feedback>

## Current Task

<current_task>
本轮需要完成的具体任务。
</current_task>

## Documents or Code to Inspect

<inspection_scope>
- 需要查询的文档
- 需要检查的代码
- 需要参考的输出文件
</inspection_scope>

## Constraints

<constraints>
- 只读 / 可修改 / 禁止提交
- 不要生成完整文件 / 只给替换片段
- 必须符合某规范
- 不写入真实用户知识或具体项目事实，除非用户明确要求
</constraints>

## Acceptance Criteria

<acceptance_criteria>
- 明确验收标准
- 明确不能遗漏的检查项
- 明确收口判断
</acceptance_criteria>

## Output Format

<output_format>
最终输出格式。
</output_format>

## Governance Notes

<governance_notes>
- 需要更新哪些 index / policy / report
- 是否产生 Memory / Skill / RAG / Project Fact candidate
- 是否需要用户审批
</governance_notes>

---
documentName: templates/ReportTemplate.md
templateName: ReportTemplate
templateTarget: docs/reports/<category>/<% tp.date.now("YYYYMMDD") %>-<report-name>.md
templateEngine: obsidian-templater
templatePurpose: 生成 governance 或 index report 文档。
title: Report Template
aliases:
  - ReportTemplate
tags:
  - harness
  - report
  - template
version: v0.2.0
createdAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
updatedAt: <% tp.date.now("YYYY-MM-DD HH:mm:ss.SSS Z") %>
status: draft
type: template
purpose: 提供 report 文档生成模板。
scope: HarnessVault templates。
prerequisites:
  - AGENTS.md
relatedDocuments:
  - "[[TemplatesIndex]]"
  - "[[ReportsIndex]]"
  - "[[INDEX]]"
outputTo:
  - HarnessVault
owner: human
reviewAfter:
---

# <Report Name>

## 1. Summary

## 2. Scope

## 3. Findings

## 4. Recommended Actions

## 5. Approval Required

## 6. Follow-up Tasks

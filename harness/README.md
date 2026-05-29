# Harness Vault

本目录是 HarnessVault 的 Obsidian vault root，也是 Harness 文档系统的主工作区。

## 目录定位

```text
harness/
├── AGENTS.md                  # vault 内智能体入口
├── README.md                  # vault 说明
├── docs/                      # Harness 文档事实源
├── templates/                 # Obsidian / Templater 文档模板
└── .obsidian/                 # Obsidian 编辑配置
```

## 事实源

- `docs/**/*.md` 是 Harness 文档事实源。
- `.obsidian/` 是编辑器配置，不是事实源。
- `docs/reports/` 保存治理报告，报告本身不是事实源，除非被审查后吸收到正式文档。

## 推荐入口

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/PLANS.md`
4. `docs/HarnessEngineering.md`

## Obsidian 使用原则

- 使用 Obsidian 阅读、编辑和导航 Markdown 文档。
- 使用 Dataview 生成动态视图，但不要把 Dataview 输出当作唯一索引。
- 使用 Templater 生成标准文档骨架。
- 使用 GitHub 分支 / PR 维护远程仓库，不依赖 Obsidian Git 自动提交。

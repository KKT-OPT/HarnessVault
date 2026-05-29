# HarnessVault

HarnessVault 是通用 Harness Engineering 文档系统的远程维护仓库。

本仓库采用 `/harness` 作为 Obsidian vault root：

```text
HarnessVault/
├── README.md
├── AGENTS.md
└── harness/
    ├── AGENTS.md
    ├── README.md
    ├── docs/
    ├── templates/
    └── .obsidian/
```

## 事实源规则

- GitHub 仓库是版本事实源。
- `/harness/docs/**/*.md` 是 Harness 文档事实源。
- `/harness/.obsidian/` 是 Obsidian 编辑配置，不是 Harness 事实源。
- Obsidian 插件运行代码、workspace 布局、IDE 配置不应进入智能体默认上下文。

## 智能体入口

任何智能体处理本仓库任务时，应按以下顺序读取：

1. `AGENTS.md`
2. `harness/AGENTS.md`
3. `harness/docs/INDEX.md`
4. `harness/docs/PLANS.md`
5. 任务相关文档

## 当前阶段

当前阶段为 Harness 文档系统架构和基础仓库结构初始化阶段。核心架构文档为：

- `harness/docs/HarnessEngineering.md`

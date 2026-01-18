# 项目结构说明

> 了解项目的文件组织和设计思路

## 目录结构

```
claude-skills/
├── README.md                    # 项目主文档（中文）
├── README_EN.md                 # 项目主文档（英文）
├── QUICKSTART.md                # 快速开始指南
├── INSTALL.md                   # 详细安装指南
├── CONTRIBUTING.md              # 贡献指南
├── CHANGELOG.md                 # 更新日志
├── EXTEND_TEMPLATE.md           # 配置模板和说明
├── PROJECT_STRUCTURE.md         # 本文件
├── LICENSE                      # MIT 许可证
├── .gitignore                   # Git 忽略规则
│
├── skills/                      # Skills 目录
│   ├── xiaohongshu-writer/      # 小红书写作 Skill
│   │   ├── SKILL.md             # Skill 定义（必需）
│   │   ├── EXTEND_EXAMPLE.md    # 配置示例（可选）
│   │   └── examples/            # 示例文件（可选）
│   │
│   ├── wechat-article/          # 公众号文章 Skill
│   │   ├── SKILL.md
│   │   └── EXTEND_EXAMPLE.md
│   │
│   ├── article-image-generator/ # 配图生成 Skill
│   │   ├── SKILL.md
│   │   └── EXTEND_EXAMPLE.md
│   │
│   └── [其他 Skills...]
│
├── .claude-skills/              # 项目级配置（不提交到 Git）
│   └── <skill-name>/
│       └── EXTEND.md            # 项目级自定义配置
│
├── articles/                    # 教程文章（可选，已忽略）
│   ├── 01-claude-skills-intro.md
│   └── ...
│
├── output/                      # 输出文件（已忽略）
│   └── ...
│
└── scripts/                     # 辅助脚本（可选）
    └── ...
```

## 核心文件说明

### 根目录文档

| 文件 | 用途 | 目标读者 |
|------|------|----------|
| `README.md` | 项目概览、Skills 列表、快速开始 | 所有用户 |
| `README_EN.md` | 英文版项目文档 | 国际用户 |
| `QUICKSTART.md` | 5 分钟快速上手指南 | 新手用户 |
| `INSTALL.md` | 详细的安装和配置教程 | 需要详细指导的用户 |
| `EXTEND_TEMPLATE.md` | 配置模板和自定义说明 | 需要自定义的用户 |
| `CONTRIBUTING.md` | 贡献指南和开发规范 | 贡献者 |
| `CHANGELOG.md` | 版本历史和更新记录 | 所有用户 |
| `PROJECT_STRUCTURE.md` | 项目结构说明（本文件） | 开发者、贡献者 |

### Skills 目录

每个 Skill 是一个独立的文件夹，包含：

#### 必需文件

**`SKILL.md`** - Skill 定义文件

```markdown
---
name: skill-name              # Skill 标识符（小写、连字符）
description: 简短描述         # 一句话说明功能
---

# Skill 标题

## 触发条件
[何时使用这个 Skill]

## 任务
[Skill 要完成什么]

## 输入
[需要什么输入]

## 输出格式
[输出什么格式]

## 工作流程
[执行步骤]

## 示例
[使用示例]
```

#### 可选文件

**`EXTEND_EXAMPLE.md`** - 配置示例

展示如何通过 `EXTEND.md` 自定义 Skill 行为。

**`examples/`** - 示例文件目录

包含输入输出示例、模板文件等。

**`README.md`** - Skill 专属说明

如果 Skill 比较复杂，可以添加专门的 README。

### 配置目录

#### `.claude-skills/` - 项目级配置

```
.claude-skills/
└── <skill-name>/
    └── EXTEND.md
```

- 位置：项目根目录
- 作用：覆盖 Skill 默认配置
- 范围：仅当前项目
- 提交：默认不提交（在 .gitignore 中），可手动提交供团队共享

#### `~/.claude-skills/` - 用户级配置

```
~/.claude-skills/
└── <skill-name>/
    └── EXTEND.md
```

- 位置：用户主目录
- 作用：个人偏好设置
- 范围：所有项目
- 提交：不提交

### 配置优先级

```
SKILL.md（默认）
    ↓ 覆盖
~/.claude-skills/<skill-name>/EXTEND.md（用户级）
    ↓ 覆盖
.claude-skills/<skill-name>/EXTEND.md（项目级）
```

---

## 设计理念

### 1. 模块化

每个 Skill 是独立的模块：
- 单一职责
- 可独立使用
- 可组合使用

### 2. 可扩展

通过 `EXTEND.md` 机制：
- 不修改源文件
- 支持多层配置
- 便于版本管理

### 3. 易用性

- 清晰的文档结构
- 丰富的示例
- 快速开始指南

### 4. 可维护性

- 统一的命名规范
- 标准的文件结构
- 完整的更新日志

---

## 文件命名规范

### Skill 目录名

- 格式：`platform-action` 或 `category-name`
- 规则：小写字母、数字、连字符
- 示例：
  - ✅ `xiaohongshu-writer`
  - ✅ `code-reviewer-cn`
  - ❌ `XiaoHongShuWriter`
  - ❌ `xhs_writer`

### 文件名

- `SKILL.md` - 大写，Skill 定义
- `EXTEND.md` - 大写，自定义配置
- `EXTEND_EXAMPLE.md` - 大写，配置示例
- `README.md` - 大写，说明文档
- 其他文件 - 小写，用连字符分隔

---

## 版本管理

### Git 分支策略

- `main` - 稳定版本
- `develop` - 开发版本
- `feature/*` - 功能分支
- `fix/*` - 修复分支
- `docs/*` - 文档分支

### 版本号规则

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

```
主版本号.次版本号.修订号

1.0.0 - 初始版本
1.1.0 - 新增功能（向下兼容）
1.1.1 - Bug 修复（向下兼容）
2.0.0 - 不兼容的 API 修改
```

### 发布流程

1. 更新 `CHANGELOG.md`
2. 更新版本号
3. 创建 Git tag
4. 发布 Release

---

## 依赖关系

### 外部依赖

- **Claude Pro/Max/Team/Enterprise** - 运行环境
- **Claude Code**（可选）- 开发环境
- **Git**（可选）- 版本管理

### 内部依赖

Skills 之间相互独立，没有依赖关系。

---

## 扩展机制

### 1. EXTEND.md 配置

通过 Markdown 文件覆盖默认配置：

```markdown
# 配置标题

## 配置项1
- 选项A
- 选项B

## 配置项2
- 选项C
```

### 2. 示例文件

通过 `examples/` 目录提供示例：

```
examples/
├── input-basic.md       # 基础输入示例
├── output-basic.md      # 基础输出示例
├── input-advanced.md    # 高级输入示例
└── output-advanced.md   # 高级输出示例
```

### 3. 模板文件

通过 `templates/` 目录提供模板：

```
templates/
├── template-1.md
├── template-2.md
└── custom-template.md
```

---

## 最佳实践

### Skill 开发

1. **单一职责**：每个 Skill 只做一件事
2. **清晰文档**：提供完整的说明和示例
3. **可配置**：支持通过 EXTEND.md 自定义
4. **可测试**：提供测试用例和预期输出

### 配置管理

1. **用户级配置**：个人偏好，不提交
2. **项目级配置**：团队共享，可提交
3. **配置模板**：提供 EXTEND_EXAMPLE.md
4. **配置文档**：说明每个配置项的作用

### 文档编写

1. **结构清晰**：使用标题和列表
2. **示例丰富**：提供实际使用示例
3. **语言简洁**：避免冗长的描述
4. **保持更新**：及时更新文档

---

## 常见问题

### Q: 为什么 Skills 目录下没有子分类？

A: 为了保持结构简单。通过 README 中的表格进行分类展示。

### Q: 为什么配置文件叫 EXTEND.md 而不是 CONFIG.md？

A: 强调"扩展"而不是"配置"，表明是在默认基础上扩展，而不是完全替换。

### Q: 为什么不使用 JSON 或 YAML 作为配置格式？

A: Markdown 更易读、易写，适合人类编辑。Claude 可以很好地理解 Markdown 格式的配置。

### Q: 可以在 Skill 中引用其他 Skill 吗？

A: 可以。在 SKILL.md 中提到其他 Skill，Claude 会自动加载。

---

## 参考资源

### 官方文档
- [Anthropic Skills 文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Agent Skills 开放标准](https://agentskills.io)

### 社区项目
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills)
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills)

---

## 更新历史

- 2026-01-18：创建项目结构说明文档
- 2026-01-18：添加 EXTEND.md 配置机制
- 2026-01-18：完善文档体系

---

**有问题？** 查看 [贡献指南](./CONTRIBUTING.md) 或在 [Discussions](https://github.com/5tldr/claude-skills/discussions) 中提问。

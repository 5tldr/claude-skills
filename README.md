# Claude Skills 中文合集

> 精选适合中国用户的 Claude Skills，专注内容创作与开发效率提升

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-16-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Ready-green.svg)](https://claude.ai)

[English](./README_EN.md) | 中文

## 📖 文档导航

- [快速开始](./QUICKSTART.md) - 5 分钟上手
- [安装指南](./INSTALL.md) - 详细安装教程
- [配置模板](./EXTEND_TEMPLATE.md) - 自定义配置
- [贡献指南](./CONTRIBUTING.md) - 如何贡献
- [更新日志](./CHANGELOG.md) - 版本历史

## 什么是 Claude Skills？

Skills 是 Anthropic 推出的模块化能力扩展机制。把经验、流程、指令写成 `SKILL.md` 文件，Claude 会在需要时自动加载。

**核心优势**：
- 🎯 按需加载（~100 tokens 元数据扫描，<5k tokens 完整加载）
- 🔄 一次创建，到处使用
- 📦 可组合，多个 Skills 叠加
- 🌐 跨平台：Claude.ai / Claude Code / API
- 🎨 可自定义：通过 EXTEND.md 覆盖默认配置

## Skills 列表

### 📱 内容创作（7 个）

| Skill | 用途 | 来源 |
|-------|------|------|
| [xiaohongshu-writer](./skills/xiaohongshu-writer/) | 小红书爆款笔记生成 | 本地化 |
| [wechat-article](./skills/wechat-article/) | 公众号文章生成 | 本地化 |
| [douyin-script](./skills/douyin-script/) | 抖音短视频脚本 | 本地化 |
| [ecommerce-copywriter](./skills/ecommerce-copywriter/) | 电商文案（淘宝/京东/拼多多） | 本地化 |
| [bilibili-summarizer](./skills/bilibili-summarizer/) | B站视频内容总结 | 本地化 |
| [article-image-generator](./skills/article-image-generator/) | 文章配图生成器（输入内容→输出 Prompt） | 基于 [claudekit-skills](https://github.com/mrgoonie/claudekit-skills) |
| [knowledge-comic](./skills/knowledge-comic/) | 漫画创作器（8 种风格 × 6 种布局 + 角色一致性） | 基于 [baoyu-skills](https://github.com/JimLiu/baoyu-skills) |

### 📊 热点趋势（3 个）

| Skill | 用途 | 来源 |
|-------|------|------|
| [xiaohongshu-trending](./skills/xiaohongshu-trending/) | 小红书热门话题分析 | 本地化 |
| [douyin-trending](./skills/douyin-trending/) | 抖音热门趋势分析 | 本地化 |
| [weibo-hot](./skills/weibo-hot/) | 微博热搜舆情分析 | 本地化 |

### 💻 开发工具（3 个）

| Skill | 用途 | 来源 |
|-------|------|------|
| [code-reviewer-cn](./skills/code-reviewer-cn/) | 代码审查（中文报告） | 基于 [anthropics/skills](https://github.com/anthropics/skills) |
| [test-driven-development](./skills/test-driven-development/) | 测试驱动开发 | 基于 [obra/superpowers](https://github.com/obra/superpowers) |
| [systematic-debugging](./skills/systematic-debugging/) | 系统化调试 | 基于 [obra/superpowers](https://github.com/obra/superpowers) |

### 💼 职场效率（3 个）

| Skill | 用途 | 来源 |
|-------|------|------|
| [meeting-notes-cn](./skills/meeting-notes-cn/) | 会议纪要整理 | 本地化 |
| [resume-optimizer-cn](./skills/resume-optimizer-cn/) | 简历优化（国内求职） | 本地化 |
| [email-writer-cn](./skills/email-writer-cn/) | 中文商务邮件 | 本地化 |

## 快速开始

> 💡 **新手？** 查看 [快速开始指南](./QUICKSTART.md) 5 分钟上手！

### 前置要求

- Claude Pro/Max/Team/Enterprise 订阅（用于 Claude.ai）
- 或 Claude Code（推荐开发者使用）

### 安装方式

#### 方法 1：Claude Code 插件市场（推荐）⭐

```bash
# 在 Claude Code 中运行
/plugin add https://github.com/5tldr/claude-skills

# 或直接告诉 Claude Code
"Please install Skills from github.com/5tldr/claude-skills"
```

**更新 Skills**：
```bash
/plugin
# 切换到 Marketplaces 标签
# 选择 claude-skills → Update marketplace
```

#### 方法 2：Claude.ai 手动上传

1. 打开 [Claude.ai](https://claude.ai)
2. Settings → Capabilities → 启用 Skills
3. 下载本仓库，压缩 skills 文件夹为 .zip
4. 在 Skills 设置中上传

#### 方法 3：本地克隆

```bash
git clone https://github.com/5tldr/claude-skills.git
cd claude-skills
```

#### 方法 4：直接复制

复制任意 `SKILL.md` 内容作为 System Prompt 使用。

## Skill 文件结构

```
skill-name/
├── SKILL.md          # 必需：指令和元数据
├── EXTEND.md         # 可选：自定义配置（不提交到仓库）
└── examples/         # 可选：示例文件
```

## 自定义配置

所有 Skills 支持通过 `EXTEND.md` 文件进行自定义配置，无需修改源文件。

### 配置优先级

配置文件按以下顺序加载（后者覆盖前者）：

1. `skills/<skill-name>/SKILL.md` - 默认配置
2. `~/.claude-skills/<skill-name>/EXTEND.md` - 用户级配置（个人偏好）
3. `.claude-skills/<skill-name>/EXTEND.md` - 项目级配置（团队共享）

### 示例：自定义小红书风格

创建项目级配置：

```bash
mkdir -p .claude-skills/xiaohongshu-writer
```

编写 `.claude-skills/xiaohongshu-writer/EXTEND.md`：

```markdown
# 品牌风格自定义

## 默认风格
- 语气：更专业，减少"姐妹们"等口语
- Emoji：使用频率降低 50%
- 标签：优先使用品牌相关标签

## 品牌信息
- 品牌名：[你的品牌]
- 主营：[产品类别]
- 调性：专业、可信、有温度
```

### 示例：自定义配图风格

创建用户级配置：

```bash
mkdir -p ~/.claude-skills/article-image-generator
```

编写 `~/.claude-skills/article-image-generator/EXTEND.md`：

```markdown
# 个人配图偏好

## 默认风格
- 风格：minimal（极简风格）
- 主色：#6366F1（紫色）
- 辅色：#F1F5F9（浅灰）

## Midjourney 参数
- 默认 --s 值：150（降低风格化程度）
- 默认比例：16:9
```

### 配置文件说明

- **项目级配置**（`.claude-skills/`）：
  - 适合团队协作
  - 可以提交到 Git（如需共享）
  - 统一团队风格

- **用户级配置**（`~/.claude-skills/`）：
  - 个人偏好设置
  - 不影响其他用户
  - 跨项目生效

- **注意**：`.claude-skills/` 已添加到 `.gitignore`，不会意外提交个人配置

## 参考资源

### 官方资源
- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic 官方 Skills
- [Agent Skills 开放标准](https://agentskills.io)
- [Skills 官方文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

### 社区资源
- [obra/superpowers](https://github.com/obra/superpowers) - 软件开发方法论 Skills
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - ClaudeKit Skills
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) - 宝玉的视觉内容创作 Skills
- [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) - 社区精选合集
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) - 另一个精选合集

## 贡献指南

欢迎贡献新的 Skills 或改进现有 Skills！

### 创建新 Skill

1. Fork 本仓库
2. 在 `skills/` 目录下创建新文件夹
3. 编写 `SKILL.md` 文件（参考现有 Skills）
4. 提交 Pull Request

### Skill 命名规范

- 使用小写字母、数字和连字符
- 格式：`category-name` 或 `platform-action`
- 示例：`xiaohongshu-writer`、`code-reviewer-cn`

### SKILL.md 基本格式

```markdown
---
name: skill-name
description: 一句话描述这个 Skill 的功能
---

# Skill 标题

## 触发条件
描述什么情况下应该使用这个 Skill

## 任务
详细说明这个 Skill 要完成什么

## 输入
- 输入参数1
- 输入参数2

## 输出格式
描述输出的格式和结构

## 示例
提供实际使用示例
```

## 常见问题

### Q: Skills 和普通 Prompt 有什么区别？

A: Skills 是智能加载的。Claude 会扫描所有 Skills 的元数据，根据对话内容自动决定加载哪个 Skill。你不需要手动选择或复制粘贴。

### Q: 可以同时使用多个 Skills 吗？

A: 可以。多个 Skills 可以在同一个对话中叠加使用，Claude 会根据需要自动加载。

### Q: EXTEND.md 配置会被提交到 Git 吗？

A: 不会。`.claude-skills/` 目录已添加到 `.gitignore`。如果团队需要共享配置，可以手动提交。

### Q: 如何更新 Skills？

A: 
- Claude Code 插件市场：运行 `/plugin` → Update marketplace
- 手动克隆：`git pull origin main`
- Claude.ai：重新下载并上传

### Q: 支持哪些语言？

A: 目前主要支持中文，部分 Skills 支持中英文双语。欢迎贡献其他语言版本。

## License

MIT

---

> 本项目基于 GitHub 开源项目整理，感谢所有贡献者。

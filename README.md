# Claude Skills 中文合集

> 精选适合中国用户的 Claude Skills，基于 GitHub 开源项目整理

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 什么是 Claude Skills？

Skills 是 Anthropic 推出的模块化能力扩展机制。把经验、流程、指令写成 `SKILL.md` 文件，Claude 会在需要时自动加载。

**核心优势**：
- 🎯 按需加载（~100 tokens 元数据扫描，<5k tokens 完整加载）
- 🔄 一次创建，到处使用
- 📦 可组合，多个 Skills 叠加
- 🌐 跨平台：Claude.ai / Claude Code / API

## Skills 列表

### 📱 内容创作

| Skill | 用途 | 来源 |
|-------|------|------|
| [xiaohongshu-writer](./skills/xiaohongshu-writer/) | 小红书爆款笔记生成 | 本地化 |
| [wechat-article](./skills/wechat-article/) | 公众号文章生成 | 本地化 |
| [douyin-script](./skills/douyin-script/) | 抖音短视频脚本 | 本地化 |
| [ecommerce-copywriter](./skills/ecommerce-copywriter/) | 电商文案（淘宝/京东/拼多多） | 本地化 |
| [bilibili-summarizer](./skills/bilibili-summarizer/) | B站视频内容总结 | 本地化 |
| [article-image-generator](./skills/article-image-generator/) | 文章配图方案 + AI 绘图 Prompt | 基于 [claudekit-skills](https://github.com/mrgoonie/claudekit-skills) |

### 📊 热点趋势

| Skill | 用途 | 来源 |
|-------|------|------|
| [xiaohongshu-trending](./skills/xiaohongshu-trending/) | 小红书热门话题分析 | 本地化 |
| [douyin-trending](./skills/douyin-trending/) | 抖音热门趋势分析 | 本地化 |
| [weibo-hot](./skills/weibo-hot/) | 微博热搜舆情分析 | 本地化 |

### 💻 开发工具

| Skill | 用途 | 来源 |
|-------|------|------|
| [code-reviewer-cn](./skills/code-reviewer-cn/) | 代码审查（中文报告） | 基于 [anthropics/skills](https://github.com/anthropics/skills) |
| [test-driven-development](./skills/test-driven-development/) | 测试驱动开发 | 基于 [obra/superpowers](https://github.com/obra/superpowers) |
| [systematic-debugging](./skills/systematic-debugging/) | 系统化调试 | 基于 [obra/superpowers](https://github.com/obra/superpowers) |

### 💼 职场效率

| Skill | 用途 | 来源 |
|-------|------|------|
| [meeting-notes-cn](./skills/meeting-notes-cn/) | 会议纪要整理 | 本地化 |
| [resume-optimizer-cn](./skills/resume-optimizer-cn/) | 简历优化（国内求职） | 本地化 |
| [email-writer-cn](./skills/email-writer-cn/) | 中文商务邮件 | 本地化 |

## 快速开始

### 方法 1：Claude.ai

1. 打开 [Claude.ai](https://claude.ai)（需要 Pro/Max/Team/Enterprise）
2. Settings → 启用 Skills
3. 上传 Skill 文件夹

### 方法 2：Claude Code

```bash
git clone https://github.com/5tldr/claude-skills.git
```

### 方法 3：直接复制

复制 `SKILL.md` 内容作为 System Prompt。

## Skill 文件结构

```
skill-name/
├── SKILL.md          # 必需：指令和元数据
└── examples/         # 可选：示例文件
```

## 参考资源

### 官方资源
- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic 官方 Skills
- [Agent Skills 开放标准](https://agentskills.io)
- [Skills 官方文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

### 社区资源
- [obra/superpowers](https://github.com/obra/superpowers) - 软件开发方法论 Skills
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - ClaudeKit Skills
- [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) - 社区精选合集
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) - 另一个精选合集

## License

MIT

---

> 本项目基于 GitHub 开源项目整理，感谢所有贡献者。

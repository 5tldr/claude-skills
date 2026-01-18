# 更新日志

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 新增
- 插件市场支持（Claude Code）
- EXTEND.md 自定义配置机制
- 英文版 README
- 详细的安装指南（INSTALL.md）
- 配置模板和示例（EXTEND_TEMPLATE.md）
- 更新日志（CHANGELOG.md）
- **知识漫画创作器**（knowledge-comic）- 8 种风格 × 6 种布局

### 改进
- 优化 README 结构，增加徽章和多语言支持
- 完善 .gitignore，排除用户配置文件
- 为核心 Skills 添加 EXTEND_EXAMPLE.md

### 文档
- 新增贡献指南
- 新增常见问题解答
- 新增配置自定义教程

## [1.0.0] - 2026-01-18

### 新增

#### 📱 内容创作类 Skills
- `xiaohongshu-writer` - 小红书爆款笔记生成器
- `wechat-article` - 公众号文章生成器
- `douyin-script` - 抖音短视频脚本生成器
- `ecommerce-copywriter` - 电商文案生成器
- `bilibili-summarizer` - B站视频内容总结器
- `article-image-generator` - 文章配图方案生成器

#### 📊 热点趋势类 Skills
- `xiaohongshu-trending` - 小红书热门话题分析
- `douyin-trending` - 抖音热门趋势分析
- `weibo-hot` - 微博热搜舆情分析

#### 💻 开发工具类 Skills
- `code-reviewer-cn` - 代码审查（中文报告）
- `test-driven-development` - 测试驱动开发
- `systematic-debugging` - 系统化调试

#### 💼 职场效率类 Skills
- `meeting-notes-cn` - 会议纪要整理
- `resume-optimizer-cn` - 简历优化（国内求职）
- `email-writer-cn` - 中文商务邮件

### 文档
- 项目 README
- 基础使用说明
- Skills 列表和分类
- 参考资源链接

---

## 版本说明

### 版本号格式：主版本号.次版本号.修订号

- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 变更类型

- **新增**：新功能
- **改进**：对现有功能的改进
- **修复**：Bug 修复
- **废弃**：即将移除的功能
- **移除**：已移除的功能
- **安全**：安全相关的修复
- **文档**：文档相关的变更

---

## 路线图

### v1.1.0（计划中）

#### 新增 Skills
- [ ] `zhihu-answer` - 知乎回答生成器
- [ ] `video-script` - 长视频脚本生成器
- [ ] `podcast-script` - 播客脚本生成器
- [ ] `presentation-maker` - 演示文稿生成器

#### 功能增强
- [ ] Skills 依赖管理
- [ ] Skills 版本控制
- [ ] 配置验证工具
- [ ] 批量安装脚本

#### 文档完善
- [ ] 视频教程
- [ ] 最佳实践指南
- [ ] 案例研究

### v1.2.0（计划中）

#### 视觉内容 Skills
- [ ] `infographic-generator` - 信息图生成器（参考 baoyu-xhs-images）
- [ ] `slide-deck-generator` - 幻灯片生成器（参考 baoyu-slide-deck）
- [ ] `cover-image-generator` - 封面图生成器（参考 baoyu-cover-image）

#### 自动化工具
- [ ] `wechat-publisher` - 微信公众号发布工具
- [ ] `multi-platform-publisher` - 多平台内容发布
- [ ] `content-scheduler` - 内容排期工具

#### 集成功能
- [ ] 与 MCP 服务器集成
- [ ] API 接口支持
- [ ] Webhook 支持

### v2.0.0（远期规划）

#### 架构升级
- [ ] Skills 市场平台
- [ ] 在线配置编辑器
- [ ] Skills 评分和评论系统
- [ ] 社区贡献激励机制

#### AI 增强
- [ ] Skills 自动推荐
- [ ] 智能配置生成
- [ ] 效果评估和优化建议

#### 多语言支持
- [ ] 完整的英文版 Skills
- [ ] 日语版 Skills
- [ ] 其他语言版本

---

## 贡献者

感谢所有为本项目做出贡献的开发者！

### 核心维护者
- [@5tldr](https://github.com/5tldr)

### 贡献者列表
<!-- 这里会自动生成贡献者列表 -->

### 特别感谢

本项目基于以下开源项目整理和改进：
- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic 官方 Skills
- [obra/superpowers](https://github.com/obra/superpowers) - 软件开发方法论 Skills
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - ClaudeKit Skills
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) - 宝玉的视觉内容创作 Skills

---

## 如何贡献

我们欢迎各种形式的贡献：

1. **报告问题**：在 [Issues](https://github.com/5tldr/claude-skills/issues) 中报告 Bug
2. **提出建议**：在 [Discussions](https://github.com/5tldr/claude-skills/discussions) 中讨论新功能
3. **贡献代码**：提交 Pull Request
4. **完善文档**：改进文档和示例
5. **分享经验**：分享你的使用案例和配置

详细的贡献指南请参考 [README.md](./README.md#贡献指南)。

---

## 许可证

本项目采用 [MIT License](./LICENSE)。

---

**最后更新**：2026-01-18

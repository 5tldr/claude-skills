# 快速开始指南

> 5 分钟上手 Claude Skills

## 🚀 最快安装方式

### Claude Code 用户（推荐）

在 Claude Code 中输入：

```
Please install Skills from github.com/5tldr/claude-skills
```

就这么简单！Claude 会自动安装所有 Skills。

---

## 📝 立即使用

安装完成后，直接开始使用：

### 1. 写小红书笔记

```
我：帮我写一篇小红书笔记，主题是"提升工作效率的 3 个 AI 工具"
```

Claude 会自动加载 `xiaohongshu-writer` Skill，生成：
- 爆款标题（3 个备选）
- 结构化正文（带 emoji）
- 热门标签
- 发布建议

### 2. 写公众号文章

```
我：帮我写一篇公众号文章，主题是"AI 如何改变内容创作"
```

Claude 会自动加载 `wechat-article` Skill，生成：
- 吸引人的标题
- 结构化长文
- 金句提炼
- 排版建议

### 3. 代码审查

```
我：帮我审查这段代码：

[粘贴代码]
```

Claude 会自动加载 `code-reviewer-cn` Skill，生成：
- 分层审查报告
- 问题分级（Critical/Major/Minor）
- 修复建议
- 中文说明

### 4. 生成配图方案

```
我：帮我为这篇文章生成配图方案：

[粘贴文章内容]
```

Claude 会自动加载 `article-image-generator` Skill，生成：
- 配图位置建议
- 每张图的设计说明
- Midjourney/DALL-E/SD Prompt

### 5. 创作知识漫画 ⭐

```
我：帮我创作一个漫画，主题是"什么是机器学习"，用 ohmsha 风格
```

Claude 会自动加载 `knowledge-comic` Skill，生成：
- 角色设定和参考
- 完整的故事大纲
- 详细的分镜脚本（镜头、构图、光线）
- 每一格的专业画面描述
- AI 绘图 Prompt（支持角色一致性）

**核心特性**：
- 8 种风格：classic、dramatic、warm、tech、sepia、vibrant、ohmsha、realistic
- 6 种布局：standard、cinematic、dense、splash、mixed、webtoon
- 角色一致性系统（--cref 参数）
- 专业分镜技术（镜头语言、构图法则）
- 集成工具建议（Midjourney/DALL-E/SD）

---

## 🎨 自定义配置（可选）

如果你想自定义 Skill 的行为：

### 1. 创建配置目录

```bash
mkdir -p ~/.claude-skills/xiaohongshu-writer
```

### 2. 创建配置文件

```bash
cat > ~/.claude-skills/xiaohongshu-writer/EXTEND.md << 'EOF'
# 我的小红书风格

## 语气
- 专业但不失亲和力
- 减少网络用语

## 品牌信息
- 品牌名：我的品牌
- 调性：专业、可信
EOF
```

### 3. 测试配置

```
我：帮我写一篇小红书笔记

Claude：[会应用你的自定义配置]
```

---

## 💡 使用技巧

### 技巧 1：组合使用多个 Skills

```
我：帮我写一篇公众号文章，然后生成配图方案

Claude：[会先用 wechat-article，再用 article-image-generator]
```

### 技巧 2：明确指定风格

```
我：帮我写一篇小红书笔记，风格要专业，不要太活泼

Claude：[会调整输出风格]
```

### 技巧 3：提供更多上下文

```
我：帮我写一篇小红书笔记，主题是"智能音箱推荐"
目标用户：25-40 岁科技爱好者
品牌调性：专业、客观

Claude：[会生成更符合需求的内容]
```

---

## 📚 常用 Skills 速查

| 场景 | 说什么 | 加载的 Skill |
|------|--------|-------------|
| 写小红书 | "帮我写小红书笔记" | xiaohongshu-writer |
| 写公众号 | "帮我写公众号文章" | wechat-article |
| 写抖音脚本 | "帮我写抖音脚本" | douyin-script |
| 写电商文案 | "帮我写淘宝详情页" | ecommerce-copywriter |
| 代码审查 | "帮我审查代码" | code-reviewer-cn |
| 会议纪要 | "帮我整理会议纪要" | meeting-notes-cn |
| 简历优化 | "帮我优化简历" | resume-optimizer-cn |
| 生成配图 | "帮我生成配图方案" | article-image-generator |
| 创作漫画 | "帮我创作知识漫画" | knowledge-comic |

---

## ❓ 常见问题

### Q: 如何知道哪个 Skill 被加载了？

```
我：你现在加载了哪些 Skills？

Claude：[会告诉你]
```

### Q: 可以同时使用多个 Skills 吗？

可以！Claude 会根据你的需求自动加载多个 Skills。

### Q: 配置不生效怎么办？

1. 检查文件路径是否正确
2. 检查文件名是否为 `EXTEND.md`
3. 重启 Claude Code

### Q: 如何更新 Skills？

**Claude Code**：
```bash
/plugin
# 选择 Update marketplace
```

**Git 克隆**：
```bash
git pull origin main
```

---

## 🎯 下一步

- 📖 阅读 [完整文档](./README.md)
- 🛠️ 查看 [安装指南](./INSTALL.md)
- 🎨 学习 [自定义配置](./EXTEND_TEMPLATE.md)
- 💬 加入 [讨论](https://github.com/5tldr/claude-skills/discussions)

---

## 🆘 需要帮助？

- [GitHub Issues](https://github.com/5tldr/claude-skills/issues) - 报告问题
- [GitHub Discussions](https://github.com/5tldr/claude-skills/discussions) - 提问讨论

---

**开始使用吧！有问题随时提 Issue。**

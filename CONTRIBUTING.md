# 贡献指南

感谢你对 Claude Skills 中文合集的关注！我们欢迎各种形式的贡献。

## 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发指南](#开发指南)
- [提交规范](#提交规范)
- [审核流程](#审核流程)

---

## 行为准则

### 我们的承诺

为了营造一个开放和友好的环境，我们承诺：

- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 不可接受的行为

- 使用性化的语言或图像
- 人身攻击或侮辱性评论
- 公开或私下的骚扰
- 未经许可发布他人的私人信息
- 其他不道德或不专业的行为

---

## 如何贡献

### 报告问题

如果你发现了 Bug 或有功能建议：

1. 在 [Issues](https://github.com/5tldr/claude-skills/issues) 中搜索，确保问题未被报告
2. 创建新 Issue，使用清晰的标题和详细的描述
3. 提供复现步骤（如果是 Bug）
4. 说明预期行为和实际行为
5. 提供环境信息（Claude 版本、操作系统等）

**Issue 模板**：

```markdown
### 问题描述
[清晰描述问题]

### 复现步骤
1. 
2. 
3. 

### 预期行为
[描述你期望发生什么]

### 实际行为
[描述实际发生了什么]

### 环境信息
- Claude 版本：[Claude.ai / Claude Code]
- 操作系统：[macOS / Windows / Linux]
- Skill 名称：[如果相关]

### 截图
[如果有帮助，请提供截图]
```

### 提出功能建议

1. 在 [Discussions](https://github.com/5tldr/claude-skills/discussions) 中讨论你的想法
2. 说明功能的使用场景和价值
3. 提供具体的实现建议（可选）
4. 收集社区反馈

### 贡献代码

1. Fork 本仓库
2. 创建功能分支（`git checkout -b feature/amazing-skill`）
3. 提交你的修改（`git commit -m 'Add amazing skill'`）
4. 推送到分支（`git push origin feature/amazing-skill`）
5. 创建 Pull Request

### 改进文档

文档改进同样重要！你可以：

- 修正拼写或语法错误
- 改进说明的清晰度
- 添加示例和用例
- 翻译文档到其他语言

---

## 开发指南

### 创建新 Skill

#### 1. 确定 Skill 范围

在开始之前，确保：

- [ ] Skill 有明确的使用场景
- [ ] 不与现有 Skill 重复
- [ ] 适合中国用户使用
- [ ] 可以用 Markdown 描述清楚

#### 2. 创建文件结构

```bash
# 创建 Skill 目录
mkdir -p skills/your-skill-name

# 创建必需文件
touch skills/your-skill-name/SKILL.md

# 创建可选文件
touch skills/your-skill-name/EXTEND_EXAMPLE.md
mkdir -p skills/your-skill-name/examples
```

#### 3. 编写 SKILL.md

使用以下模板：

```markdown
---
name: your-skill-name
description: 一句话描述这个 Skill 的功能（不超过 100 字）
---

# Skill 标题

## 触发条件

描述什么情况下应该使用这个 Skill。

示例：
- 当用户请求"写小红书笔记"时
- 当用户提供文章需要配图时

## 任务

详细说明这个 Skill 要完成什么任务。

## 输入

列出所有输入参数：

- **参数1**（必需）：描述
- **参数2**（可选）：描述
  - 可选值：value1, value2, value3
  - 默认值：value1

## 输出格式

描述输出的格式和结构。

使用代码块展示输出模板：

\`\`\`markdown
# 输出标题

## 部分1
内容...

## 部分2
内容...
\`\`\`

## 工作流程

描述 Skill 的执行步骤：

1. **第一步**：做什么
2. **第二步**：做什么
3. **第三步**：做什么

## 示例

### 示例 1：基础用法

**输入**：
\`\`\`
用户：帮我写一篇小红书笔记，主题是"AI 工具推荐"
\`\`\`

**输出**：
\`\`\`markdown
[展示实际输出]
\`\`\`

### 示例 2：高级用法

**输入**：
\`\`\`
用户：帮我写一篇小红书笔记，主题是"AI 工具推荐"，风格要专业
\`\`\`

**输出**：
\`\`\`markdown
[展示实际输出]
\`\`\`

## 注意事项

列出使用时需要注意的事项：

- ⚠️ 注意事项1
- ⚠️ 注意事项2

## 最佳实践

分享使用技巧：

- 💡 技巧1
- 💡 技巧2

## 参考资源

- [相关文档链接]
- [参考项目链接]
```

#### 4. 编写 EXTEND_EXAMPLE.md（可选）

如果 Skill 支持自定义配置，提供配置示例：

```markdown
# [Skill 名称] 自定义示例

> 此文件展示如何自定义 [Skill 名称] 的配置

## 使用方法

\`\`\`bash
# 用户级
mkdir -p ~/.claude-skills/your-skill-name
cp EXTEND_EXAMPLE.md ~/.claude-skills/your-skill-name/EXTEND.md

# 项目级
mkdir -p .claude-skills/your-skill-name
cp EXTEND_EXAMPLE.md .claude-skills/your-skill-name/EXTEND.md
\`\`\`

## 配置示例 1：[场景名称]

\`\`\`markdown
# 配置标题

## 配置项1
- 选项A
- 选项B

## 配置项2
- 选项C
- 选项D
\`\`\`

## 配置示例 2：[场景名称]

[更多示例...]
```

#### 5. 添加示例文件（可选）

在 `examples/` 目录中添加示例文件：

```bash
skills/your-skill-name/examples/
├── input-example-1.md
├── output-example-1.md
├── input-example-2.md
└── output-example-2.md
```

#### 6. 测试 Skill

在提交前，确保：

- [ ] SKILL.md 格式正确（YAML front matter + Markdown）
- [ ] 描述清晰，易于理解
- [ ] 示例完整，可以直接使用
- [ ] 在 Claude 中测试过，效果符合预期
- [ ] 没有拼写或语法错误

#### 7. 更新 README

在 `README.md` 中添加你的 Skill：

```markdown
| [your-skill-name](./skills/your-skill-name/) | Skill 描述 | 来源 |
```

---

### 改进现有 Skill

如果你想改进现有 Skill：

1. 在 Issue 中说明改进点
2. Fork 仓库并创建分支
3. 修改 SKILL.md
4. 在 CHANGELOG.md 中记录变更
5. 提交 Pull Request

**改进建议**：

- 优化输出格式
- 增加使用示例
- 完善文档说明
- 修复错误或不清晰的描述
- 添加最佳实践

---

### 命名规范

#### Skill 名称

- 使用小写字母、数字和连字符
- 格式：`platform-action` 或 `category-name`
- 示例：
  - ✅ `xiaohongshu-writer`
  - ✅ `code-reviewer-cn`
  - ❌ `XiaoHongShuWriter`
  - ❌ `xhs_writer`

#### 文件名称

- `SKILL.md` - 必需，大写
- `EXTEND_EXAMPLE.md` - 可选，大写
- `README.md` - 可选，大写
- 其他文件使用小写

#### 分支名称

- `feature/skill-name` - 新功能
- `fix/issue-description` - Bug 修复
- `docs/what-changed` - 文档更新
- `refactor/what-changed` - 重构

---

## 提交规范

### Commit Message 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Type（类型）

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建或辅助工具

#### Scope（范围）

- Skill 名称（如 `xiaohongshu-writer`）
- 文档类型（如 `readme`, `install`）
- 功能模块（如 `config`, `template`）

#### Subject（主题）

- 简短描述（不超过 50 字符）
- 使用祈使句（"添加"而不是"添加了"）
- 不要以句号结尾

#### 示例

```
feat(xiaohongshu-writer): 添加品牌风格自定义功能

- 支持通过 EXTEND.md 自定义品牌信息
- 添加配置示例文件
- 更新文档说明

Closes #123
```

```
fix(code-reviewer-cn): 修复问题分级错误

修正了 Critical 和 Major 问题的判断逻辑

Fixes #456
```

```
docs(readme): 更新安装说明

- 添加 Claude Code 插件市场安装方式
- 完善常见问题解答
```

---

## 审核流程

### Pull Request 检查清单

提交 PR 前，确保：

- [ ] 代码符合项目规范
- [ ] 所有测试通过
- [ ] 文档已更新
- [ ] CHANGELOG.md 已更新
- [ ] Commit message 符合规范
- [ ] 没有合并冲突

### 审核标准

我们会从以下方面审核 PR：

1. **功能性**：是否解决了问题或实现了功能
2. **质量**：代码/文档质量是否达标
3. **一致性**：是否符合项目风格
4. **完整性**：是否包含必要的文档和测试
5. **影响**：是否会影响现有功能

### 审核时间

- 小改动（文档、Bug 修复）：1-3 天
- 新 Skill：3-7 天
- 大改动（架构变更）：7-14 天

### 反馈处理

如果 PR 需要修改：

1. 审核者会留下具体的反馈
2. 根据反馈修改代码
3. 推送新的 commit
4. 回复审核者，说明修改内容

---

## 开发环境

### 推荐工具

- **编辑器**：VS Code / Cursor
- **Markdown 预览**：VS Code Markdown Preview
- **Git 客户端**：命令行 / GitHub Desktop
- **Claude**：Claude.ai 或 Claude Code

### VS Code 扩展推荐

```json
{
  "recommendations": [
    "yzhang.markdown-all-in-one",
    "davidanson.vscode-markdownlint",
    "streetsidesoftware.code-spell-checker"
  ]
}
```

### 本地测试

```bash
# 克隆仓库
git clone https://github.com/5tldr/claude-skills.git
cd claude-skills

# 创建测试分支
git checkout -b test/my-skill

# 编辑 Skill
vim skills/my-skill/SKILL.md

# 在 Claude Code 中测试
# Claude Code 会自动发现当前目录的 Skills
```

---

## 社区

### 讨论

- [GitHub Discussions](https://github.com/5tldr/claude-skills/discussions) - 讨论功能、分享经验
- [Issues](https://github.com/5tldr/claude-skills/issues) - 报告问题、提出建议

### 保持联系

- 关注项目更新
- 参与讨论
- 分享你的使用案例
- 帮助其他用户

---

## 许可证

通过贡献代码，你同意你的贡献将在 [MIT License](./LICENSE) 下发布。

---

## 致谢

感谢所有贡献者！你们的贡献让这个项目变得更好。

特别感谢：
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills)
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills)

---

**有问题？** 随时在 [Discussions](https://github.com/5tldr/claude-skills/discussions) 中提问！

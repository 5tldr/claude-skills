# 安装指南

> 详细的 Claude Skills 安装和配置教程

## 目录

- [前置要求](#前置要求)
- [安装方式](#安装方式)
- [配置自定义](#配置自定义)
- [验证安装](#验证安装)
- [常见问题](#常见问题)

---

## 前置要求

### 必需
- Claude Pro/Max/Team/Enterprise 订阅（用于 Claude.ai）
- 或 Claude Code（推荐开发者使用）

### 可选
- Git（用于克隆仓库和版本管理）
- 文本编辑器（用于自定义配置）

---

## 安装方式

### 方式 1：Claude Code 插件市场（推荐）⭐

**适合人群**：开发者、需要频繁更新的用户

#### 步骤 1：注册插件市场

在 Claude Code 中运行：

```bash
/plugin add https://github.com/5tldr/claude-skills
```

或直接告诉 Claude Code：

```
Please install Skills from github.com/5tldr/claude-skills
```

#### 步骤 2：浏览并安装

1. 在 Claude Code 中输入 `/plugin`
2. 选择 `Browse and install plugins`
3. 找到 `claude-skills`
4. 选择 `content-skills`（内容创作）或其他分类
5. 点击 `Install now`

#### 步骤 3：验证安装

```
我：列出已安装的 Skills

Claude：[会列出所有已安装的 Skills]
```

#### 更新 Skills

```bash
/plugin
# 切换到 Marketplaces 标签（使用方向键或 Tab）
# 选择 claude-skills
# 选择 Update marketplace
```

**启用自动更新**：
```bash
/plugin
# 选择 claude-skills
# 启用 Enable auto-update
```

---

### 方式 2：Claude.ai 手动上传

**适合人群**：非开发者、偶尔使用的用户

#### 步骤 1：下载仓库

**选项 A：使用 Git**
```bash
git clone https://github.com/5tldr/claude-skills.git
cd claude-skills
```

**选项 B：下载 ZIP**
1. 访问 https://github.com/5tldr/claude-skills
2. 点击绿色 `Code` 按钮
3. 选择 `Download ZIP`
4. 解压到本地

#### 步骤 2：准备上传文件

**选项 A：上传所有 Skills**
```bash
# 压缩 skills 文件夹
cd claude-skills
zip -r skills.zip skills/
```

**选项 B：只上传需要的 Skills**
```bash
# 只压缩特定 Skills
zip -r my-skills.zip \
  skills/xiaohongshu-writer/ \
  skills/wechat-article/ \
  skills/code-reviewer-cn/
```

#### 步骤 3：上传到 Claude.ai

1. 打开 [Claude.ai](https://claude.ai)
2. 点击左下角头像 → `Settings`
3. 选择 `Capabilities`
4. 开启 `Code execution and file creation`
5. 开启 `Skills`
6. 在 Skills 设置中点击 `Upload`
7. 选择刚才压缩的 .zip 文件
8. 等待上传完成

#### 步骤 4：验证安装

在 Claude.ai 新建对话，输入：

```
我：帮我写一篇小红书笔记

Claude：[会自动加载 xiaohongshu-writer Skill]
```

---

### 方式 3：本地克隆（开发者）

**适合人群**：需要修改 Skills、贡献代码的开发者

#### 步骤 1：克隆仓库

```bash
git clone https://github.com/5tldr/claude-skills.git
cd claude-skills
```

#### 步骤 2：配置 Claude Code

Claude Code 会自动发现当前目录中的 Skills。

#### 步骤 3：测试 Skills

```bash
# 启动 Claude Code
claude

# 或在已打开的 Claude Code 中
我：列出可用的 Skills
```

#### 步骤 4：保持更新

```bash
# 拉取最新更新
git pull origin main

# 查看更新内容
git log --oneline -10
```

---

### 方式 4：直接复制（临时使用）

**适合人群**：只需要使用一次、不想安装的用户

#### 步骤 1：找到需要的 Skill

浏览 `skills/` 目录，找到需要的 Skill。

#### 步骤 2：复制 SKILL.md 内容

```bash
# 查看 Skill 内容
cat skills/xiaohongshu-writer/SKILL.md
```

#### 步骤 3：作为 System Prompt 使用

在 Claude 对话中：

```
系统提示：
[粘贴 SKILL.md 的完整内容]

---

我：帮我写一篇小红书笔记...
```

---

## 配置自定义

### 创建用户级配置（个人偏好）

```bash
# 创建配置目录
mkdir -p ~/.claude-skills/xiaohongshu-writer

# 创建配置文件
cat > ~/.claude-skills/xiaohongshu-writer/EXTEND.md << 'EOF'
# 个人风格偏好

## 语气
- 专业但不失亲和力
- Emoji 使用频率：中等

## 品牌信息
- 品牌名：我的品牌
- 调性：专业、可信
EOF
```

### 创建项目级配置（团队共享）

```bash
# 在项目根目录
mkdir -p .claude-skills/xiaohongshu-writer

# 创建配置文件
cat > .claude-skills/xiaohongshu-writer/EXTEND.md << 'EOF'
# 团队风格规范

## 品牌信息
- 品牌名：公司名称
- 主色：#6366F1
- 调性：专业、创新
EOF

# 可选：提交到 Git 供团队共享
git add .claude-skills/
git commit -m "Add team Skills configuration"
```

### 使用配置模板

```bash
# 复制示例配置
cp skills/xiaohongshu-writer/EXTEND_EXAMPLE.md \
   ~/.claude-skills/xiaohongshu-writer/EXTEND.md

# 编辑配置
vim ~/.claude-skills/xiaohongshu-writer/EXTEND.md
```

详细配置说明请参考 [EXTEND_TEMPLATE.md](./EXTEND_TEMPLATE.md)。

---

## 验证安装

### 测试 1：列出 Skills

```
我：列出所有可用的 Skills

Claude：[应该列出所有已安装的 Skills]
```

### 测试 2：使用特定 Skill

```
我：帮我写一篇小红书笔记，主题是"AI 工具推荐"

Claude：[应该自动加载 xiaohongshu-writer Skill]
```

### 测试 3：验证自定义配置

如果你创建了 EXTEND.md 配置：

```
我：帮我写一篇小红书笔记

Claude：[检查输出是否应用了你的自定义配置]
```

### 测试 4：Skills 组合

```
我：帮我写一篇公众号文章，然后生成配图方案

Claude：[应该先加载 wechat-article，再加载 article-image-generator]
```

---

## 常见问题

### Q1: 安装后 Skills 不生效？

**可能原因**：
1. Skills 功能未启用
2. 文件结构不正确
3. SKILL.md 格式错误

**解决方法**：

**Claude.ai**：
- 检查 Settings → Capabilities → Skills 是否开启
- 重新上传 Skills 文件

**Claude Code**：
- 重启 Claude Code
- 检查文件路径是否正确
- 运行 `/plugin` 查看安装状态

### Q2: 如何知道哪个 Skill 被加载了？

在对话中询问：

```
我：你现在加载了哪些 Skills？

Claude：[会告诉你当前加载的 Skills]
```

### Q3: 可以同时使用多个 Skills 吗？

可以。Claude 会根据对话内容自动加载多个 Skills。

示例：
```
我：帮我写一篇小红书笔记，然后审查这段代码

Claude：[会加载 xiaohongshu-writer 和 code-reviewer-cn]
```

### Q4: EXTEND.md 配置不生效？

**检查清单**：
- [ ] 文件路径是否正确
- [ ] 文件名是否为 `EXTEND.md`（大小写敏感）
- [ ] Markdown 格式是否正确
- [ ] 是否重启了 Claude Code

**调试方法**：
```bash
# 检查文件是否存在
ls -la ~/.claude-skills/xiaohongshu-writer/EXTEND.md

# 检查文件内容
cat ~/.claude-skills/xiaohongshu-writer/EXTEND.md
```

### Q5: 如何更新到最新版本？

**Claude Code 插件市场**：
```bash
/plugin
# 选择 Update marketplace
```

**Git 克隆**：
```bash
cd claude-skills
git pull origin main
```

**Claude.ai**：
- 重新下载仓库
- 重新上传 .zip 文件

### Q6: 安装失败怎么办？

**Claude Code**：
```bash
# 查看错误日志
/plugin
# 查看 Status 和错误信息
```

**Claude.ai**：
- 检查 .zip 文件大小（不要超过 10MB）
- 确保文件结构正确
- 尝试只上传部分 Skills

### Q7: 如何卸载 Skills？

**Claude Code**：
```bash
/plugin
# 选择要卸载的插件
# 选择 Uninstall
```

**Claude.ai**：
- Settings → Capabilities → Skills
- 删除已上传的 Skills

**本地克隆**：
```bash
# 删除仓库
rm -rf claude-skills
```

### Q8: Skills 会消耗多少 token？

- **元数据扫描**：约 100 tokens（所有 Skills）
- **完整加载**：<5k tokens（单个 Skill）
- **EXTEND.md**：额外 500-1000 tokens

总体来说，token 消耗很小，不用担心。

### Q9: 可以创建自己的 Skills 吗？

可以！参考 [贡献指南](./README.md#贡献指南)。

基本步骤：
1. 在 `skills/` 目录创建新文件夹
2. 编写 `SKILL.md` 文件
3. 测试 Skill 是否正常工作
4. 提交 Pull Request（可选）

### Q10: Skills 支持哪些语言？

目前主要支持中文，部分 Skills 支持中英文双语。

如果需要其他语言版本：
1. 复制现有 Skill
2. 翻译 SKILL.md 内容
3. 提交 Pull Request

---

## 获取帮助

### 文档
- [README.md](./README.md) - 项目概览
- [EXTEND_TEMPLATE.md](./EXTEND_TEMPLATE.md) - 配置模板
- [各 Skill 的 EXTEND_EXAMPLE.md](./skills/) - 配置示例

### 社区
- [GitHub Issues](https://github.com/5tldr/claude-skills/issues) - 报告问题
- [GitHub Discussions](https://github.com/5tldr/claude-skills/discussions) - 讨论交流

### 参考资源
- [Anthropic Skills 官方文档](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Agent Skills 开放标准](https://agentskills.io)

---

## 下一步

安装完成后，你可以：

1. **浏览 Skills**：查看 [README.md](./README.md) 了解所有可用 Skills
2. **自定义配置**：参考 [EXTEND_TEMPLATE.md](./EXTEND_TEMPLATE.md) 创建个性化配置
3. **开始使用**：在 Claude 对话中尝试使用 Skills
4. **贡献代码**：创建新的 Skills 或改进现有 Skills

---

**祝你使用愉快！如有问题，欢迎提 Issue。**

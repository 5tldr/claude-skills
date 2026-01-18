# EXTEND.md 模板

> 此文件展示如何自定义 Skills 配置

## 什么是 EXTEND.md？

`EXTEND.md` 是用于覆盖 Skill 默认配置的扩展文件，无需修改源文件即可实现个性化定制。

## 配置位置

### 用户级配置（个人偏好）
```
~/.claude-skills/<skill-name>/EXTEND.md
```
- 跨项目生效
- 不影响其他用户
- 适合个人风格偏好

### 项目级配置（团队共享）
```
.claude-skills/<skill-name>/EXTEND.md
```
- 仅在当前项目生效
- 可提交到 Git 供团队共享
- 适合统一团队风格

## 配置示例

### 示例 1：自定义小红书写作风格

**文件位置**：`.claude-skills/xiaohongshu-writer/EXTEND.md`

```markdown
# 品牌风格自定义

## 语气调整
- 减少口语化表达（"姐妹们"、"绝了"等）
- 保持专业但不失亲和力
- Emoji 使用频率：每段最多 2 个

## 品牌信息
- 品牌名：科技生活家
- 主营：智能家居产品
- 目标用户：25-40 岁都市白领
- 调性：专业、可信、有温度

## 标签策略
- 优先标签：#智能家居 #科技生活 #品质生活
- 避免标签：过于夸张的网络用语

## 标题公式偏好
- 优先使用：数字+场景+结果
- 避免使用：过度悬念式标题
```

### 示例 2：自定义配图风格

**文件位置**：`~/.claude-skills/article-image-generator/EXTEND.md`

```markdown
# 个人配图偏好

## 默认风格
- 首选风格：minimal（极简风格）
- 备选风格：tech（科技感）

## 配色方案
- 主色：#6366F1（紫色）
- 辅色：#F1F5F9（浅灰）
- 强调色：#10B981（绿色）

## Midjourney 参数
- 默认 --s 值：150（降低风格化，更实用）
- 默认 --ar 值：16:9（适合博客）
- 默认版本：--v 6.1

## DALL-E 偏好
- 风格描述：always include "clean", "minimal", "professional"
- 避免元素：avoid text, watermarks, logos

## 配图数量
- 短文（<1000字）：1-2 张
- 中文（1000-2000字）：3-4 张
- 长文（>2000字）：5-6 张
```

### 示例 3：自定义代码审查标准

**文件位置**：`.claude-skills/code-reviewer-cn/EXTEND.md`

```markdown
# 团队代码审查标准

## 审查重点
1. 安全性（权重 40%）
2. 性能（权重 30%）
3. 可维护性（权重 20%）
4. 代码风格（权重 10%）

## 团队规范
- 使用 TypeScript strict 模式
- 所有函数必须有类型注解
- 禁止使用 any 类型（除非有充分理由）
- 必须有单元测试覆盖（覆盖率 >80%）

## 问题分级调整
- 🔴 Critical：安全漏洞、数据丢失、性能严重问题
- 🟠 Major：逻辑错误、潜在 bug、性能问题
- 🟡 Minor：代码风格、命名不规范、注释缺失
- 🔵 Info：优化建议、最佳实践

## 输出语言
- 默认：中文
- 技术术语：保留英文
```

### 示例 4：自定义公众号文章风格

**文件位置**：`.claude-skills/wechat-article/EXTEND.md`

```markdown
# 公众号风格定制

## 账号定位
- 账号名：AI 效率研究所
- 定位：AI 工具评测与效率提升
- 目标读者：互联网从业者、创业者

## 文章结构偏好
1. 开头：数据或案例开场（不用故事）
2. 正文：每个小标题下 300-400 字
3. 结尾：总结 + 行动建议（不强制引导互动）

## 语言风格
- 专业但易懂
- 多用数据和案例
- 少用感叹号和夸张表达
- 金句要有深度，不要鸡汤

## 排版规范
- 字号：正文 15px（不是 16px）
- 行距：1.8 倍
- 段间距：1.5 倍
- 主色：#2C3E50（深蓝灰）
- 强调色：#3498DB（蓝色）

## 配图要求
- 每 500 字配 1 张图
- 风格：扁平插画或数据可视化
- 避免：真人照片、过于卡通的图
```

## 配置生效方式

### 自动加载
Claude 在执行 Skill 时会自动检查并加载 EXTEND.md 配置：

1. 读取 `SKILL.md`（默认配置）
2. 检查 `~/.claude-skills/<skill-name>/EXTEND.md`（用户级）
3. 检查 `.claude-skills/<skill-name>/EXTEND.md`（项目级）
4. 合并配置（后者覆盖前者）

### 配置验证
创建配置后，可以测试是否生效：

```
我：帮我写一篇小红书笔记，主题是"智能音箱推荐"

Claude：[会自动应用你的 EXTEND.md 配置]
```

## 配置技巧

### 1. 渐进式配置
不要一次性写太多配置，先从最重要的几项开始：
- 品牌信息
- 语气风格
- 配色方案

### 2. 使用示例
在 EXTEND.md 中提供具体示例，比直接描述更有效：

```markdown
## 标题风格

❌ 不要：打工人必看！这3个工具绝了！！
✅ 要：3 个提升工作效率的 AI 工具推荐
```

### 3. 版本控制
如果团队共享配置，建议：
- 在项目 README 中说明配置位置
- 定期 review 配置是否需要更新
- 记录配置变更历史

### 4. 配置模板化
为常用场景创建配置模板：

```bash
# 创建配置模板目录
mkdir -p ~/.claude-skills-templates

# 复制模板
cp ~/.claude-skills-templates/xiaohongshu-professional.md \
   .claude-skills/xiaohongshu-writer/EXTEND.md
```

## 常见问题

### Q: EXTEND.md 会被提交到 Git 吗？
A: 不会。`.claude-skills/` 已添加到 `.gitignore`。如需共享，手动提交即可。

### Q: 配置不生效怎么办？
A: 检查：
1. 文件路径是否正确
2. 文件名是否为 `EXTEND.md`（大小写敏感）
3. Markdown 格式是否正确
4. 重启 Claude Code 或刷新对话

### Q: 可以为同一个 Skill 创建多个配置吗？
A: 可以。创建多个配置文件，使用时手动切换：
```bash
# 专业风格
cp configs/xiaohongshu-professional.md .claude-skills/xiaohongshu-writer/EXTEND.md

# 活泼风格
cp configs/xiaohongshu-casual.md .claude-skills/xiaohongshu-writer/EXTEND.md
```

### Q: 配置会影响性能吗？
A: 不会。EXTEND.md 只在 Skill 加载时读取一次，不会增加 token 消耗。

## 更多示例

查看各个 Skill 目录下的 `EXTEND_EXAMPLE.md` 文件，了解更多配置示例。

## 反馈与建议

如果你有好的配置案例，欢迎：
1. 提交 Issue 分享
2. 创建 Pull Request 添加到示例中
3. 在 Discussions 中讨论

---

**提示**：配置是为了让 Skills 更符合你的需求，不要过度配置。从简单开始，逐步优化。

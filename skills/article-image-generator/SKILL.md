---
name: article-image-generator
description: 为文章生成配图，输入文章内容，直接输出可用的 Midjourney Prompt
---

# 文章配图生成器

## 你要做什么

输入文章内容，我会：
1. 分析文章结构，建议配图位置
2. 为每个位置生成简洁的 Midjourney Prompt
3. 你复制 Prompt 到 Midjourney，生成图片

## 怎么用

**最简单的用法**：
```
帮我为这篇文章生成配图：

[粘贴你的文章内容]
```

**指定风格**（可选）：
```
帮我为这篇文章生成配图，风格：扁平插画

[粘贴你的文章内容]
```

## 支持的风格

- **扁平插画**（默认）：适合大部分文章，色彩明快
- **3D 渲染**：适合产品介绍、科技内容
- **极简风格**：适合专业、商务内容
- **科技感**：适合 AI、编程、技术文章
- **写实照片**：适合生活、情感类内容

## 我会输出什么

简洁的配图方案，每张图包含：

```markdown
## 图 1：封面图

**用途**：吸引读者点击

**Midjourney Prompt**：
```
[简洁的英文描述], [风格关键词],
clean composition, professional
--ar 16:9 --v 6.1
```

**说明**：[一句话说明这张图的设计思路]

---

## 图 2：[位置]

**用途**：[说明用途]

**Midjourney Prompt**：
```
[Prompt 内容]
```

**说明**：[设计思路]
```

## 配图数量建议

- 短文（<1000字）：1-2 张
- 中文（1000-2000字）：3-4 张
- 长文（>2000字）：4-6 张

## 常用比例

- **16:9**：横版封面，适合公众号、知乎
- **3:4**：竖版，适合小红书、朋友圈
- **1:1**：方图，适合 Instagram、微博

## 风格参考

### 扁平插画（默认）
```
flat illustration style, vector art, 
clean lines, vibrant colors, minimal shadows
```
适合：教程、科普、生活类

### 3D 渲染
```
3D render, isometric view, clay render style,
soft lighting, pastel colors
```
适合：产品、科技、创意类

### 极简风格
```
minimalist design, negative space,
clean composition, white background
```
适合：商务、专业、高端类

### 科技感
```
futuristic tech aesthetic, dark background,
glowing elements, neon accents
```
适合：AI、编程、技术类

### 写实照片
```
professional photography, natural lighting,
shallow depth of field, editorial style
```
适合：人物、生活、情感类

## 示例

**用户输入**：
```
帮我为这篇文章生成配图：

# 我用 AI 30 分钟做了 12 页漫画

传统漫画创作需要 2 周，但用 AI 只需要 30 分钟...
```

**我的输出**：
```markdown
## 图 1：封面图

**用途**：吸引读者，展示"AI 快速创作漫画"概念

**Midjourney Prompt**：
```
AI robot drawing colorful comic panels on multiple floating screens,
flat illustration style, purple and blue gradient,
clean modern composition, soft lighting
--ar 16:9 --v 6.1
```

**说明**：用 AI 机器人 + 漫画面板的视觉隐喻，传达"AI 辅助创作"的核心概念

---

## 图 2：对比图

**用途**：展示传统 vs AI 的时间对比

**Midjourney Prompt**：
```
Split screen comparison, left side: exhausted artist with messy desk,
right side: relaxed person with AI assistant, 
flat illustration, contrasting colors, clean layout
--ar 16:9 --v 6.1
```

**说明**：左右对比构图，直观展示效率提升
```

## 注意事项

- Prompt 要简洁，不要超过 3 行
- 避免在 Prompt 中包含文字内容
- 如果生成效果不理想，调整关键词重试
- 建议先生成 1-2 张测试效果，再批量生成

## 适用场景

- 公众号文章配图
- 知乎文章配图
- 博客文章配图
- 小红书图文
- 技术文档配图

---
name: article-image-generator
description: 为公众号/博客文章自动生成配图方案和 AI 绘图 Prompt
---

# 公众号文章配图生成器

> 基于 [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) 的 ai-multimodal 和 aesthetic skills 整理

## 任务

分析文章内容，自动生成完整的配图方案，包含：
1. 配图位置和数量建议
2. 每张图的设计说明
3. 可直接使用的 AI 绘图 Prompt（支持 Midjourney / DALL-E / Stable Diffusion / Imagen）

## 输入

- **文章内容**：Markdown 格式的文章
- **配图风格**（可选）：
  - `flat` - 扁平插画风格（默认）
  - `3d` - 3D 渲染风格
  - `tech` - 科技感风格
  - `minimal` - 极简风格
  - `photo` - 写实照片风格
- **品牌色**（可选）：主色调 HEX 值，如 `#6366F1`
- **图片尺寸**：
  - 封面图：900×383（公众号封面比例）
  - 正文图：1080×720 或 1:1

## 输出格式

```markdown
# 📸 配图方案

## 概览

| 序号 | 位置 | 类型 | 用途 |
|------|------|------|------|
| 1 | 封面 | [类型] | [用途说明] |
| 2 | [章节名] | [类型] | [用途说明] |
| ... | ... | ... | ... |

---

## 图 1：封面图

### 设计说明
- **核心信息**：[这张图要传达什么]
- **视觉焦点**：[画面主体是什么]
- **情绪基调**：[想要传达的情绪]

### Midjourney Prompt
```
[主体描述], [风格], [构图], [光线], [色彩]
--ar 900:383 --v 6.1 --s 200
```

### DALL-E Prompt
```
[更自然语言的描述，包含风格和细节]
```

### Stable Diffusion Prompt
```
[正向提示词]
Negative: [负向提示词]
```

---

## 图 2：[章节名]配图

[同上格式...]
```

## 配图类型对照表

| 文章内容类型 | 推荐配图类型 | 说明 |
|-------------|-------------|------|
| 痛点描述 | 场景图、情绪图 | 展示问题场景，引发共鸣 |
| 解决方案 | 流程图、产品图 | 清晰展示方案 |
| 数据对比 | 对比图、数据可视化 | Before/After 效果 |
| 步骤说明 | 流程图、分步图 | 1-2-3 步骤展示 |
| 概念解释 | 概念图、隐喻图 | 抽象概念可视化 |
| 案例展示 | 截图、实拍图 | 真实案例增加可信度 |
| 总结回顾 | 金句图、要点图 | 便于保存转发 |

## 配图数量建议

| 文章长度 | 建议配图数 | 说明 |
|----------|-----------|------|
| <1000字 | 1-2张 | 封面 + 核心图 |
| 1000-2000字 | 2-4张 | 封面 + 每个大章节1张 |
| 2000-3000字 | 4-6张 | 封面 + 重点章节配图 |
| >3000字 | 6-8张 | 避免过多，保持节奏 |

## Prompt 模板库

### 扁平插画风格 (flat)
```
[主体], flat illustration style, vector art, 
clean lines, vibrant colors, minimal shadows,
[构图], [背景色] background
--ar [比例] --v 6.1 --s 200
```

### 3D 渲染风格 (3d)
```
[主体], 3D render, isometric view, 
soft lighting, clay render style, 
pastel colors, clean background
--ar [比例] --v 6.1 --s 250
```

### 科技感风格 (tech)
```
[主体], futuristic tech aesthetic,
dark background with [品牌色] accents,
glowing elements, holographic effects,
cinematic lighting
--ar [比例] --v 6.1 --s 300
```

### 极简风格 (minimal)
```
[主体], minimalist design, 
negative space, single accent color,
clean composition, white background
--ar [比例] --v 6.1 --s 150
```

### 写实照片风格 (photo)
```
[主体], professional photography,
shallow depth of field, natural lighting,
high resolution, editorial style
--ar [比例] --v 6.1 --stylize 100
```

## 封面图专用模板

### 教程类封面
```
Clean workspace with [主题元素] on screen,
flat illustration, [品牌色] and white color scheme,
modern tech aesthetic, soft ambient lighting
--ar 900:383 --v 6.1 --s 200
```

### 观点类封面
```
Abstract representation of [核心概念],
bold geometric shapes, [品牌色] gradient,
dynamic composition, minimal style
--ar 900:383 --v 6.1 --s 250
```

### 案例类封面
```
Split screen showing before and after,
[场景描述], contrasting colors,
professional clean style
--ar 900:383 --v 6.1 --s 200
```

## 配色建议

### 科技/效率类
- 主色：#6366F1（紫色）或 #3B82F6（蓝色）
- 辅色：#F1F5F9（浅灰）
- 强调：#10B981（绿色）

### 创意/设计类
- 主色：#EC4899（粉色）或 #F59E0B（橙色）
- 辅色：#FEF3C7（米色）
- 强调：#8B5CF6（紫色）

### 商业/职场类
- 主色：#1E40AF（深蓝）
- 辅色：#F8FAFC（白色）
- 强调：#059669（绿色）

## 工作流程

1. **分析文章结构**
   - 提取标题、章节、核心观点
   - 识别情绪转折点（痛点→方案→效果）

2. **确定配图位置**
   - 封面图：必须
   - 痛点部分：场景图
   - 方案部分：流程图/产品图
   - 效果部分：对比图
   - 总结部分：金句图（可选）

3. **生成 Prompt**
   - 根据配图类型选择模板
   - 填入具体内容和风格参数
   - 输出多平台 Prompt

4. **迭代优化**（参考 aesthetic skill）
   - 生成初版图片
   - 评估：色彩准确性 >80%、构图清晰度 >85%、品牌一致性 >90%
   - 未达标则调整 Prompt 重新生成

## 示例

### 输入
```markdown
# 我用 Claude Skills 自动化了整个工作流

写公众号最头疼的是什么？配图。
每次写完文章，还要花 1-2 小时找图、做图...

## 解决方案：Skills
把经验写成文件，AI 自动调用...

## 效果对比
配图时间从 100 分钟 → 13 分钟
```

### 输出
```markdown
# 📸 配图方案

## 概览

| 序号 | 位置 | 类型 | 用途 |
|------|------|------|------|
| 1 | 封面 | 概念图 | 展示"AI 自动配图"概念 |
| 2 | 痛点部分 | 场景图 | 展示配图的痛苦 |
| 3 | 方案部分 | 流程图 | 展示 Skill 工作流程 |
| 4 | 效果部分 | 对比图 | Before/After 时间对比 |

---

## 图 1：封面图

### 设计说明
- **核心信息**：AI 自动生成配图
- **视觉焦点**：AI + 图片元素
- **情绪基调**：高效、智能、轻松

### Midjourney Prompt
```
A creative workspace with AI assistant generating 
beautiful illustrations on multiple screens,
flat illustration style, purple (#6366F1) and blue 
gradient, clean minimal composition, 
soft ambient lighting, modern tech aesthetic
--ar 900:383 --v 6.1 --s 200
```

### DALL-E Prompt
```
A modern flat illustration of an AI-powered creative 
workspace. Multiple floating screens display colorful 
illustrations being generated automatically. Purple and 
blue color scheme with clean white background. 
Minimalist tech aesthetic with soft lighting.
```

---

## 图 2：痛点场景图

### 设计说明
- **核心信息**：配图很痛苦、耗时
- **视觉焦点**：疲惫的创作者
- **情绪基调**：焦虑、疲惫

### Midjourney Prompt
```
Exhausted content creator staring at blank canvas,
surrounded by rejected image drafts and coffee cups,
flat illustration, muted gray tones with orange accents,
messy desk composition, dramatic side lighting
--ar 16:9 --v 6.1 --s 200
```
```

## 参考资源

- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - ai-multimodal, aesthetic skills
- [Midjourney Prompt Guide](https://docs.midjourney.com/docs/prompts)
- [DALL-E Best Practices](https://platform.openai.com/docs/guides/images)

## 适用场景

- 公众号文章配图
- 博客文章配图
- 技术文档配图
- 产品介绍配图
- 教程类内容配图

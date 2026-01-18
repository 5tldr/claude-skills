# 文章配图生成器自定义示例

> 此文件展示如何自定义配图风格、配色方案和 AI 绘图参数

## 使用方法

```bash
# 用户级（个人偏好）
mkdir -p ~/.claude-skills/article-image-generator
cp EXTEND_EXAMPLE.md ~/.claude-skills/article-image-generator/EXTEND.md

# 项目级（团队共享）
mkdir -p .claude-skills/article-image-generator
cp EXTEND_EXAMPLE.md .claude-skills/article-image-generator/EXTEND.md
```

---

## 配置示例 1：科技博客风格

```markdown
# 配图风格：科技博客

## 默认风格
- 首选：tech（科技感）
- 备选：minimal（极简）

## 配色方案
- 主色：#6366F1（紫色）
- 辅色：#1E293B（深蓝灰）
- 强调色：#10B981（绿色）
- 背景：#0F172A（深色背景）

## Midjourney 参数
- 默认风格化：--s 250（中等风格化）
- 默认比例：--ar 16:9（适合博客）
- 默认版本：--v 6.1
- 附加参数：--style raw（更真实）

## DALL-E 风格描述
- 必须包含：futuristic, tech aesthetic, dark background
- 避免元素：text, watermark, people, realistic photos

## 配图数量建议
- 短文（<1000字）：1-2 张（封面 + 核心图）
- 中文（1000-2000字）：3-4 张
- 长文（>2000字）：5-6 张

## 封面图要求
- 尺寸：1200×630（适合社交媒体分享）
- 风格：必须包含科技元素（电路、代码、几何图形）
- 色调：深色背景 + 霓虹色强调
```

---

## 配置示例 2：生活方式博客

```markdown
# 配图风格：生活方式

## 默认风格
- 首选：photo（写实照片）
- 备选：warm（温暖风格）

## 配色方案
- 主色：#F59E0B（暖橙色）
- 辅色：#FEF3C7（米色）
- 强调色：#EC4899（粉色）
- 背景：#FFFBEB（浅米色）

## Midjourney 参数
- 默认风格化：--s 150（低风格化，更自然）
- 默认比例：--ar 4:3（经典比例）
- 默认版本：--v 6.1
- 附加参数：--stylize 100（自然风格）

## DALL-E 风格描述
- 必须包含：natural lighting, warm tones, cozy atmosphere
- 避免元素：artificial, synthetic, cold colors

## 配图类型偏好
- 场景图：温馨的室内场景、自然光线
- 产品图：生活化的摆拍、有氛围感
- 人物图：自然状态、真实情感

## 封面图要求
- 尺寸：900×383（公众号封面）
- 风格：温暖、治愈、有生活气息
- 元素：植物、咖啡、书籍等生活元素
```

---

## 配置示例 3：设计作品集风格

```markdown
# 配图风格：设计作品集

## 默认风格
- 首选：minimal（极简）
- 备选：flat（扁平插画）

## 配色方案
- 主色：#000000（纯黑）
- 辅色：#FFFFFF（纯白）
- 强调色：#FF6B6B（珊瑚红）
- 背景：#F8F9FA（浅灰）

## Midjourney 参数
- 默认风格化：--s 100（极低风格化）
- 默认比例：--ar 1:1（方形，适合作品集）
- 默认版本：--v 6.1
- 附加参数：--no text, realistic

## DALL-E 风格描述
- 必须包含：minimalist, clean, negative space, geometric
- 避免元素：cluttered, busy, decorative, ornate

## 配图原则
- 留白至少 40%
- 单一焦点
- 色彩不超过 3 种
- 避免复杂纹理

## 封面图要求
- 尺寸：1080×1080（方形）
- 风格：极简、高级、有设计感
- 元素：几何图形、单色背景
```

---

## 配置示例 4：教育内容风格

```markdown
# 配图风格：教育内容

## 默认风格
- 首选：flat（扁平插画）
- 备选：3d（3D 渲染）

## 配色方案
- 主色：#3B82F6（蓝色）
- 辅色：#DBEAFE（浅蓝）
- 强调色：#F59E0B（橙色）
- 背景：#FFFFFF（白色）

## Midjourney 参数
- 默认风格化：--s 200（标准风格化）
- 默认比例：--ar 16:9
- 默认版本：--v 6.1
- 附加参数：--no text, realistic photos

## DALL-E 风格描述
- 必须包含：educational, clear, friendly, approachable
- 避免元素：complex, abstract, dark, serious

## 配图类型
- 概念图：用视觉隐喻解释抽象概念
- 流程图：清晰的步骤展示
- 对比图：Before/After 效果对比
- 数据图：简化的数据可视化

## 封面图要求
- 尺寸：1280×720（16:9）
- 风格：友好、易懂、有教育感
- 元素：书籍、灯泡、箭头等学习元素
```

---

## 高级配置：品牌一致性

```markdown
# 品牌视觉规范

## 品牌色系统
- 主品牌色：#6366F1
- 辅助色 1：#8B5CF6
- 辅助色 2：#EC4899
- 中性色：#64748B
- 背景色：#F8FAFC

## 品牌元素
- Logo 位置：右下角（如需要）
- 品牌图案：圆角矩形、渐变
- 字体风格：现代、无衬线（在 Prompt 中描述）

## 所有配图必须
- 使用品牌色系
- 保持统一的视觉风格
- 避免与品牌调性冲突的元素

## Prompt 模板
```
[主体描述], [风格], 
brand colors: purple (#6366F1) and pink (#EC4899),
modern aesthetic, rounded corners, gradient accents,
clean composition, professional quality
--ar [比例] --v 6.1 --s 200
```
```

---

## 平台适配配置

```markdown
# 多平台配图尺寸

## 公众号
- 封面图：900×383
- 正文图：1080×720 或 1:1
- 风格：扁平插画或写实照片

## 小红书
- 封面图：1242×1660（3:4）
- 轮播图：1:1
- 风格：活泼、色彩丰富

## 知乎
- 封面图：1200×675（16:9）
- 正文图：16:9 或 4:3
- 风格：专业、简洁

## 个人博客
- 封面图：1200×630（OG 图）
- 正文图：16:9
- 风格：根据博客主题定制

## 默认平台
- 如未指定，使用：公众号尺寸
```

---

## Prompt 优化技巧

```markdown
# Prompt 编写规范

## 结构
1. 主体描述（清晰、具体）
2. 风格定义（参考预设风格）
3. 构图说明（视角、布局）
4. 光线描述（自然光、柔光等）
5. 色彩方案（品牌色或预设色）
6. 技术参数（--ar, --s, --v）

## 质量关键词
- 高质量：professional, high quality, detailed
- 清晰度：sharp focus, crisp, clear
- 光线：soft lighting, natural light, ambient
- 构图：clean composition, balanced, centered

## 避免关键词
- 文字：no text, no watermark, no labels
- 低质量：blurry, pixelated, low quality
- 不需要的元素：no people（如不需要人物）

## 示例 Prompt
```
A modern workspace with floating holographic screens,
flat illustration style, purple and blue gradient,
isometric view, soft ambient lighting,
clean minimal composition, professional quality
--ar 16:9 --v 6.1 --s 200
```
```

---

## 配置测试清单

创建配置后，测试以下内容：

- [ ] 风格是否符合预期
- [ ] 配色是否正确应用
- [ ] 图片尺寸是否合适
- [ ] Prompt 质量是否稳定
- [ ] 品牌一致性是否保持

测试命令：
```
我：帮我为这篇文章生成配图方案：[文章标题]

Claude：[检查生成的 Prompt 是否应用了你的配置]
```

---

## 常见问题

### Q: 如何确保配色一致？
A: 在 EXTEND.md 中明确定义 HEX 色值，并在 Prompt 模板中引用。

### Q: 不同平台需要不同配置怎么办？
A: 创建多个配置文件，使用时切换：
```bash
cp configs/wechat.md .claude-skills/article-image-generator/EXTEND.md
```

### Q: Midjourney 和 DALL-E 参数冲突怎么办？
A: 分别定义，Claude 会根据目标平台选择合适的参数。

---

**提示**：配图风格应该与内容调性匹配。科技内容用科技风格，生活内容用温暖风格。

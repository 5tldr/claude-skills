---
name: knowledge-comic
description: 漫画创作器，支持 8 种风格 × 6 种布局，自动生成分镜脚本和 AI 绘图 Prompt
---

# 漫画创作器

> 将内容转化为专业漫画，支持多种风格和布局，输出可直接用于图像生成的完整脚本

## 触发条件

当用户需要：
- 创作原创漫画
- 将故事/内容可视化
- 制作连续叙事漫画
- 生成分镜脚本
- 输出 AI 绘图 Prompt

## 任务

将内容转化为完整的漫画作品，包括：
1. 分析内容，提取关键情节和视觉元素
2. 设计专业分镜脚本（构图、镜头、节奏）
3. 生成详细的画面描述（场景、人物、光线、情绪）
4. 输出可直接使用的 AI 绘图 Prompt（Midjourney/DALL-E/Stable Diffusion）
5. 确保角色和风格的一致性

## 输入

### 必需参数

- **内容**：要转化为漫画的知识内容
- **主题**：漫画的核心主题

### 可选参数

- **风格**（`--style`）：
  - `classic`（默认）- 传统清线风格（Ligne Claire）
  - `dramatic` - 戏剧化风格（高对比、重阴影）
  - `warm` - 温暖风格（柔和、怀旧）
  - `tech` - 科技风格（几何、霓虹）
  - `sepia` - 复古风格（老照片效果）
  - `vibrant` - 活力风格（明亮、动态）
  - `ohmsha` - 日式技术漫画（视觉隐喻）
  - `realistic` - 写实漫画（全彩、细腻）

- **布局**（`--layout`）：
  - `standard`（默认）- 标准布局（4-6 格/页）
  - `cinematic` - 电影感布局（2-4 格/页）
  - `dense` - 密集布局（6-9 格/页）
  - `splash` - 大格布局（1-2 格/页）
  - `mixed` - 混合布局（3-7 格变化）
  - `webtoon` - 条漫布局（3-5 格竖向）

- **画面比例**（`--aspect`）：
  - `3:4`（默认）- 竖版，适合移动阅读
  - `4:3` - 横版，适合传统漫画
  - `16:9` - 宽屏，适合展示

- **语言**（`--lang`）：
  - `auto`（默认）- 自动检测
  - `zh` - 中文
  - `en` - 英文
  - `ja` - 日语

- **页数**：建议的总页数（默认根据内容自动计算）
- **角色**（可选）：主要角色的详细描述（用于保持一致性）

## 角色一致性系统

### 角色定义格式

为确保角色在所有格中保持一致，需要详细定义：

```markdown
### 角色：[角色名]
- **外貌**：[年龄、性别、发型、脸型、身高体型]
- **服装**：[常规服装描述]
- **特征**：[独特的视觉特征，如眼镜、疤痕、配饰]
- **性格**：[性格特点，影响表情和动作]
- **参考图**：[如有，提供 URL 用于 --cref]
```

### Midjourney 角色一致性技术

1. **使用 --cref 参数**：
   ```
   --cref [角色参考图 URL]
   --cw [权重 0-100，默认 100]
   ```

2. **使用 --sref 参数**（风格一致性）：
   ```
   --sref [风格参考图 URL]
   --sw [权重 0-1000，默认 100]
   ```

3. **详细描述法**：
   - 每个 Prompt 都包含完整的角色描述
   - 使用一致的关键词和顺序
   - 保持风格参数（--s 值）一致

## 输出格式

```markdown
# 📚 漫画：[标题]

## 📋 漫画信息

| 项目 | 内容 |
|------|------|
| 标题 | [漫画标题] |
| 风格 | [选择的风格] |
| 布局 | [选择的布局] |
| 总页数 | [X] 页 |
| 总格数 | [Y] 格 |
| 画面比例 | [3:4 / 4:3 / 16:9] |

## 👥 角色设定

### 角色 1：[角色名]
- **外貌**：[详细描述]
- **服装**：[服装描述]
- **特征**：[独特特征]
- **性格**：[性格特点]

### 角色 2：[角色名]
[同上格式...]

---

## 🎬 故事大纲

### 第一幕：[标题]
[情节概述]

### 第二幕：[标题]
[情节概述]

### 第三幕：[标题]
[情节概述]

---

## 📖 分镜脚本

### 第 1 页

#### 格 1：[场景简述]

**分镜信息**：
- 格子大小：[大格/中格/小格]
- 镜头类型：[远景/全景/中景/特写/大特写]
- 镜头角度：[平视/俯视/仰视/倾斜]
- 构图：[三分法/对称/对角线/框架式]

**画面描述**：
- **场景**：[环境、时间、天气、氛围]
- **人物**：[角色、位置、姿势、表情、动作]
- **前景**：[前景元素]
- **中景**：[主体内容]
- **背景**：[背景细节]
- **光线**：[光源、方向、强度、色温]
- **色彩**：[主色调、对比色、情绪色]
- **焦点**：[视觉焦点、引导线]
- **情绪**：[要传达的情绪和氛围]

**对话**：
- [角色名]：「[台词]」

**旁白**：
[旁白文字]

**音效**：
[音效描述，如需要]

**Midjourney Prompt**：
```
[角色完整描述], [动作和表情], [场景环境],
[镜头类型] shot, [镜头角度] angle,
[风格名称] comic style, [具体风格特征],
[光线描述], [色彩方案],
clean linework, professional comic art,
sequential art, panel layout
--ar [比例] --v 6.1 --s [风格化值]
--cref [角色参考图 URL，如有]
--sref [风格参考图 URL，如有]
--no text, watermark, speech bubbles
```

**DALL-E 3 Prompt**：
```
Comic panel: [完整场景描述，包含角色、动作、环境、光线]
[风格名称] comic art style, [具体风格特征]
[镜头类型和角度描述]
Professional sequential art, clean composition
No text or speech bubbles
```

**Stable Diffusion Prompt**：
```
Positive: [角色], [动作], [场景], [风格], [质量标签]
comic panel, manga style, professional artwork,
detailed background, dynamic composition,
[光线和色彩描述]

Negative: text, speech bubbles, watermark, signature,
blurry, low quality, deformed, ugly, bad anatomy
```

---

#### 格 2：[场景简述]

[同上格式...]

---

### 第 2 页

[同上格式...]

---

## 🎨 风格指南

### 视觉风格：[选择的风格]
[风格的详细描述和特点]

### 色彩方案
- **主色**：[HEX] - [用途]
- **辅色**：[HEX] - [用途]
- **强调色**：[HEX] - [用途]
- **背景色**：[HEX] - [用途]

### 线条风格
- 线条粗细：[描述]
- 线条质感：[描述]
- 阴影处理：[描述]

### 角色一致性要点
- [关键特征1]
- [关键特征2]
- [关键特征3]

---

## 🎬 分镜技术

### 镜头语言

| 镜头类型 | 用途 | 情绪效果 |
|---------|------|---------|
| 远景 (Extreme Long Shot) | 建立场景、展示环境 | 宏大、孤独 |
| 全景 (Long Shot) | 展示人物全身和环境 | 客观、叙事 |
| 中景 (Medium Shot) | 展示人物上半身 | 对话、互动 |
| 特写 (Close-up) | 展示面部表情 | 情感、细节 |
| 大特写 (Extreme Close-up) | 展示局部细节 | 强调、紧张 |

### 镜头角度

| 角度 | 效果 | 适用场景 |
|------|------|---------|
| 平视 (Eye Level) | 客观、中立 | 日常对话 |
| 俯视 (High Angle) | 渺小、脆弱 | 展示弱势 |
| 仰视 (Low Angle) | 强大、威严 | 展示力量 |
| 倾斜 (Dutch Angle) | 不安、混乱 | 紧张场景 |

### 构图法则

1. **三分法**：将画面分为九宫格，重点放在交叉点
2. **对称构图**：平衡、稳定、正式
3. **对角线构图**：动态、引导视线
4. **框架式构图**：聚焦、深度感
5. **留白构图**：呼吸感、情绪空间

---

## 📐 技术参数详解

### Midjourney 参数

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `--ar` | 画面比例 | 3:4 (竖版) / 4:3 (横版) / 16:9 (宽屏) |
| `--v` | 版本 | 6.1 (最新) |
| `--s` | 风格化程度 | 100-300 (漫画) |
| `--c` | 混乱度 | 0-100 (默认 0) |
| `--cref` | 角色参考 | [图片 URL] |
| `--cw` | 角色权重 | 0-100 (默认 100) |
| `--sref` | 风格参考 | [图片 URL] |
| `--sw` | 风格权重 | 0-1000 (默认 100) |
| `--no` | 排除元素 | text, watermark, speech bubbles |

### 角色一致性最佳实践

1. **第一格生成后**：
   - 保存角色图片 URL
   - 在后续所有格中使用 `--cref [URL]`

2. **详细描述法**：
   ```
   [角色名], [年龄] years old, [性别],
   [发型和颜色], [脸型], [眼睛特征],
   wearing [服装详细描述],
   [独特特征如眼镜、疤痕等]
   ```

3. **保持参数一致**：
   - 所有格使用相同的 `--s` 值
   - 所有格使用相同的 `--v` 版本
   - 保持风格关键词一致

### 图像生成工作流

1. **生成角色参考**：
   ```
   Character design sheet: [角色完整描述]
   Multiple angles: front view, side view, back view
   [风格] comic style, clean linework
   --ar 16:9 --v 6.1 --s 200
   ```

2. **生成分镜**：
   - 使用角色参考 URL
   - 按页面顺序生成
   - 检查一致性

3. **后期处理**：
   - 添加对话框和文字
   - 调整色彩平衡
   - 统一风格
   - 添加音效文字

---

## 🔧 集成工具建议

### 图像生成工具

1. **Midjourney**（推荐）：
   - 最适合漫画风格
   - 角色一致性最好（--cref）
   - 风格控制精确

2. **DALL-E 3**：
   - 适合写实风格
   - 文字理解能力强
   - 安全性高

3. **Stable Diffusion**：
   - 可控性最强
   - 需要调参经验
   - 可本地部署

### 后期处理工具

1. **对话框添加**：
   - Clip Studio Paint
   - Photoshop
   - Krita (免费)

2. **色彩调整**：
   - Photoshop
   - GIMP (免费)

3. **排版工具**：
   - InDesign
   - Affinity Publisher
   - Canva

### 自动化工具

1. **批量生成**：
   - Midjourney Bot
   - ComfyUI (SD)

2. **角色库管理**：
   - 建立角色参考图库
   - 记录 --cref URL
   - 保存成功的 Prompt

---

## 💡 专业技巧

### 提升画面质量

1. **质量关键词**：
   ```
   professional comic art, high quality, detailed,
   clean linework, sharp focus, well composed,
   masterpiece, best quality
   ```

2. **避免关键词**：
   ```
   --no text, watermark, signature, speech bubbles,
   blurry, low quality, deformed, ugly, bad anatomy,
   extra limbs, poorly drawn
   ```

### 角色表情库

建立常用表情的 Prompt 模板：
- 惊讶：eyes wide open, mouth agape, raised eyebrows
- 愤怒：furrowed brows, clenched teeth, intense glare
- 悲伤：downcast eyes, slight frown, tears
- 喜悦：bright smile, sparkling eyes, relaxed posture
- 困惑：tilted head, questioning look, hand on chin
- 恐惧：wide eyes, pale face, trembling

### 动作姿势库

常用动作的描述模板：
- 奔跑：running pose, dynamic motion, speed lines
- 战斗：fighting stance, action pose, impact effect
- 思考：sitting, hand on chin, contemplative
- 对话：facing each other, gesturing, engaged
- 惊讶：stepping back, defensive posture, shocked
```

## 风格详解

### 1. Classic（传统清线风格）⭐

**特点**：
- 统一的清晰轮廓线
- 平涂色彩，少阴影
- 细致的背景描绘
- 欧洲漫画传统（丁丁历险记风格）

**适合场景**：
- 传记故事
- 科学家生平
- 历史事件
- 平衡叙事

**Prompt 模板**：
```
[主体], ligne claire style, clean uniform outlines,
flat colors, detailed background, European comic aesthetic,
clear composition, professional comic art
--ar 3:4 --v 6.1 --s 200
```

---

### 2. Dramatic（戏剧化风格）

**特点**：
- 高对比度
- 重阴影和明暗对比
- 强烈的表情
- 棱角分明的构图

**适合场景**：
- 重大发现时刻
- 冲突场景
- 高潮情节
- 紧张氛围

**Prompt 模板**：
```
[主体], dramatic comic style, high contrast,
heavy shadows, intense expressions, angular composition,
noir aesthetic, dynamic lighting
--ar 3:4 --v 6.1 --s 300
```

---

### 3. Warm（温暖风格）

**特点**：
- 柔和的边缘
- 金色调和暖色系
- 温馨的室内场景
- 怀旧感

**适合场景**：
- 个人故事
- 童年回忆
- 师徒关系
- 温情时刻

**Prompt 模板**：
```
[主体], warm comic style, soft edges,
golden tones, cozy interiors, nostalgic feel,
gentle lighting, heartwarming atmosphere
--ar 3:4 --v 6.1 --s 200
```

---

### 4. Tech（科技风格）

**特点**：
- 精确的几何线条
- 电路图案和科技元素
- 霓虹色调
- 深色背景

**适合场景**：
- 计算机历史
- AI 故事
- 现代科技
- 未来主题

**Prompt 模板**：
```
[主体], futuristic tech comic style,
precise geometric lines, circuit patterns,
neon accents, dark background, cyberpunk aesthetic,
digital art style
--ar 3:4 --v 6.1 --s 300
```

---

### 5. Sepia（复古风格）

**特点**：
- 老照片效果
- 泛黄纸张质感
- 时代准确的细节
- 怀旧氛围

**适合场景**：
- 1950 年前的故事
- 古典科学
- 历史人物
- 年代感内容

**Prompt 模板**：
```
[主体], vintage sepia comic style,
aged paper effect, period-accurate details,
nostalgic atmosphere, historical illustration,
classic engraving style
--ar 3:4 --v 6.1 --s 200
```

---

### 6. Vibrant（活力风格）

**特点**：
- 充满活力的线条
- 明亮的色彩
- 动态的姿势
- 年轻化风格

**适合场景**：
- 科学解释
- "顿悟"时刻
- 年轻受众
- 活力主题

**Prompt 模板**：
```
[主体], vibrant comic style, energetic lines,
bright colors, dynamic poses, youthful aesthetic,
expressive characters, lively composition
--ar 3:4 --v 6.1 --s 250
```

---

### 7. Ohmsha（日式技术漫画）

**特点**：
- 视觉隐喻和比喻
- 可爱的小道具
- 学生/导师互动
- 教学式对话

**适合场景**：
- 技术教程
- 复杂概念（机器学习、物理）
- 知识科普
- 教育内容

**Prompt 模板**：
```
[主体], Japanese manga guide style,
visual metaphors, cute gadgets, teacher-student dynamic,
educational manga aesthetic, clear explanations,
friendly characters
--ar 3:4 --v 6.1 --s 200
```

---

### 8. Realistic（写实漫画）

**特点**：
- 全彩写实风格
- 数字绘画质感
- 平滑的渐变
- 准确的比例

**适合场景**：
- 美食、美酒
- 商业故事
- 生活方式
- 专业话题

**Prompt 模板**：
```
[主体], realistic manga style, full color,
digital painting, smooth gradients, accurate proportions,
professional illustration, detailed rendering
--ar 3:4 --v 6.1 --s 150
```

---

## 布局详解

### 1. Standard（标准布局）

- **格数**：4-6 格/页
- **适合**：对话、叙事流程
- **节奏**：平稳、易读

### 2. Cinematic（电影感布局）

- **格数**：2-4 格/页
- **适合**：戏剧性时刻、场景建立
- **节奏**：舒缓、有张力

### 3. Dense（密集布局）

- **格数**：6-9 格/页
- **适合**：技术解释、时间线
- **节奏**：快速、信息密集

### 4. Splash（大格布局）

- **格数**：1-2 大格/页
- **适合**：关键时刻、揭示
- **节奏**：震撼、强调

### 5. Mixed（混合布局）

- **格数**：3-7 格变化
- **适合**：复杂叙事、情感弧线
- **节奏**：灵活、富有变化

### 6. Webtoon（条漫布局）

- **格数**：3-5 格竖向
- **适合**：移动阅读、教程
- **节奏**：连续、流畅

---

## 工作流程

### 第一步：内容分析与角色设计

1. **提取核心元素**
   - 关键情节点
   - 主要角色
   - 场景设定
   - 情感曲线

2. **角色设计**
   - 外貌特征定义
   - 服装风格设计
   - 性格特点
   - 生成角色参考图

### 第二步：故事结构设计

1. **三幕式结构**
   - 第一幕：建立（Setup）
   - 第二幕：对抗（Confrontation）
   - 第三幕：解决（Resolution）

2. **节奏规划**
   - 开场：吸引注意
   - 发展：推进情节
   - 高潮：情感爆发
   - 结局：情绪落地

### 第三步：分镜设计

1. **确定每页格数**
   - 根据布局类型
   - 考虑叙事节奏
   - 平衡信息密度

2. **设计每格构图**
   - 选择镜头类型
   - 确定镜头角度
   - 规划视觉引导
   - 安排对话和旁白

### 第四步：生成 Prompt

1. **角色一致性**
   - 使用 --cref 参数
   - 保持描述一致
   - 统一风格参数

2. **画面质量**
   - 添加质量关键词
   - 排除负面元素
   - 优化技术参数

3. **输出多平台 Prompt**
   - Midjourney（推荐）
   - DALL-E 3
   - Stable Diffusion

### 第五步：图像生成与后期

1. **生成图像**
   - 按顺序生成
   - 检查一致性
   - 必要时重新生成

2. **后期处理**
   - 添加对话框
   - 调整色彩
   - 统一风格
   - 添加音效文字

---

## 示例

### 示例 1：图解机器学习

**输入**：
```
主题：机器学习的工作原理
内容：解释监督学习、训练过程、模型预测
风格：ohmsha
布局：standard
```

**输出**：
```markdown
# 📚 知识漫画：机器学习入门

## 第 1 页

### 格 1：开场

**画面**：
- 场景：教室，黑板上写着"机器学习"
- 人物：老师（戴眼镜的机器人）和学生（好奇的小女孩）
- 焦点：老师指着黑板
- 情绪：友好、欢迎

**对话**：
- 老师：「今天我们来学习机器学习！」
- 学生：「听起来好复杂...」

**Midjourney Prompt**：
```
Friendly robot teacher with glasses pointing at blackboard 
with "Machine Learning" written, curious young student sitting,
Japanese manga guide style, educational manga aesthetic,
classroom setting, warm lighting, cute characters
--ar 3:4 --v 6.1 --s 200 --no text
```

### 格 2：什么是机器学习

**画面**：
- 场景：思维泡泡中展示大脑和电脑连接
- 人物：学生在思考
- 焦点：大脑-电脑连接的视觉隐喻
- 情绪：好奇、理解

**旁白**：
机器学习就是让电脑像人一样学习！

**Midjourney Prompt**：
```
Thought bubble showing brain connected to computer,
visual metaphor for machine learning, cute illustration style,
Japanese manga guide aesthetic, simple and clear,
educational diagram
--ar 3:4 --v 6.1 --s 200 --no text
```

[继续...]
```

---

### 示例 2：图灵的故事

**输入**：
```
主题：艾伦·图灵的生平
内容：图灵的童年、破译密码、计算机理论
风格：classic
布局：cinematic
```

**输出**：
```markdown
# 📚 知识漫画：图灵传

## 第 1 页

### 格 1：童年（大格）

**画面**：
- 场景：1920 年代英国乡村，小图灵在观察花朵
- 人物：8 岁的图灵，专注的表情
- 焦点：图灵的眼睛和花朵的细节
- 情绪：好奇、专注

**旁白**：
1912 年，艾伦·图灵出生在伦敦。
从小，他就对自然界的规律着迷。

**Midjourney Prompt**：
```
Young Alan Turing age 8 observing flowers in 1920s English countryside,
ligne claire style, clean uniform outlines, flat colors,
detailed background, European comic aesthetic, nostalgic atmosphere,
professional comic art
--ar 4:3 --v 6.1 --s 200 --no text
```

[继续...]
```

---

## 注意事项

### ⚠️ 内容设计

- 每格信息量不要过大（1-2 个要点）
- 对话要简洁（每句不超过 20 字）
- 视觉和文字要互补，不要重复
- 注意节奏，避免单调

### ⚠️ 视觉设计

- 保持风格一致性
- 注意人物造型的连贯性
- 背景不要过于复杂
- 留白要适当

### ⚠️ Prompt 生成

- 避免在 Prompt 中包含文字内容
- 使用 `--no text` 参数
- 后期再添加对话框和文字
- 保持 Prompt 简洁清晰

### ⚠️ 技术限制

- AI 绘图可能需要多次生成
- 人物一致性需要额外注意
- 复杂场景可能需要分步生成
- 建议使用 Midjourney 的 `--cref` 参数保持角色一致

---

## 最佳实践

### 💡 叙事技巧

1. **开头要抓人**：第一格决定读者是否继续
2. **节奏要变化**：快慢结合，避免单调
3. **高潮要突出**：用大格或特殊构图
4. **结尾要有力**：留下深刻印象

### 💡 视觉技巧

1. **视角变化**：远景、中景、特写交替
2. **构图对比**：静态和动态结合
3. **色彩情绪**：用色彩传达情绪
4. **视觉引导**：用线条引导视线

### 💡 教育效果

1. **化繁为简**：用视觉隐喻简化概念
2. **循序渐进**：从简单到复杂
3. **重复强化**：关键概念多次出现
4. **互动感**：让读者有参与感

---

## 参考资源

### 漫画风格参考
- **Ligne Claire**：丁丁历险记、蓝精灵
- **Ohmsha**：《漫画算法》系列、《漫画统计学》
- **写实漫画**：《神之雫》、《孤独的美食家》

### 教育漫画案例
- **Logicomix**：逻辑学漫画
- **Feynman**：费曼传记漫画
- **The Thrilling Adventures of Lovelace and Babbage**：计算机历史漫画

### 工具推荐
- **Midjourney**：最适合漫画风格
- **DALL-E 3**：适合写实风格
- **Stable Diffusion**：可控性强，需要调参

---

## 适用场景

- 🎨 **原创漫画**：故事创作、角色设计
- 📖 **内容可视化**：将文字内容转化为漫画
- 👤 **人物传记**：历史人物、名人故事
- 🔬 **概念解释**：复杂概念的视觉化
- 📚 **叙事作品**：小说改编、剧本可视化
- 💼 **商业故事**：品牌故事、产品介绍

---

## 扩展阅读

- [Understanding Comics](https://en.wikipedia.org/wiki/Understanding_Comics) - Scott McCloud
- [Making Comics](https://en.wikipedia.org/wiki/Making_Comics) - Scott McCloud
- [漫画分镜技法](https://book.douban.com/subject/26297117/)

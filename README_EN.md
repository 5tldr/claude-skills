# Claude Skills Collection (Chinese Edition)

> Curated Claude Skills for Chinese users, focusing on content creation and development efficiency

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-16-blue.svg)](./skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Ready-green.svg)](https://claude.ai)

English | [中文](./README.md)

## What are Claude Skills?

Skills are modular capability extensions introduced by Anthropic. Write your experience, processes, and instructions into `SKILL.md` files, and Claude will automatically load them when needed.

**Key Benefits**:
- 🎯 On-demand loading (~100 tokens for metadata scan, <5k tokens for full load)
- 🔄 Create once, use everywhere
- 📦 Composable - stack multiple Skills
- 🌐 Cross-platform: Claude.ai / Claude Code / API
- 🎨 Customizable: Override defaults via EXTEND.md

## Skills List

### 📱 Content Creation (7 Skills)

| Skill | Purpose | Source |
|-------|---------|--------|
| [xiaohongshu-writer](./skills/xiaohongshu-writer/) | Xiaohongshu (RedNote) viral post generator | Localized |
| [wechat-article](./skills/wechat-article/) | WeChat Official Account article generator | Localized |
| [douyin-script](./skills/douyin-script/) | Douyin (TikTok) short video script | Localized |
| [ecommerce-copywriter](./skills/ecommerce-copywriter/) | E-commerce copy (Taobao/JD/Pinduoduo) | Localized |
| [bilibili-summarizer](./skills/bilibili-summarizer/) | Bilibili video content summarizer | Localized |
| [article-image-generator](./skills/article-image-generator/) | Article image generator (input content → output Prompt) | Based on [claudekit-skills](https://github.com/mrgoonie/claudekit-skills) |
| [knowledge-comic](./skills/knowledge-comic/) | Comic creator (8 styles × 6 layouts + character consistency) | Based on [baoyu-skills](https://github.com/JimLiu/baoyu-skills) |

### 📊 Trending Analysis (3 Skills)

| Skill | Purpose | Source |
|-------|---------|--------|
| [xiaohongshu-trending](./skills/xiaohongshu-trending/) | Xiaohongshu trending topics analysis | Localized |
| [douyin-trending](./skills/douyin-trending/) | Douyin trending analysis | Localized |
| [weibo-hot](./skills/weibo-hot/) | Weibo hot search sentiment analysis | Localized |

### 💻 Development Tools (3 Skills)

| Skill | Purpose | Source |
|-------|---------|--------|
| [code-reviewer-cn](./skills/code-reviewer-cn/) | Code review (Chinese reports) | Based on [anthropics/skills](https://github.com/anthropics/skills) |
| [test-driven-development](./skills/test-driven-development/) | Test-driven development | Based on [obra/superpowers](https://github.com/obra/superpowers) |
| [systematic-debugging](./skills/systematic-debugging/) | Systematic debugging | Based on [obra/superpowers](https://github.com/obra/superpowers) |

### 💼 Workplace Efficiency (3 Skills)

| Skill | Purpose | Source |
|-------|---------|--------|
| [meeting-notes-cn](./skills/meeting-notes-cn/) | Meeting notes organizer | Localized |
| [resume-optimizer-cn](./skills/resume-optimizer-cn/) | Resume optimizer (Chinese job market) | Localized |
| [email-writer-cn](./skills/email-writer-cn/) | Chinese business email writer | Localized |

## Quick Start

### Prerequisites

- Claude Pro/Max/Team/Enterprise subscription (for Claude.ai)
- Or Claude Code (recommended for developers)

### Installation

#### Method 1: Claude Code Plugin Marketplace (Recommended) ⭐

```bash
# Run in Claude Code
/plugin add https://github.com/5tldr/claude-skills

# Or simply tell Claude Code
"Please install Skills from github.com/5tldr/claude-skills"
```

**Update Skills**:
```bash
/plugin
# Switch to Marketplaces tab
# Select claude-skills → Update marketplace
```

#### Method 2: Claude.ai Manual Upload

1. Open [Claude.ai](https://claude.ai)
2. Settings → Capabilities → Enable Skills
3. Download this repo, compress skills folder to .zip
4. Upload in Skills settings

#### Method 3: Local Clone

```bash
git clone https://github.com/5tldr/claude-skills.git
cd claude-skills
```

#### Method 4: Direct Copy

Copy any `SKILL.md` content to use as System Prompt.

## Skill File Structure

```
skill-name/
├── SKILL.md          # Required: Instructions and metadata
├── EXTEND.md         # Optional: Custom config (not committed)
└── examples/         # Optional: Example files
```

## Customization

All Skills support customization via `EXTEND.md` files without modifying source files.

### Configuration Priority

Config files are loaded in this order (later overrides earlier):

1. `skills/<skill-name>/SKILL.md` - Default config
2. `~/.claude-skills/<skill-name>/EXTEND.md` - User-level (personal preferences)
3. `.claude-skills/<skill-name>/EXTEND.md` - Project-level (team shared)

### Example: Customize Xiaohongshu Style

Create project-level config:

```bash
mkdir -p .claude-skills/xiaohongshu-writer
```

Write `.claude-skills/xiaohongshu-writer/EXTEND.md`:

```markdown
# Brand Style Customization

## Default Style
- Tone: More professional, less casual slang
- Emoji: Reduce usage by 50%
- Tags: Prioritize brand-related tags

## Brand Info
- Brand: [Your Brand]
- Category: [Product Category]
- Tone: Professional, trustworthy, warm
```

## References

### Official Resources
- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic Official Skills
- [Agent Skills Open Standard](https://agentskills.io)
- [Skills Official Docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

### Community Resources
- [obra/superpowers](https://github.com/obra/superpowers) - Software development methodology Skills
- [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - ClaudeKit Skills
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) - Baoyu's visual content creation Skills
- [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) - Community curated collection
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) - Another curated collection

## Contributing

Contributions of new Skills or improvements to existing ones are welcome!

### Creating a New Skill

1. Fork this repository
2. Create a new folder in `skills/`
3. Write `SKILL.md` file (refer to existing Skills)
4. Submit Pull Request

### Skill Naming Convention

- Use lowercase letters, numbers, and hyphens
- Format: `category-name` or `platform-action`
- Examples: `xiaohongshu-writer`, `code-reviewer-cn`

## FAQ

### Q: What's the difference between Skills and regular Prompts?

A: Skills are intelligently loaded. Claude scans all Skills' metadata and automatically decides which Skill to load based on conversation context. No manual selection or copy-paste needed.

### Q: Can I use multiple Skills simultaneously?

A: Yes. Multiple Skills can be stacked in the same conversation, and Claude will load them as needed.

### Q: Will EXTEND.md configs be committed to Git?

A: No. The `.claude-skills/` directory is in `.gitignore`. Teams can manually commit if sharing is needed.

### Q: How to update Skills?

A: 
- Claude Code marketplace: Run `/plugin` → Update marketplace
- Manual clone: `git pull origin main`
- Claude.ai: Re-download and upload

## License

MIT

---

> This project is curated from GitHub open source projects. Thanks to all contributors.

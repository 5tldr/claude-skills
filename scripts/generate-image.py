#!/usr/bin/env python3
"""
使用 OpenRouter + Gemini 2.5 Flash Image (Nano Banana) 生成文章配图
"""

import requests
import json
import os
import sys
import base64
import time

# OpenRouter API Key - 从环境变量读取
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

# 模型选择
MODEL = "google/gemini-3-pro-image-preview"  # Nano Banana Pro

def generate_image_openrouter(prompt: str, aspect_ratio: str = "16:9"):
    """调用 OpenRouter Gemini 2.5 Flash Image 生成图片"""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/skills",
        "X-Title": "Claude Skills Article"
    }
    
    # 构建请求
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "modalities": ["image", "text"],
        "image_config": {
            "aspect_ratio": aspect_ratio,
            "image_size": "2K"
        }
    }
    
    print(f"正在生成图片...")
    print(f"模型: {MODEL}")
    print(f"Prompt: {prompt[:100]}...")
    print(f"比例: {aspect_ratio}")
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=180
        )
        
        # 先打印响应，再检查状态
        result = response.json()
        if response.status_code != 200:
            print(f"❌ HTTP {response.status_code}")
            print(f"   错误: {json.dumps(result, indent=2, ensure_ascii=False)[:800]}")
            return None
        
        # 解析响应
        if "choices" in result and len(result["choices"]) > 0:
            message = result["choices"][0].get("message", {})
            images = message.get("images", [])
            
            if images:
                image_data = images[0].get("image_url", {}).get("url", "")
                if image_data.startswith("data:image"):
                    print(f"✅ 生成成功!")
                    return image_data
            
            # 有些模型返回格式不同
            content = message.get("content", "")
            print(f"响应内容: {content[:200] if content else '无'}")
            
        print(f"❌ 响应异常: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
        return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        if hasattr(e, 'response') and e.response:
            try:
                error_json = e.response.json()
                print(f"   错误详情: {json.dumps(error_json, indent=2, ensure_ascii=False)}")
            except:
                print(f"   响应: {e.response.text[:500]}")
        return None

def save_base64_image(data_url: str, filename: str):
    """保存 base64 图片到本地"""
    try:
        # 解析 data URL
        # 格式: data:image/png;base64,xxxxx
        if "," in data_url:
            header, base64_data = data_url.split(",", 1)
        else:
            base64_data = data_url
        
        # 解码并保存
        image_bytes = base64.b64decode(base64_data)
        
        with open(filename, "wb") as f:
            f.write(image_bytes)
        
        print(f"✅ 已保存: {filename} ({len(image_bytes) / 1024:.1f} KB)")
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


# 文章01的配图 Prompts - 哆啦A梦主题，符合文章上下文
# 文章主题：Claude Skills = AI技能插件，像哆啦A梦的四次元口袋
ARTICLE_01_PROMPTS = {
    "01_cover": {
        "prompt": """Create a Doraemon style anime illustration for an article about AI Skills.

Scene: A blue robot cat (like Doraemon) happily pulling out glowing skill cards from its 4D pocket. A young boy with glasses watches with amazement and excitement.

Elements:
- The robot cat's pocket glows with magical light
- 5-6 colorful floating cards coming out of the pocket, each with a simple icon (pen, code brackets, video camera, calendar, document)
- Sparkles and magic effects around the cards
- Bright blue sky with fluffy white clouds
- Text-free, clean composition

Style: Classic Doraemon anime art, warm colors, cheerful and magical mood. The scene represents "AI skills ready to use anytime, like magic tools from a pocket".""",
        "aspect_ratio": "16:9"
    },
    "02_pain_point": {
        "prompt": """Create a cute Doraemon style cartoon illustration showing frustration.

Scene: A classroom or study room. Nobita (boy with glasses) is crying at his messy desk. Gian (big chubby boy) is laughing at him. Shizuka (cute girl with short hair) looks worried and concerned.

Elements:
- Nobita: tears streaming, head on desk, surrounded by messy papers and sticky notes
- Gian: pointing and laughing, teasing Nobita
- Shizuka: standing nearby with a worried expression, wanting to help
- Desk covered with scattered papers, crumpled notes
- Cute cartoon style with big expressive eyes
- Soft pastel colors but slightly muted to show frustration

Style: Classic Doraemon cartoon, cute and expressive characters, comedic scene. No Doraemon robot cat in this scene.""",
        "aspect_ratio": "16:9"
    },
    "03_before_after": {
        "prompt": """Create a cute Doraemon style split-screen cartoon illustration with only Nobita and Doraemon.

LEFT SIDE (Before - sad):
- Nobita alone, crying at messy desk
- Scattered papers and sticky notes everywhere
- Gray and muted colors
- Sad and frustrated mood

RIGHT SIDE (After - happy):
- Nobita smiling happily with Doraemon beside him
- Doraemon's 4D pocket glowing
- Colorful skill cards floating in the air
- Bright cheerful colors with sparkles and magic effects

Style: Classic cute Doraemon cartoon, only these two characters, clear vertical split in middle. Simple and clean composition.""",
        "aspect_ratio": "16:9"
    },
    "04_skills_grid": {
        "prompt": """Create a cute Doraemon style cartoon illustration showing magical gadgets.

Scene: Doraemon, Nobita, Shizuka, and Gian standing together looking up at 6 floating magical gadgets in the sky. Everyone is amazed and excited.

Elements:
- Doraemon proudly presenting the gadgets from his pocket
- Nobita pointing excitedly at the gadgets
- Shizuka clasping hands with starry eyes
- Gian with mouth open in amazement
- 6 colorful floating gadgets with cute icons: pen, code, video, calendar, document, lightbulb
- Sparkles and magical effects around the gadgets
- Bright blue sky with fluffy clouds

Style: Cute Doraemon cartoon, all characters together as friends, magical and cheerful atmosphere. Big cute eyes on all characters.""",
        "aspect_ratio": "16:9"
    },
    "05_quote": {
        "prompt": """Create a Doraemon style illustration for an inspirational quote about AI Skills.

Scene: A peaceful sunset scene with the blue robot cat and the boy sitting together on a grassy hill, looking at the horizon. The robot cat's pocket glows softly.

Elements:
- Warm orange and purple sunset sky
- Silhouette style but still recognizable as Doraemon characters
- Large empty sky area in the upper portion (for text overlay)
- Peaceful, reflective mood
- Soft clouds and gentle lighting

Style: Doraemon anime style, emotional and inspiring. Represents "Skills turn experience into reusable assets - teaching AI instead of just using AI".""",
        "aspect_ratio": "1:1"
    }
}

def main():
    output_dir = "output/article-01-images"
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("文章01 配图生成")
    print("模型: Gemini 2.5 Flash Image (Nano Banana)")
    print("=" * 60)
    print()
    
    # 解析命令行参数
    if len(sys.argv) > 1:
        key = sys.argv[1]
        if key in ARTICLE_01_PROMPTS:
            prompts = {key: ARTICLE_01_PROMPTS[key]}
        elif key == "all":
            prompts = ARTICLE_01_PROMPTS
        else:
            print(f"可用选项: {list(ARTICLE_01_PROMPTS.keys())}")
            print("或 'all' 生成全部")
            return
    else:
        # 默认只生成封面图
        prompts = {"01_cover": ARTICLE_01_PROMPTS["01_cover"]}
    
    results = []
    
    for name, config in prompts.items():
        print(f"\n{'='*40}")
        print(f"生成: {name}")
        print(f"{'='*40}")
        
        image_data = generate_image_openrouter(
            prompt=config["prompt"],
            aspect_ratio=config["aspect_ratio"]
        )
        
        if image_data:
            filename = f"{output_dir}/{name}.png"
            if save_base64_image(image_data, filename):
                results.append({"name": name, "file": filename, "success": True})
            else:
                results.append({"name": name, "file": None, "success": False})
        else:
            results.append({"name": name, "file": None, "success": False})
        
        # 避免请求过快
        if len(prompts) > 1:
            print("等待 3 秒...")
            time.sleep(3)
    
    # 汇总结果
    print()
    print("=" * 60)
    print("生成完成!")
    print("=" * 60)
    
    success_count = sum(1 for r in results if r["success"])
    print(f"成功: {success_count}/{len(prompts)}")
    print(f"目录: {output_dir}")
    print()
    
    for r in results:
        status = "✅" if r["success"] else "❌"
        print(f"  {status} {r['name']}")
    
    # 保存结果记录
    with open(f"{output_dir}/results.json", "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()

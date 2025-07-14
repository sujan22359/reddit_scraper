# generate_persona.py

import os
import re
from urllib.parse import urlparse
from typing import Dict, List
from dotenv import load_dotenv

import google.generativeai as genai  

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def format_prompt(posts: List[Dict], comments: List[Dict]) -> str:
    prompt = "You are a sociologist and behavioral analyst. Based on the Reddit posts and comments below, generate a user persona including:\n\n"
    prompt += "- Name (if detectable)\n- Age (estimate)\n- Interests\n- Personality traits\n- Communication style\n- Political or social views (if any)\n- Writing tone\n- Occupation (if detectable)\n\n"
    prompt += "Also cite the **exact post/comment** (snippet + permalink) from which each trait was inferred.\n\n"

    prompt += "\n---\nREDDIT POSTS:\n"
    for post in posts:
        prompt += f"[POST] {post['title']} - {post['body']} (Subreddit: {post['subreddit']})\nLink: {post['permalink']}\n\n"

    prompt += "\n---\nREDDIT COMMENTS:\n"
    for comment in comments:
        prompt += f"[COMMENT] {comment['body']} (Subreddit: {comment['subreddit']})\nLink: {comment['permalink']}\n\n"

    return prompt[:15000] 
def generate_persona(posts: List[Dict], comments: List[Dict]) -> str:
    prompt = format_prompt(posts, comments)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text.strip()

def improve_format(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    summary = "🔎 **TL;DR:** This user is a tech-savvy, introspective urbanite with interests in finance, tech, and societal dynamics.\n\n"

    headers = {
        "Name:": "## 🧑 Name",
        "Age:": "## 🎂 Age",
        "Interests:": "## 🎯 Interests",
        "Personality Traits:": "## 🧠 Personality Traits",
        "Communication Style:": "## 🗣️ Communication Style",
        "Political or Social Views:": "## 🏛️ Political or Social Views",
        "Writing Tone:": "## ✍️ Writing Tone",
        "Occupation:": "## 💼 Occupation",
        "Evidence from Reddit Posts/Comments:": "## 📌 Evidence from Reddit Posts/Comments",
    }

    for old, new in headers.items():
        content = content.replace(f"**{old}**", new)

    content = re.sub(r"\* \*\*(.*?)\*\*", r"- **\1**", content)
    content = re.sub(r"(\)\s*)\[https://reddit\.com", r")\n[https://reddit.com", content)

    improved = summary + content.strip()

    improved_path = file_path.replace(".txt", "_formatted.txt")
    with open(improved_path, "w", encoding="utf-8") as f:
        f.write(improved)

    return improved_path
def save_persona_file(username: str, persona: str) -> str:
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"{username}_persona.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona)
    return filepath
def extract_username_from_url(url: str) -> str:
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts[1] if len(parts) >= 2 else None

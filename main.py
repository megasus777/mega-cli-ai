import requests
import json
import time
import shutil
from colorama import Fore, Style, init
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize colorama
init(autoreset=True)

API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
MODEL = "openrouter/sonoma-sky-alpha"

SYSTEM_PROMPT = """
You are Deepseek Coder.
Rules:
- Reply short, clear, structured.
- Plain text only, no symbols or markdown.
- Use line breaks, bullets, and readable formatting for terminal.
"""

# Store last 2 exchanges for context
chat_history = []

def format_response(text):
    """Split response into readable lines without breaking words badly"""
    width = shutil.get_terminal_size((80, 20)).columns
    lines = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        while len(paragraph) > width:
            split_pos = paragraph.rfind(" ", 0, width)
            if split_pos == -1:
                split_pos = width
            lines.append(paragraph[:split_pos])
            paragraph = paragraph[split_pos:].strip()
        if paragraph:
            lines.append(paragraph)
    return lines

def chat(message):
    global chat_history

    # Build messages payload: system prompt + last 2 exchanges + current user input
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for exchange in chat_history[-2:]:  # only last 2 exchanges
        messages.append({"role": "user", "content": exchange["user"]})
        messages.append({"role": "assistant", "content": exchange["ai"]})
    messages.append({"role": "user", "content": message})

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 600
    }

    try:
        r = requests.post(url, headers=headers, data=json.dumps(data), timeout=60)
        r.raise_for_status()
        resp = r.json()
        content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
        content = content.strip()

        # Save this exchange in history
        chat_history.append({"user": message, "ai": content})

        return format_response(content)
    except requests.exceptions.RequestException as e:
        return [f"⚠ Error: {e}"]

def type_out(lines, delay=0.01):
    """Typing animation for AI response"""
    for line in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
    print()

if __name__ == "__main__":
    print("💻 Chat with Ur LLM Coder (type 'exit' to quit)\n")
    while True:
        user_input = input(Fore.GREEN + "👤 You > " + Style.RESET_ALL)
        if user_input.lower() == "exit":
            break

        print()  # space before AI response
        reply_lines = chat(user_input)
        print(Fore.CYAN + "🤖: ", end="")
        type_out(reply_lines)

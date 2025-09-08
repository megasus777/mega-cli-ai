# Mega-cli-ai

mega-cli-ai project is a terminal-based AI coding assistant powered by OpenRouter LLM.  
It provides concise, structured, and readable responses for programming questions directly in your terminal.

---

## Features

- Short, clear, and structured AI responses.
- Real-time typing animation for a ChatGPT-like experience.
- Retains last 2 interactions for context memory.
- Perfect formatting for easy reading in terminal.
- Works on Linux terminals (Kali, Ubuntu, etc.), Also on Windows WSL and Termux as Well.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/megasus777/mega-cli-ai.git
cd mega-cli-ai
```
2. **Install The required packages:**
```bash
python install requirements.txt
```
3. **Get ur API-KEY from openrouter website and put it in a .env file and name it ``OPEN_ROUTER_API_KEY`` Then Run:**
```bash
python install requirements.txt
```
4. **And Finally Run The LLM and Enjoy:**
```bash
python main.py
```
## Bonus
***Use the following command in ur terminal to create an alias (shortcut) that what when u will type it the LLM will Run without typing ``python main.py`` each time u wanna use it:***
```bash
alias llm='python ~/path-to-ur/main.py'
```
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
2. **Get ur API-KEY from openrouter website and put it in a .env file and name it ``OPEN_ROUTER_API_KEY`` Then Run:**
```bash
pip install -r requirements.txt
```
3. **And Finally Run The LLM and Enjoy:**
```bash
python main.py
```
## Bonus
***Use the following command in ur terminal to create an alias (shortcut) that when u will type it the LLM will Run without typing ``python main.py`` each time u wanna use it:***
```bash
# open your ~/.zshrc or ~/.bashrc then add the following command in the end of the file then save it.
alias llm='python ~/path-to-ur/main.py'
```
***Then  if u wanna run it just type ``llm`` in your terminal and the llm /ai will run in ur opening terminal session.***

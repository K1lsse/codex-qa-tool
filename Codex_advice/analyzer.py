from client import call_codex
from prompts import build_log_prompt

def analyze_log(log_text: str):
    prompt = build_log_prompt(log_text)
    result = call_codex(prompt)
    return result
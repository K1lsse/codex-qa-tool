from tools.log_tools import analyze_log
from core.llm import ask_llm


def route(user_input: str):
    text = user_input.strip()
    lower_text = text.lower()

    # 支持: log / log xxx.log / 分析日志
    if lower_text == "log" or "日志" in text:
        return analyze_log("logs/sample.log")

    if lower_text.startswith("log "):
        log_path = text[4:].strip()
        if not log_path:
            return "[提示] 请输入日志路径，例如: log logs/sample.log"
        return analyze_log(log_path)

    return ask_llm(user_input)

from tools.log_tools import analyze_log
from core.llm import ask_llm
def route(user_input: str):

    text = user_input.lower()

    # log分析
    if "log" in text:
        return analyze_log("logs/test.log")

    # 默认走LLM
    return ask_llm(user_input)
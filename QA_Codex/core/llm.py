from openai import OpenAI
from core.config import Config


client = None
if Config.TOKENESS_API_KEY:
    client = OpenAI(
        api_key=Config.TOKENESS_API_KEY,
        base_url=Config.TOKENESS_BASE_URL
    )


def ask_llm(prompt: str):
    if not Config.TOKENESS_API_KEY:
        return "[LLM不可用] 请先在 .env 中配置 TOKENESS_API_KEY"

    try:
        resp = client.chat.completions.create(
            model=Config.MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"[LLM调用失败] {e}"

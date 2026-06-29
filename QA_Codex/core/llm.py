from openai import OpenAI
from core.config import Config

client = OpenAI(
    api_key=Config.TOKENESS_API_KEY,
    base_url=Config.TOKENESS_BASE_URL
)

def ask_llm(prompt: str):

    resp = client.chat.completions.create(
        model=Config.MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return resp.choices[0].message.content
from openai import OpenAI

client = OpenAI(
    api_key="sk-XTu6HMB6wE4mc7Za2Z25Sq008yJXmCMVuh8Kq10gJDspkq6h",
    base_url="https://n.tokeness.io/v1"
)

def call_codex(prompt: str):
    response = client.chat.completions.create(
        model="codex-auto-review",
        messages=[
            {"role": "system", "content": "你是资深QA工程师，擅长找bug和分析系统问题"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
from core.router import route


def chat_loop():
    print("===== QA Codex v0.3 =====")

    while True:
        user_input = input("请输入>>> ").strip()

        if not user_input:
            print("请输入内容后再试。")
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("bye")
            break

        try:
            result = route(user_input)
            print(result)
        except Exception as e:
            print(f"[系统错误] {e}")

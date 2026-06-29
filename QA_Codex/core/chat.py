from core.router import route

def chat_loop():
    print("===== QA Codex v0.2 =====")

    while True:
        user_input = input("请输入>>> ")

        if user_input.lower() in ["exit", "quit"]:
            print("bye 👋")
            break

        result = route(user_input)
        print(result)
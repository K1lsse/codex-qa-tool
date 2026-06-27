from analyzer import analyze_log

if __name__ == "__main__":
    print("=== QA Codex Tool ===")

    with open("samples/Sample.log", "r", encoding="utf-8") as f:
        log = f.read()

    result = analyze_log(log)

    print("\n===== ANALYSIS RESULT =====\n")
    print(result)
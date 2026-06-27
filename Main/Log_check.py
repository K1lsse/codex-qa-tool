# log_check_function.py

log_file = "sample.log"
keywords = ["error", "fail", "crash", "timeout", "exception", "panic", "fatal", "disconnect"]

# 封装函数：检查一行是否包含关键词
def contains_keyword(line, keywords_list):
    """
    line: 字符串，当前日志行
    keywords_list: 关键字列表
    返回 True/False
    """
    lower_line = line.lower()
    for keyword in keywords_list:
        if keyword in lower_line:
            return True
    return False

# 打开 result.txt 文件准备写入
with open("result.txt", "w", encoding="utf-8") as result_file:
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line_number, line in enumerate(f, start=1):
            if contains_keyword(line, keywords):
                result_file.write(f"Line {line_number}: {line.strip()}\n")
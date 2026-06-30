import os


def analyze_log(path: str) -> str:
    if not os.path.exists(path):
        return f"[log分析失败] 文件不存在: {path}"

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        return f"[log分析失败] 无法读取文件: {e}"

    total_lines = len(lines)
    error_lines = []
    warn_lines = []

    for line in lines:
        upper_line = line.upper()
        if "ERROR" in upper_line:
            error_lines.append(line.strip())
        if "WARN" in upper_line or "WARNING" in upper_line:
            warn_lines.append(line.strip())

    preview = []
    if error_lines:
        preview.append("ERROR样例:")
        preview.extend(error_lines[:3])

    if warn_lines:
        preview.append("WARN样例:")
        preview.extend(warn_lines[:3])

    if not preview:
        preview.append("未发现 ERROR 或 WARN 关键字")

    return (
        f"[log分析完成]\n"
        f"文件: {path}\n"
        f"总行数: {total_lines}\n"
        f"ERROR 数量: {len(error_lines)}\n"
        f"WARN 数量: {len(warn_lines)}\n"
        f"{chr(10).join(preview)}"
    )

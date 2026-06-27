def build_log_prompt(code: str):
    return f"""
你是资深SDET工程师，请分析以下代码：

1. 是否存在bug
2. 是否有边界问题
3. 是否存在性能风险
4. 给出优化建议
5. 如果可能，请补充测试用例

代码如下：
{code}
"""
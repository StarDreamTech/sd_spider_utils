def clean_text(text: str) -> str:
    # 替换非断空白符为普通空格
    text = text.replace("\xa0", " ")
    # 移除字符串两端的空格
    text = text.strip()
    # 替换多个空格为单个空格
    text = " ".join(text.split())
    # 移除多余的标点符号，例如连续的逗号或逗号后面紧跟空格
    text = text.replace(" ,", ",").replace(", ,", ",")
    return text


def contains_chinese(text: str) -> bool:
    """
    使用正则表达式检查是否包含汉字
    """
    import re

    return bool(re.search(r"[\u4e00-\u9fa5]", text))


def contains_date(text: str) -> bool:
    """
    使用正则表达式检查是否包含类似 '2022年03月30日' 的日期
    """
    import re

    return bool(re.search(r"\d{4}[-/年]\d{1,2}[-/月]\d{1,2}日?", text))


if __name__ == "__main__":
    """
    文本是否包含中文
    """
    text1: str = "This is a te{||||  nmakldnsjdmksxm  15651654 st.把那家伙半小时·"
    text2: str = "这是一个测试。"

    print(contains_chinese(text1))  # False
    print(contains_chinese(text2))  # True

    # 测试
    text1: str = "今天是2022年03月30日，天气晴。"
    text2: str = "这是一个没有日期的文本。"
    text3: str = "今天是2022 03 30。"

    print(contains_date(text1))  # True
    print(contains_date(text2))  # False
    print(contains_date(text3))  # False

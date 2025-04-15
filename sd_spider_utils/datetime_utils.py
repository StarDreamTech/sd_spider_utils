from typing import List
from datetime import datetime
import re


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
    return bool(re.search(r"[\u4e00-\u9fa5]", text))


def contains_date(text: str) -> bool:
    """
    使用正则表达式检查是否包含类似 '2022年03月30日' 的日期
    """
    return bool(re.search(r"\d{4}[-/年]\d{1,2}[-/月]\d{1,2}日?", text))


def extract_dates(text: str) -> List[datetime]:
    """
    提取文本中所有的日期并返回 datetime 对象列表
    支持格式如: 2022年03月30日, 2022-03-30, 2022/03/30
    """
    # 正则表达式匹配日期
    pattern: str = r"\d{4}[-/年]\d{1,2}[-/月]\d{1,2}日?"
    matches = re.findall(pattern, text)

    dates: List[datetime] = []
    for match in matches:
        # 替换中文字符为标准分隔符
        normalized = match.replace("年", "-").replace("月", "-").replace("日", "")
        try:
            # 将字符串转换为 datetime 对象
            date_obj = datetime.strptime(normalized, "%Y-%m-%d")
            dates.append(date_obj)
        except ValueError:
            # 如果转换失败，跳过这个匹配
            continue

    return dates


if __name__ == "__main__":
    # 测试日期提取
    test_text: str = "今天是2022年03月30日，昨天是2022-03-29，明天是2022/03/31。"
    dates: List[datetime] = extract_dates(test_text)
    for date in dates:
        print(f"Found date: {date.strftime('%Y-%m-%d')}")  # 格式化输出日期

    # 原有的测试代码
    text1: str = "This is a te{||||  nmakldnsjdmksxm  15651654 st.把那家伙半小时·"
    text2: str = "这是一个测试。"
    print(contains_chinese(text1))  # False
    print(contains_chinese(text2))  # True

    text3: str = "今天是2022年03月30日，天气晴。"
    text4: str = "这是一个没有日期的文本。"
    print(contains_date(text3))  # True
    print(contains_date(text4))  # False

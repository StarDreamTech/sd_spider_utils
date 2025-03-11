from datetime import datetime

def timestamp_to_datetime(timestamp: int) -> str:
    """
    将时间戳转换为年月日时分秒格式。
    
    :param timestamp: 时间戳（秒级）
    :return: 格式化的日期时间字符串
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def datetime_to_timestamp(date_str: str) -> int:
    """
    解析时间字符串为时间戳。
    
    :param date_str: 时间字符串，格式如 '2025-03-06 12:34:56'
    :return: 对应的时间戳（秒级）
    """
    return int(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').timestamp())

if __name__=="__main__":
    # 时间转换示例
    timestamp = 1709810400
    date_str = timestamp_to_datetime(timestamp)
    print(date_str)  # 输出: "2024-03-07 00:00:00"

    parsed_timestamp = datetime_to_timestamp("2024-03-07 00:00:00")
    print(parsed_timestamp)  # 输出: 1709810400

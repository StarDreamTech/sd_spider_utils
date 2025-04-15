sd_spider_utils
================

一个高效的 Python 爬虫工具库，提供解析、文本标准化等常用功能，助力快速开发爬虫项目。

安装
----

使用 pip 安装：

::

    pip install sd_spider_utils

使用示例
--------

::

    from sd_spider_utils.text_utils import normalize_text

    text = "Ｃａｆé['S.\u2009M. Koksbang\xa0', 'S.\u2009M. Koksbang']"  # 包含全角字符和组合字符
    clean_text = normalize_text(text)
    print(clean_text)

功能特性
--------

- **HTML 解析**：快速提取网页中的文本内容。
- **文本标准化**：清洗和规范化抓取到的文本数据。
- **常用工具函数**：如 User-Agent 随机生成、请求重试机制等。

项目链接
--------

- PyPI: https://pypi.org/project/sd_spider_utils/
- 源码仓库: https://github.com/StarDreamTech/sd_spider_utils
- 视频教程:  https://space.bilibili.com/1909782963
- 作者: 星梦 (cpython666@gmail.com)

许可证
------

MIT License，详见 LICENSE 文件。

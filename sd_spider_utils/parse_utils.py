from typing import List


def get_text_bs4(html: str, remove_blank_lines: bool = False) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    if remove_blank_lines:
        return "\n".join(
            line.strip() for line in soup.text.splitlines() if line.strip()
        )
    else:
        return soup.text.strip()


def get_text_xpath(text: str) -> List[str]:
    from lxml import etree

    tree = etree.fromstring(text)
    return tree.xpath("//text()")


def get_text_scrapy(text: str) -> str:
    from scrapy import Selector

    response = Selector(text=text)
    return "".join(response.xpath("//text()").getall())


if __name__ == "__main__":
    text: str = (
        "<div><p>这是段落1</p><p>这是段落2<em>2nsjkxabs</em><p>这是段落3</p></p></div>"
    )
    print(get_text_scrapy(text))
    print(get_text_bs4(text))
    # ['这是段落1', '这是段落2', '2nsjkxabs', '这是段落3']

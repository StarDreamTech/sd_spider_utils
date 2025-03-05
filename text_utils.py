def normalize_unicode_text(text):
    '''
    转换为标准形式
    '''
    import unicodedata
    normalized_text = unicodedata.normalize("NFKC", text)
    print('normal', normalized_text)

if __name__ =="__main__":
    text = "Ｃａｆé['S.\u2009M. Koksbang\xa0', 'S.\u2009M. Koksbang']"  # 包含全角字符和组合字符
    normalize_unicode_text(text)
def strtobool(value):
    """
    常见字符串转布尔值
    """
    _MAP = {
        "y": True,
        "yes": True,
        "t": True,
        "true": True,
        "on": True,
        "1": True,
        "n": False,
        "no": False,
        "f": False,
        "false": False,
        "off": False,
        "0": False,
    }
    try:
        return _MAP[str(value).lower()]
    except KeyError:
        raise ValueError('"{}" is not a valid bool value'.format(value))

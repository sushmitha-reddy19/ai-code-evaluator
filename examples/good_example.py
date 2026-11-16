def parse_name(value):
    try:
        value = value.strip()
        if not value:
            raise ValueError('empty input')
        return value.title()
    except AttributeError as exc:
        raise ValueError('text required') from exc


def test_parse_name():
    assert parse_name(' ada ') == 'Ada'

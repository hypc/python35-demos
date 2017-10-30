from unittest.mock import Mock


if __name__ == '__main__':
    m = Mock()
    m.a.return_value = '1'
    m.b.return_value = '2'
    print(m.a())
    print(m.b())

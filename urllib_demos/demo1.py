import unittest
from urllib import parse


class UrllibTest(unittest.TestCase):
    def test_quote(self):
        s = '@=+/\\'
        self.assertEqual('%40%3D%2B/%5C', parse.quote(s))

    def test_unquote(self):
        s = '%3D'
        self.assertEqual('=', parse.unquote(s))

    def test_quote_plus(self):
        s = ' +'
        self.assertEqual('+%2B', parse.quote_plus(s))

    def test_unquote_plus(self):
        s = '+'
        self.assertEqual(' ', parse.unquote_plus(s))

    def test_urlencode(self):
        d = {'a': 1, 'b': 2}
        s = parse.urlencode(d)
        self.assertTrue(s == 'a=1&b=2' or s == 'b=2&a=1')

    def test_(self):
        s = 'a=1&b=2&a=3'
        d = parse.parse_qs(s)  # {'a': ['1', '3'], 'b': ['2']}
        self.assertEqual(d['b'][0], '2')
        self.assertEqual(d['a'][0], '1')
        self.assertEqual(d['a'][1], '3')

    def test_urlparse(self):
        u = 'https://www.baidu.com/search?wd=123'
        a = parse.urlparse(u)
        print(a)


if __name__ == '__main__':
    unittest.main()

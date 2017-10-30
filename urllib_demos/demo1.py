import urllib
import unittest


class UrllibTest(unittest.TestCase):

    def test_quote(self):
        s = '@=+/\\'
        self.assertEqual('%40%3D%2B/%5C', urllib.parse.quote(s))

    def test_unquote(self):
        s = '%3D'
        self.assertEqual('=', urllib.parse.unquote(s))

    def test_quote_plus(self):
        s = ' +'
        self.assertEqual('+%2B', urllib.parse.quote_plus(s))

    def test_unquote_plus(self):
        s = '+'
        self.assertEqual(' ', urllib.parse.unquote_plus(s))

    def test_urlencode(self):
        d = {'a': 1, 'b': 2}
        s = urllib.parse.urlencode(d)
        self.assertTrue(s == 'a=1&b=2' or s == 'b=2&a=1')

    def test_(self):
        s = 'a=1&b=2&a=3'
        d = urllib.parse.parse_qs(s)    # {'a': ['1', '3'], 'b': ['2']}
        self.assertEqual(d['b'][0], '2')
        self.assertEqual(d['a'][0], '1')
        self.assertEqual(d['a'][1], '3')


if __name__ == '__main__':
    unittest.main()

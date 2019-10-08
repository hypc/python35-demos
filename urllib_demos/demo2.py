"""
url解析与拼接
"""
from unittest import TestCase
from urllib import parse


class URLTestCase(TestCase):
    def setUp(self):
        super(URLTestCase, self).setUp()

    def test_parse(self):
        url = 'https://www.google.com/search?q=1&oq=1&sourceid=chrome&ie=UTF-8#123'

        # 解析url
        parsed = parse.urlparse(url)
        print(parsed)
        self.assertEqual(parsed.scheme, 'https')
        self.assertEqual(parsed.netloc, 'www.google.com')
        self.assertEqual(parsed.path, '/search')
        self.assertEqual(parsed.params, '')
        self.assertEqual(parsed.query, 'q=1&oq=1&sourceid=chrome&ie=UTF-8')
        self.assertEqual(parsed.fragment, '123')

        # 解析query
        params = parse.parse_qs(parsed.query)
        print(params)

    def test_unparse(self):
        scheme = 'https'
        netloc = 'www.google.com'
        path = 'search'
        params = {'q': '1', 'ie': 'UTF-8', 'oq': '1', 'sourceid': 'chrome'}
        fragment = '123'

        # 拼接query
        query = parse.urlencode(params)
        print(query)

        # 拼接url
        url = parse.urlunparse((scheme, netloc, path, '', query, fragment))
        print(url)

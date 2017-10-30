import re
import unittest


class ReTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_match(self):
        a = '2016-06-01, I am very happy'
        m = re.match(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', a)
        print(m.groups())
        print(m.groupdict())

    def test_sub(self):
        '''
        测试正则替换
        '''
        s = '123sdf--123sdf'
        strs = re.sub('[a-z]', '', s)
        self.assertEqual('123--123', strs, '')
        print(strs)

    def test_111(self):
        a = '<http://127.0.0.1:80/asd?page=1&page_size=10>; rel="next"'
        m = re.match('<(?P<url>http://[^>]+)>; ?rel=.+', a)
        print(m.groupdict()['url'])

if __name__ == '__main__':
    unittest.main()

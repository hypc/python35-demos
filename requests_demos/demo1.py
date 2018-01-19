from unittest import TestCase
from unittest import mock

import requests

responses = {
    'https://www.baidu.com': '1',   # 将此处'1'换成对应的Response对象
    'https://www.bing.com': '2',
    '404': '3',
}


def mocked_requests_get(*args, **kwargs):
    return responses.get(args[0])


class RequestTestCase(TestCase):
    def setUp(self):
        super(RequestTestCase, self).setUp()

    def test_1(self):
        resp = requests.get("https://www.baidu.com")
        self.assertEqual(resp.status_code, 200)

    @mock.patch('requests.get', mock.Mock(side_effect=mocked_requests_get))
    def test_2(self):
        resp = requests.get("https://www.baidu.com")
        resp2 = requests.get("https://www.bing.com")

        print(resp)
        print(resp2)

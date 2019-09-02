"""
上下文管理器

拥有启动及退出的过程。
我们可以将一些进入需要初始化、退出需要销毁的代码片段上。

如：文件读写、数据库连接、网络请求等。
"""
from unittest import TestCase


class MyContext(object):
    def __init__(self):
        print('__init__')
        super(MyContext, self).__init__()

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print('__exit__')


class ContextmanagerTestCase(TestCase):
    def setUp(self):
        super(ContextmanagerTestCase, self).setUp()

    def test_1(self):
        with MyContext():
            print('body')

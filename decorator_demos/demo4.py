from functools import wraps
from unittest import TestCase


class deco(object):
    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwds):
            return func(*args, **kwds)

        return inner


class DecoratorTest(TestCase):
    def setUp(self):
        super(DecoratorTest, self).setUp()

    def test_1(self):
        @deco()
        def aaa(*args, **kwargs):
            print(args, kwargs)

        aaa()
        aaa(1, 2, a=1)

    def test_2(self):
        class AAA(object):
            @deco()
            def aaa(self, *args, **kwargs):
                print(args, kwargs)

        AAA().aaa()
        AAA().aaa(1, 2, a=1)

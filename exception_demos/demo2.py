from unittest import TestCase


class MyException(Exception):
    pass


class ExceptionTestCase(TestCase):
    def setUp(self):
        super(ExceptionTestCase, self).setUp()

    def test(self):
        try:
            raise MyException('1234')
        except MyException as e:
            print(e.__str__())

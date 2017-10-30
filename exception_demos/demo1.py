import unittest


class MyException(Exception):
    pass


class My2Exception(MyException):
    pass


class Test(unittest.TestCase):

    def setUp(self):
        super(Test, self).setUp()

    def test_1(self):
        try:
            raise MyException('123')
        except MyException as e:
            print(e)

    def test_2(self):
        try:
            raise My2Exception('456')
        except My2Exception as e:
            print(e)

    def test_3(self):
        try:
            raise My2Exception
        except My2Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()

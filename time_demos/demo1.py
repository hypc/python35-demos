from datetime import datetime, timedelta
import time
import unittest
from unittest.case import skip


class TimeTest(unittest.TestCase):

    @skip('')
    def test_format(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))

    @skip('')
    def test_from_string(self):
        pass

    @skip('')
    def test_to_timestamp(self):
        dt = time.strptime('2016-01-01 12:13:14', '%Y-%m-%d %H:%M:%S')
        print(time.mktime(dt))

        dt2 = datetime.now()
        print(time.mktime(dt2.timetuple()))


class DatetimeTest(unittest.TestCase):

    @skip('')
    def test_format(self):
        dt = datetime.now()
        print(dt.strftime('%Y-%m-%d %H:%M:%S'))

    @skip('')
    def test_from_string(self):
        dt = datetime.strptime('2016-01-01 12:13:14', '%Y-%m-%d %H:%M:%S')
        print(dt.strftime('%Y-%m-%d %H:%M:%S'))

    @skip('')
    def test_calc(self):
        dt = datetime.now()
        print(dt)
        print(dt + timedelta(1, 10, 100))
        print(dt + timedelta(days=1))
        print(dt + timedelta(seconds=10))
        print(dt + timedelta(microseconds=100))


if __name__ == '__main__':
    unittest.main()

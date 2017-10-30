import calendar
from datetime import datetime
import unittest


def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + int(month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


class Test(unittest.TestCase):

    def test_1(self):
        dt = datetime.strptime('2016-01-31 12:13:14', '%Y-%m-%d %H:%M:%S')
        print(add_months(dt, 1))

    def test_2(self):
        dt = datetime.strptime('2016-12-31 12:13:14', '%Y-%m-%d %H:%M:%S')
        print(add_months(dt, 5))


if __name__ == '__main__':
    unittest.main()

from datetime import datetime, tzinfo, timedelta
import unittest
from unittest.case import skip

import pytz


ZERO_TIME_DELTA = timedelta(0)
LOCAL_TIME_DELTA = timedelta(hours=8)  # 本地时区偏差


class UTC(tzinfo):

    def utcoffset(self, dt):
        return ZERO_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA


class LocalTimezone(tzinfo):

    def utcoffset(self, dt):
        return LOCAL_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA

    def tzname(self, dt):
        return '+08:00'


utc_tz = UTC()
local_tz = LocalTimezone()


class Test(unittest.TestCase):

    @skip('')
    def test_1(self):
        tz = pytz.timezone(pytz.country_timezones('cn')[0])
        print(tz)

    @skip('')
    def test_2(self):
        dt = datetime.now(tz=utc_tz)
        print(dt)
        dt2 = datetime.now(tz=local_tz)
        print(dt2)
        dt3 = dt.replace(tzinfo=local_tz)
        print(dt3)

    @skip('')
    def test_3(self):
        dt = datetime.now(tz=utc_tz)
        print(dt)
        print(dt.timestamp())
        dt = dt.now(tz=local_tz)
        print(dt)
        print(dt.timestamp())

    def test_4(self):
        dt = datetime.now(tz=local_tz)
        print(dt)
        timestamp = dt.timestamp()
        print(timestamp)
        print(datetime.fromtimestamp(timestamp))
        print(datetime.fromtimestamp(timestamp, tz=utc_tz))
        print(datetime.fromtimestamp(timestamp, tz=local_tz))


if __name__ == '__main__':
    unittest.main()

import calendar
from datetime import datetime


Yearmonth = (
    (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
    (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
)


def addmonths(begindate, months):
    n = begindate.year * 12 + begindate.month - 1
    n = n + months
    ryear = int(n / 12)
    rmonth = n % 12 + 1
    rday = begindate.day
    if calendar.isleap(ryear):
        if rday > Yearmonth[1][rmonth]:
            rday = Yearmonth[1][rmonth]
    else:
        if rday > Yearmonth[0][rmonth]:
            rday = Yearmonth[0][rmonth]

    return begindate.replace(year=ryear, month=rmonth, day=rday)

if __name__ == '__main__':
    print(addmonths(datetime(2016, 1, 30), 1))
    print(addmonths(datetime(2016, 3, 31), 1))
    print(addmonths(datetime(2011, 1, 31), 1))

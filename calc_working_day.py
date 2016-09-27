import time
from datetime import date


def test():
    assert calc_working_day(3, 2016, 9, 1) == 5
    assert calc_working_day(11, 2016, 9, 2) == 17


def what_week_day(year, month, day):
    return date(year, month, day).weekday()


def calc_working_day(x, year, month, day):
    day = 5 - what_week_day(year, month, day) - 1
    var = x / 5
    mod = x % 5

    if mod > day:
        var += 1

    return var*2+x

test()
print calc_working_day(5, 2016, 9, 5)

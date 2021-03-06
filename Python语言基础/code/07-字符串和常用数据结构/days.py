"""
指定的年月日是这一年的第几天
"""


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def days(year, month, day):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    days = 0
    for index in range(month - 1):
        days += days_of_month[index]
    return days + day


if __name__ == "__main__":
    print(days(1980, 11, 28))
    print(days(1981, 12, 31))
    print(days(2018, 1, 1))
    print(days(2016, 3, 1))

"""
函数的定义和使用 - 判断一个数是不是回文数
"""

num = 1221


def is_palindrome(num):
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        return True
    else:
        return False


if is_palindrome(num):
    print(num, 'is a palindrome number!')
else:
    print(num, 'is not a palindrome number!')
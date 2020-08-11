"""
判断输入的正整数是不是回文素数
"""

import math

num = 11


def is_prime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


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


if is_prime(num) and is_palindrome(num):
    print(num, 'is a palindrome and prime number!')
else:
    print(num, 'is not a palindrome and prime number!')
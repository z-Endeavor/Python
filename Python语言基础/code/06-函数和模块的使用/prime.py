"""
函数的定义和使用 - 判断一个数是不是素数
"""

import math

num = 7


def is_prime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


if is_prime(num):
    print(num, 'is a prime number!')
else:
    print(num, 'is not a prime number!')

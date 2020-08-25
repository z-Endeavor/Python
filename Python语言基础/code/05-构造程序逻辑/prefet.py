"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""
import math

for n in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(n)) + 1):
        if n % factor == 0:
            result += factor
            if factor != 1 and n // factor != factor:
                result += n // factor
    if result == n:
        print(n, end=' ')

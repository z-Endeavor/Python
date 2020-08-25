"""
输出2~99之间的素数
"""

import math

for n in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(n)) + 1):
        if n % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=' ')

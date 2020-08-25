"""
输入两个正整数计算最大公约数和最小公倍数
"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('The gcd of %d and %d is %d' % (x, y, factor))
        print('The lcm of %d and %d is %d' % (x, y, x * y // factor))
        break

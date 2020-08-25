"""
输入一个正整数判断它是不是素数
1. 直接法
2. 优化
"""
import math

"""
直接法
    对于给定的数num，直接遍历 (2,num) 之间是否存在它的合数。
"""
num1 = int(input("Input Number: "))
is_prime = True
for x in range(2, num1):
    if num1 % x == 0:
        is_prime = False
        break
if is_prime and num1 != 1:
    print('%d is a prime number.' % num1)
else:
    print('%d is not a prime number' % num1)


"""
优化
    若所给定的数num不是素数
    那么存在不等于1的两个约数x1和x2，并且满足x1 >= sqrt(num)，x2 <= sqrt(num)
    因此可直接搜索 num % x1 是否为0来判断素数。
"""
num2 = int(input("Input Number: "))
end = int(math.sqrt(num2))
is_prime = True
for y in range(2, end + 1):
    if num2 % y == 0:
        is_prime = False
        break
if is_prime and num2 != 1:
    print('%d is a prime number.' % num2)
else:
    print('%d is not a prime number.' % num2)

"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c or b + c > a or c + a > b:
    print('Perimeter: ', a + b + c)
    p = (a + b + c) / 2
    print('Area: ', math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print('Not a triangle!')

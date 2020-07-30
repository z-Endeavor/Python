"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

num = random.randint(1, 100)
while True:
    guess = int(input('Input Number: '))
    if guess > num:
        print('Bigger than answer!')
    elif guess < num:
        print('Smaller than answer!')
    else:
        print('Right answer!')
        break


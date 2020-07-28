"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

from random import randint

money = 1000
while money > 0:
    print('Your Money: ', money)
    second_round = False
    wager = int(input('Please wager: '))

    first = randint(1, 6) + randint(1, 6)
    print('You get %d' % first)
    if first == 7 or first == 11:
        print('You win!')
        money += wager
    elif first == 2 or first == 3 or first == 12:
        print('Banker win!')
        money -= wager
    else:
        second_round = True

    while second_round:
        second = randint(1, 6) + randint(1, 6)
        print('You get %d' % second)
        if second == 7:
            print('Banker win!')
            money -= wager
            break
        elif second == first:
            print('You win!')
            money += wager
            break

print('You have no money, Game Over!')

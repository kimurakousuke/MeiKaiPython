# 猜拳游戏

import random

print('猜拳游戏')

# 胜利次数、失败次数、平局次数
win_no = lose_no = draw_no = 0

while True:
    comp = random.randint(0, 2)

    while True:
        human = int(input('石头剪子布(0：石头／1：剪刀／2:布）：'))
        if 0 <= human <= 2:
            break

    print('我出的是', end='')
    if comp == 0:
        print('石头', end='')
    elif comp == 1:
        print('剪刀', end='')
    else:
        print('布', end='')
    print('。')

    # 判断胜负
    judge = (human - comp + 3) % 3

    if judge == 0:
        print('平局。')
        draw_no += 1
    elif judge == 1:
        print('你输了。')
        lose_no += 1
    else:
        print('你赢了。')
        win_no += 1

    retry = int(input('再玩一局(0：是／1：否）：'))
    if retry == 1:
        break

print('成绩：', win_no, '次胜利', lose_no, '次失败', draw_no, '次平局。')

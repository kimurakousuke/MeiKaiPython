# 心算练习（三个三位整数相加） 

import random

def confirm_retry():
    """确认是否进行再次练习""" 
    while True:
        n = int(input('再练习一次？<Yes…1／No…0>：')) 
        if n == 0 or n == 1:
            return n

print('心算练习开始！') 

while True:
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    z = random.randint(100, 999)

    while True:
        print(x, '+', y, '+', z, '= ', end='')
        k = int(input())
        if k == x + y + z:
            break
        print('答案错误！') 

    if not confirm_retry():
        break

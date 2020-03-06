# 生成n个10～99的随机数

import random

n = int(input('生成随机数个数：'))

for _ in range(n):
    r = random.randint(10, 99)
    if (r == 13):
        print('\n根据条件终止循环。')
        break
    print(r, end=' ')
else:
    print('\n随机数生成结束。')

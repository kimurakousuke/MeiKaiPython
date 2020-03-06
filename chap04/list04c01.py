# 每隔1秒对正整数进行递减直至为0

import time

print('递减计数。') 
n = int(input('正整数：')) 

while n >= 0:
    print(n, end=' ')
    n -= 1 # n减1
    time.sleep(1) # 暂停1秒
print()
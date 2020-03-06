# 猜数字游戏

import random 

MAX = 1000 # 猜测数字的最大值
MAX_STAGE = 10 # 可以输入的最大次数
print('正确数字在1～{}的范围内，请在{}次以内猜中正确数字。'.format(MAX, MAX_STAGE)) 

stage = 1 
answer = random.randint(1, MAX) 

while stage <= MAX_STAGE: 
    print('第', stage, '次 正确数字是多少：', end='') 
    n = int(input()) 
    
    if n < 1 or n > MAX: # 如果输入范围以外的数字则重新输入
        continue 
        
    if n == answer: # 正确答案
        print('正确。','第', stage, '次猜中。') 
        break 
    elif n > answer: 
        print('正确数字要小一些。') 
    else: 
        print('正确数字要大一些。') 
    
    stage += 1 
    
else: 
    print('真可惜。正确数字是', answer, '。')
# 仅选出80分以上的分数

import random 

number = int(input('学生的人数：')) 

tensu = [None] * number 

for i in range(number): 
    tensu[i] = random.randint(0, 100) 
    
print('所有学生的分数=', tensu) 
print('合格学生的分数=', list(filter(lambda n: n >= 80, tensu)))
# 第7章 总结

import random

MAX = 10
print('生成0～{}的随机数。'.format(MAX)) 
number = int(input('生成个数：')) 

# 生成元素总数为number且所有元素为None的列表 
v = [None] * number

# 所有元素赋值为0～MAX的随机数
for i in range(number):
    v[i] = random.randint(0, MAX)

# 打印输出列表
print(v)

# 使用'*'打印输出纵向的柱状图
for i in range(MAX, 0, -1):
    for j in range(0, number):
        if v[j] >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('-' * number)
for i in range(number):
    print(i % 10, end='')

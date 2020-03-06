# 使用enumerate函数遍历并输出字符串内的所有字符（从1开始计数）

s = input('字符串：') 

for i, ch in enumerate(s, 1): 
    print('第{}个字符：{}'.format(i, ch))
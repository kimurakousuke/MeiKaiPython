# 使用enumerate函数反向遍历并输出字符串的所有字符

s = input('字符串：') 

for i, ch in enumerate(reversed(s), 1): 
    print('倒数第{}个字符：{}'.format(i, ch)) 
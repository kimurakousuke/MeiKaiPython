# 使用enumerate函数遍历并输出字符串内的所有字符

s = input('字符串：')

for i, ch in enumerate(s):
    print('s[{}] = {}'.format(i, ch))

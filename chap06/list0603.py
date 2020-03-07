# 读取字符串后，使用for语句遍历其中所有字符并输出

s = input('字符串：')

for i in range(len(s)):
    print('s[{}] = {}'.format(i, s[i]))

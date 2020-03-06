# 从读取的字符串中搜索字符

s = input('字符串s：')
c = input('查找字符c：')

print('字符{}'.format(c), end='')

for i in range(len(s)):
    if s[i] == c:
        print('在s[{}]中。'.format(i))
        break
else:
    print('不存在。')

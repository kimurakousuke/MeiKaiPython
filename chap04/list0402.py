# 从一个正整数开始递减计数到0

print('递减计数。')
n = int(input('正整数: '))

while n >= 0:
    print(n,end=' ')
    n -= 1     # n减1
print()
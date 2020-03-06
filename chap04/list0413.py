# 读取整数后列举小于该数的奇数

n = int(input('整数：'))

for i in range(1, n + 1, 2):
    print(i, end=' ')
print()

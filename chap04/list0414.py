# 读取整数后列举该数的全部约数

n = int(input('整数：'))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
print()

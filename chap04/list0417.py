# 打印输出九九乘法表

print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print('{:3d}'.format(i * j), end='')
    print()
print('-' * 27)

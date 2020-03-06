# 打印输出直角在右下角的等腰直角三角形

print('直角在右下角的等腰直角三角形') 
n = int(input('腰长：'))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()

# 直角在左下角的等腰直角三角形

print('直角在左下角的等腰直角三角形') 
n = int(input('腰长：'))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

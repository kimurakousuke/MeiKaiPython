# 直角在左下角的等腰三角形

print('直角在左下角的等腰三角形') 

n = int(input('腰长：')) 

for i in range(1, n + 1):
    for _ in range(i):
        print('*', end='')
    print()

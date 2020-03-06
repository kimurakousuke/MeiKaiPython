# 输出直角在左下角的等腰三角形和长方形（其二：关键字参数） 

# 连续打印输出n个s
def puts(n, s):
    for i in range(n):
        print(s, end='')

print('直角在左下角的等腰三角形') 
n = int(input('腰长：')) 

for i in range(1, n + 1):
    puts(n = i, s = '*')
    print()

print('长方形') 
h = int(input('宽度：')) 
w = int(input('长度：')) 

for i in range(1, h + 1):
    puts(s = '+', n = w)
    print()

# 长方形 

print('长方形') 
h = int(input('宽度：')) 
w = int(input('长度：')) 

for i in range(1, h + 1):
    for _ in range(w):
        print('*', end='')
    print()

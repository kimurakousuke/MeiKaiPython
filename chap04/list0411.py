# 使用for语句对整数进行递增（排序后从a到b） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

a, b = sorted([a, b]) # 升序排列

for counter in range(a, b + 1):
    print(counter, end=' ')
print()

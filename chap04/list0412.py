# 整数的递增计数

start = int(input('开始：')) 
end = int(input('结束：')) 
step = int(input('步进：'))

for count in range(start, end, step):
    print(count, end=' ')
print()

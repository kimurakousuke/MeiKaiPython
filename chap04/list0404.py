# 计算1到n的和（n赋值为读取的正整数）

print('计算1到n的和。')

while True: 
    n = int(input('n的值：')) 
    if n > 0: 
        break 

sum = 0 
i = 1 
while i <= n: 
    sum += i # sum加i
    i += 1 # i加1
print('1到', n, '的和是', sum, '。')
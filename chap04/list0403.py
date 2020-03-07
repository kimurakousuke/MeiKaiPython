# 计算1到n的和

print('计算1到n的和。') 
n = int(input('n的值：')) 

sum = 0
i = 1
while i <= n:
    sum += i # sum加i
    i += 1 # i加1
print('1到', n, '的和为', sum, '。')
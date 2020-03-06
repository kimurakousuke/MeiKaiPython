# 读取分数后输出总分和平均分（其三：使用enumerate遍历后计算总分）

print('计算总分和平均分。') 
number = int(input('学生的人数：')) 

tensu = [None] * number

for i in range(number):
    tensu[i] = int(input('第{}名的分数：'.format(i + 1)))

total = 0
for i, point in enumerate(tensu):
    total += point                       # 不需要i的值

print('总分为{}分。'.format(total)) 
print('平均分为{}分。'.format(total / number)) 

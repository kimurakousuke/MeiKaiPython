# 读取分数后输出总分以及平均分（其二：错误）

print('计算总分和平均分。') 
number = int(input('学生的人数：')) 

tensu = [None] * number

for i, point in enumerate(tensu):
    point = int(input('第{}名的分数：'.format(i + 1))) 

sum = 0
for i in range(number):
    sum += tensu[i]

print('总分为{}分。'.format(total)) 
print('平均分为{}分。'.format(total / number)) 


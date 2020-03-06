# 读取分数后输出总分和平均分（其五：使用sum函数计算总分） 

print('计算总分和平均分。') 
number = int(input('学生的人数：')) 

tensu = [None] * number

for i in range(number):
    tensu[i] = int(input('第{}名的分数：'.format(i + 1)))

total = sum(tensu)

print('总分为{}分。'.format(total)) 
print('平均分为{}分。'.format(total / number)) 

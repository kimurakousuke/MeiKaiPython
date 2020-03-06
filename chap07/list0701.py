# 读取5个人的分数并输出总分以及平均分

print('计算5个人分数的总分以及平均分。') 

tensu1 = int(input('第1名分数：')) 
tensu2 = int(input('第2名分数：')) 
tensu3 = int(input('第3名分数：')) 
tensu4 = int(input('第4名分数：')) 
tensu5 = int(input('第5名分数：')) 

total = 0 
total += tensu1 
total += tensu2 
total += tensu3 
total += tensu4 
total += tensu5 

print('总分是{}分。'.format(total)) 
print('平均分是{}分。'.format(total / 5))
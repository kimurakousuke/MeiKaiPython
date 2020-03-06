# 读取人数和分数后输出总分和平均分

print('计算总分和平均分。') 
print('注意：输入"End"后停止读取分数。') 

number = 0 
tensu = [] # 空列表 

while True: 
    s = input('第{}名的分数：'.format(number + 1)) 
    if s == 'End': 
        break 
    tensu.append(int(s)) # 在末尾追加分数
    number += 1 
    
total = sum(tensu) 

print('总分为{}分。'.format(total)) 
print('平均分为{}分。'.format(total / number)) 
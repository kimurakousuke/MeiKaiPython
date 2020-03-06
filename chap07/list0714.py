# 读取人数和分数后输出最低分和最高分（其二：利用内置函数） 

print('注意：输入"End"后停止读取分数。') 

number = 0
tensu = []                  # 列表

while True:
    s = input('第{}名的分数：'.format(number + 1))
    if s == 'End':
        break
    tensu.append(int(s))    # 在末尾添加
    number += 1

minimum = min(tensu)
maximum = max(tensu)

for i in range(1, number):
    if tensu[i] < minimum: minimum = tensu[i]
    if tensu[i] > maximum: maximum = tensu[i]

print('最低分为{}分。'.format(minimum)) 
print('最高分为{}分。'.format(maximum))

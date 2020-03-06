# 根据读取的月份输出季节（其三：连续使用比较运算符） 

month = int(input('查询季节。\n月份：')) 

if 3 <= month <= 5: 
    print('该月份是春天。') 
elif 6 <= month <= 8: 
    print('该月份是夏天。') 
elif 9 <= month <= 11: 
    print('该月份是秋天。') 
elif month == 12 or month == 1 or month == 2:
    print('该月份是冬天。')
else:
    print('该月份不存在。')
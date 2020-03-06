# 根据读取的月份输出季节（其四：使用集合） 

month = int(input('查询季节。\n月份：')) 

if month in {3, 4, 5}: 
    print('该月份是春天。') 
elif month in {6, 7, 8}: 
    print('该月份是夏天。') 
elif month in {9, 10, 11}: 
    print('该月份是秋天。') 
elif month in {1, 2, 12}: 
    print('该月份是冬天。') 
else: 
    print('该月份不存在。') 

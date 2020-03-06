# 根据读取的月份输出季节（其一） 

month = int(input('查询季节。\n月份：')) 

if 3 <= month and month <= 5: 
    print('该月份是春天。')  
elif 6 <= month and month <= 8: 
    print('该月份是夏天。')  
elif 9 <= month and month <= 11: 
    print('该月份是秋天。')  
elif (month == 1 or # 1月份是冬天  
      month == 2 or # 2月份也是冬天 
      month == 12   # 12月份也是冬天 
     ): 
    print('该月份是冬天。')  
else: 
    print('该月份不存在。')
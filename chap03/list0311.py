# 判断整数的位数（0、1位数或多位数） 

n = int(input('整数：')) 

if n == 0: # 零 
    print('该数字为零。')  
elif n >= -9 and n <= 9: # 1位数 
    print('该数字为1位数。')  
else: # 多位数 
    print('该数字为多位数。') 

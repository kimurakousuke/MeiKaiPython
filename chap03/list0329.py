# 读取的整数是否为正数或正奇数 

n = int(input('整数：')) 

if n > 0: 
    print('该数字为正数。') 
    if n % 2 == 1: 
        print('该数字为奇数。')
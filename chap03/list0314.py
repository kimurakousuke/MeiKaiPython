# a是否能被b整除 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

c = b != 0 and a % b 
print(c, end='…') 

if c: 
    print('a不能被b整除。')  
else: 
    print('b等于0或a能被b整除。')

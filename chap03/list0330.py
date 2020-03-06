# 对两个整数按照升序排列（其一） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

if a > b: 
    t = a 
    a = b
    b = t 
    
print('按照a≦b进行排序。')  
print('变量a的值是', a, '。') 
print('变量b的值是', b, '。')
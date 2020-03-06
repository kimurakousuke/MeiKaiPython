# 对三个整数按照升序排列 

a = int(input('整数a：')) 
b = int(input('整数b：')) 
c = int(input('整数c：')) 

if a > b: a, b = b, a 
if b > c: b, c = c, b 
if a > b: a, b = b, a 

print('按照a≦b≦c进行排序。')  
print('变量a的值是', a, '。') 
print('变量b的值是', b, '。') 
print('变量c的值是', c, '。')
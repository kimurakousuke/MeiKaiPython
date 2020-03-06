# 对两个整数按照降序排列 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

a, b = sorted([a, b], reverse=True)

print('按照a≧b进行排序。') 
print('变量a的值是', a, '。') 
print('变量b的值是', b, '。') 
# 打印输出两个数字中的较小数字（其二：条件运算符） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

min2 = a if a < b else b

print('较小的数字是', min2, '。')
# 打印输出两个数字中的较小数字（其一：if语句） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

if a < b: 
    min2 = a 
else: 
    min2 = b 
print('较小的数字是', min2, '。')

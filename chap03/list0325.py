# 计算并输出较小的数字和较大的数字（其一） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

if a < b: 
    min2 = a 
    max2 = b 
else: 
    min2 = b 
    max2 = a 

print('较小的数字是', min2, '。') 
print('较大的数字是', max2, '。')
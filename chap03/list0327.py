# 计算并输出较小的数字和较大的数字（其四：条件运算符） 

a = int(input('整数a：'))
b = int(input('整数b：'))

min2, max2 = (a, b) if a < b else (b, a)

print('较小的数字是', min2, '。') 
print('较大的数字是', max2, '。')

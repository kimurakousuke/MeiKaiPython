# 整数左移或右移后用二进制数表示

x = int(input('整数：')) 
n = int(input('移动位数：')) 

print('x = {:b}'.format(x)) 
print('x << n = {:b}'.format(x << n)) 
print('x >> n = {:b}'.format(x >> n))
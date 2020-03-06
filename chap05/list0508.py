# 后4比特位的清除、设置和反转 

a = int(input('0～255：')) 

print('该数字 = {:08b}'.format(a)) 
print('清除 = {:08b}'.format(a & 0b11110000)) 
print('设置 = {:08b}'.format(a | 0b00001111)) 
print('反转 = {:08b}'.format(a ^ 0b00001111)) 
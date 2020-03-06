"""调用min_max模块中的多个函数""" 

import min_max 

x = float(input('实数x：')) 
y = float(input('实数y：')) 
z = float(input('实数z：')) 

print('x和y中的最小值是{}，最大值是{}。'.format(*min_max.min_max2(x, y))) 
print('y和z中的最小值是{}，最大值是{}。'.format(*min_max.min_max2(y, z))) 
print('x和z中的最小值是{}，最大值是{}。'.format(*min_max.min_max2(x, z))) 
print('x、y和z中的最小值是{}，最大值是{}。'.format(*min_max.min_max3(x, y, z))) 
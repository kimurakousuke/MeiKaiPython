"""调用min_max2模块中的min_max2函数""" 

import min_max2

x = float(input('实数x：')) 
y = float(input('实数y：')) 

mini, maxi = min_max2.min_max2(x, y) 
print('最小值是', mini, '。') 
print('最大值是', maxi, '。')
# 使用update方法合并字典（没有重复的键） 

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 
cmy = {'cyan': '浅蓝', 'magenta': '紫红', 'yellow': '黄'} 

# 合并字典rgb和字典cmy
rgb.update(cmy) 
print(rgb)
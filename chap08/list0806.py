# 使用update方法合并字典（有重复的键）

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 
cry = {'cyan': '浅蓝', 'red': '红', 'yellow': '黄'} 

# 合并字典rgb和字典cry
rgb.update(cry) 
print(rgb) 
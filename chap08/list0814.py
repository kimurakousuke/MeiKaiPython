# 对从字典获取的视图进行遍历（从items()分别取出键和值） 

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 

# 对使用keys()获取的视图进行遍历
for key in rgb.keys(): 
    print(key) 
    
# 对使用values()获取的视图进行遍历
for value in rgb.values(): 
    print(value) 

# 使用itmes()获取视图后进行遍历
for key, value in rgb.items():
    print(key, value)

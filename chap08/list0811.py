# 取出字典的所有键、所有值以及所有元素

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 

print('键：', list(rgb.keys())) # 键的视图转换为列表
print('值 ：', list(rgb.values())) # 值的视图转换为列表
print('元素：', list(rgb.items())) # (键, 值)的视图转换为列表
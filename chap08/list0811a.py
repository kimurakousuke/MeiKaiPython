# 以元组形式取出字典的所有键、所有值以及所有元素

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'}

print('键：', tuple(rgb.keys()))      # 键的视图转换为元组
print('值　：', tuple(rgb.values()))    # 值的视图转换为元组
print('元素：', tuple(rgb.items()))     # (键, 值)的视图转换为元组

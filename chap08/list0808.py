# 使用enumerate函数遍历字典的所有键

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 

for i, key in enumerate(rgb):
    print('{} {}'.format(i, key))

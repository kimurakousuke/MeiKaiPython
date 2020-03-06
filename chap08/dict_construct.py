# 字典的生成

dict01 = {}                     # {}    空字典
dict02 = {'Japan': 392, 'Korea': 408, 'China': 156, 'Taiwan': 158}

dict03 = dict()                 # {}    空字典

lst = [('Japan', 392), ('Korea', 408), ('China', 156), ('Taiwan', 158)]
dict04 = dict(lst)

key = ['Japan', 'Korea', 'China', 'Taiwan']
value = [392, 408, 156, 158]
dict05 = dict(zip(key, value))

print('dict01 =', dict01)
print('dict02 =', dict02)
print('dict03 =', dict03)
print('dict04 =', dict04)
print('dict05 =', dict05)

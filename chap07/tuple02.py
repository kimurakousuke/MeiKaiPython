# 通过enumerate函数遍历元组的所有元素

x = ('John', 'George', 'Paul', 'Ringo')

for i, name in enumerate(x):
    print('x[{}] = {}'.format(i, name))

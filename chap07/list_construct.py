# 生成列表

list01 = []                   # []
list02 = [1, 2, 3]            # [1, 2, 3]
list03 = ['A', 'B', 'C', ]    # ['A', 'B', 'C']

# 季节名列表
list04 = [
    'spring',
    'summer',
    'autumn',
    'winter',
]

list05 = list() # [] 空列表
list06 = list('ABC') # ['A', 'B', 'C'] 从字符串的每个字符生成
list07 = list([1, 2, 3]) # [1, 2, 3] 从列表生成 
list08 = list((1, 2, 3)) # [1, 2, 3] 从元组生成 
list09 = list({1, 2, 3}) # [1, 2, 3] 从集合生成       在下一章讲解

list10 = list(range(7))           # [0, 1, 2, 3, 4, 5, 6]
list11 = list(range(3, 8))        # [3, 4, 5, 6, 7]
list12 = list(range(3, 13, 2))    # [3, 5, 7, 9, 11]

# 生成一个元素总数为5且元素都为空的列表
list13 = [None] * 5 # [None, None, None, None, None] 

print('list01 =', list01)
print('list02 =', list02)
print('list03 =', list03)
print('list04 =', list04)
print('list05 =', list05)
print('list06 =', list06)
print('list07 =', list07)
print('list08 =', list08)
print('list09 =', list09)
print('list10 =', list10)
print('list11 =', list11)
print('list12 =', list12)
print('list13 =', list13)

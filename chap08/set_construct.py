# 集合的生成

set01 = {1}                     # {1}
set02 = {1, 2, 3}               # {1, 2, 3}
set03 = {1, 2, 3,}              # {1, 2, 3}
set04 = {'A', 'B', 'C'}         # {'A', 'B', 'C'}

set05 = set()                   # set() 空集合 
set06 = set('ABC')              # {'A', 'B', 'C'} 从字符串的各个字符生成集合
set07 = set([1, 2, 3])          # {1, 2, 3} 从列表生成集合 
set08 = set([1, 2, 3, 2])       # {1, 2, 3} 从列表生成集合
set09 = set((1, 2, 3))          # {1, 2, 3} 从元组生成集合

print('set01 =', set01)
print('set02 =', set02)
print('set03 =', set03)
print('set04 =', set04)
print('set05 =', set05)
print('set06 =', set06)
print('set07 =', set07)
print('set08 =', set08)
print('set09 =', set09)

# 元组的生成

tuple01 = ()                    # ()
tuple02 = 1,                    # (1)
tuple03 = (1,)                  # (1)
tuple04 = 1, 2, 3               # (1, 2, 3)
tuple05 = 1, 2, 3,              # (1, 2, 3)
tuple06 = (1, 2, 3)             # (1, 2, 3)
tuple07 = (1, 2, 3, )           # (1, 2, 3)
tuple08 = 'A', 'B', 'C',        # ('A', 'B', 'C')

tuple09 = tuple()          # () 空元组
tuple10 = tuple('ABC')     # ('A', 'B', 'C') 从字符串的每个字符生成元组
tuple11 = tuple([1, 2, 3]) # (1, 2, 3) 从列表生成元组
tuple12 = tuple({1, 2, 3}) # (1, 2, 3) 从集合生成元组

tuple13 = tuple(range(7))           # (0, 1, 2, 3, 4, 5, 6)
tuple14 = tuple(range(3, 8))        # (3, 4, 5, 6, 7)
tuple15 = tuple(range(3, 13, 2))    # (3, 5, 7, 9, 11)
tuple16 = divmod(13, 3)             # (4, 1)  商为4，余数为1

print('tupe01 =', tuple01)
print('tupe02 =', tuple02)
print('tupe03 =', tuple03)
print('tupe04 =', tuple04)
print('tupe05 =', tuple05)
print('tupe06 =', tuple06)
print('tupe07 =', tuple07)
print('tupe08 =', tuple08)
print('tupe09 =', tuple09)
print('tupe10 =', tuple10)
print('tupe11 =', tuple11)
print('tupe12 =', tuple12)
print('tupe13 =', tuple13)
print('tupe14 =', tuple14)
print('tupe15 =', tuple15)
print('tupe16 =', tuple16)

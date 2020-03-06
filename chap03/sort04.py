# 对四个整数值进行升序排列（sroted函数）

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
d = int(input('整数d：'))

a, b, c, d = sorted([a, b, c, d])     # # 对四个值进行升序排列

print('按照a≦b≦c≦d进行排序。')
print('变量a的值是', a, '。') 
print('变量b的值是', b, '。')
print('变量c的值是', c, '。')
print('变量d的值是', d, '。')

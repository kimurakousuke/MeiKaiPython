# 使用**解包映射型实参的示例

def puts(n, s):
    """连续打印输出n个s""" 
    for _ in range(n):
        print(s, end='')

d1 = {'n': 3, 's': '*'}     # 3个'*'
d2 = {'s': '+', 'n' :7}     # 7个'+'

puts(**d1)
print()
puts(**d2)

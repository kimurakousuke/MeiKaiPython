# 计算元组中3个值的最大值

def max3(a, b, c):
    """计算并返回a、b和c中的最大值""" 
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

tpl1 = (1, 3, 5)
m = max3(*tpl1)
print(tpl1, '的最大値是', m, '。')

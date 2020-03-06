# 对列表中的三个数值计算最大值

def max3(a, b, c):
    """计算并返回a、b和c中的最大值""" 
    max = a 
    if b > max: max = b 
    if c > max: max = c 
    return max

lst1 = [1, 3, 5] 
m = max3(*lst1) 
print(lst1, '的最大值是', m, '。') 
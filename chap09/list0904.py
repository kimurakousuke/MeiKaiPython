# 计算三个数值的最大值

def max3(a, b, c): 
    """计算并返回n1、n2和x1的最大值是""" 
    max = a 
    if b > max: max = b 
    if c > max: max = c 
    return max 

n1 = int(input('整数n1：')) 
n2 = int(input('整数n2：'))
n3 = int(input('整数n3：')) 

print('最大值是', max3(n1, n2, n3), '。') 

x1 = float(input('实数x1：')) 
x2 = float(input('实数x2：')) 
x3 = float(input('实数x3：')) 

print('最大值是', max3(x1, x2, x3), '。') 

print('n1、n2和x1的最大值是', max3(n1, n2, x1), '。')
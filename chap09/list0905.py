# 计算两个值的最大值

def max2(a, b): 
    """计算并返回a和b的最大值""" 
    if a > b: 
        return a
    return b 
    
n1 = int(input('整数n1：')) 
n2 = int(input('整数n2：')) 

print('最大值是', max2(n1, n2), '。') 
"""计算两个值中的最小值和最大值"""

def min_max2(a, b): 
    """计算并返回a和b中的最小值和最大值""" 
    return (a, b) if a < b else (b, a) 

n1 = int(input('整数n1：')) 
n2 = int(input('整数n2：')) 

minimum, maximum = min_max2(n1, n2) 
print('最小值是', minimum, '，最大值是', maximum, '。')
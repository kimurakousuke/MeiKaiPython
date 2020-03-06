# 计算非负整数的阶乘

def factorial(n): 
    """递归求解非负整数的阶乘""" 
    if n > 0: 
        return n * factorial(n - 1) 
    else: 
        return 1 

n = int(input('几的阶乘：')) 
print(n, '的阶乘是', factorial(n), '。') 
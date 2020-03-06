# 计算1到n总和的程序 

def sum_1ton(n): 
    """计算整数1到n的总和""" 
    s = 0 
    while n > 0: 
        s += n 
        n -= 1 
    return s 
    
x = int(input('x的值：')) 
total = sum_1ton(x) 
print('1到', x, '的总和是', total, '。') 
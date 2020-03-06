"""打印输出九九乘法表和九九加法表""" 

def kuku(func): 
    """打印输出九九乘法表""" 
    for i in range(1, 10): 
        for j in range(1, 10): 
            print('{:3d}'.format(func(i, j)), end='') 
        print() 
        
def mul2(x, y): 
    return x * y
    
def add2(x, y): 
    return x + y 
    
n = int(input('乘法[0]／加法[1]：')) 

if n == 0: 
    print('九九乘法表') 
    kuku(mul2) 
elif n == 1: 
    print('九九加法表') 
    kuku(add2)
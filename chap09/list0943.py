"""通过一个名字调用两个函数""" 

def mul2(x, y): 
    return x * y 

def add2(x, y): 
    return x + y 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

func = mul2 
print('a与b的积是', func(a, b), '。') 

func = add2 
print('a与b的和是', func(a, b), '。')
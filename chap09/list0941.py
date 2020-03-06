"""确认函数是对象""" 

def min2(a, b): 
    """计算并返回a和b最小值的函数""" 
    return a if a < b else b 
    
a = int(input('整数a：')) 
b = int(input('整数b：')) 

func = min2 
print('最小值是', func(a, b), '。') 

del min2 
print('最小值是', func(a, b), '。') 

del func 
print('最小值是', func(a, b), '。') 
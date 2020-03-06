"""打印输出函数的类型和标识号""" 

def min2(a, b): 
    """计算并返回a和b中较小值的函数""" 
    return a if a < b else b

func = min2

print('type(min2), id(min2) = ', type(min2), id(min2))
print('type(func), id(func) = ', type(func), id(func))

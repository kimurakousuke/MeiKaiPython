"""计算最小值和最大值的模块""" 

def min_max2(a: 'value', b: 'value') -> 'value': 
    """计算并返回a和b中的最小值和最大值""" 
    return min(a, b), max(a, b) 

def min_max3(a: 'value', b: 'value', c: 'value') -> 'value': 
    """计算并返回a、b和c中的最小值和最大值""" 
    return min(a, b, c), max(a, b, c) 

if __name__ == '__main__': 
    x = int(input('整数x：')) 
    y = int(input('整数y：')) 
    z = int(input('整数z：')) 
    
    print('x和y中的最小值是{}，最大值是{}。'.format(*min_max2(x, y))) 
    print('y和z中的最小值是{}，最大值是{}。'.format(*min_max2(y, z)))  
    print('x和z中的最小值是{}，最大值是{}。'.format(*min_max2(x, z))) 
    print('x、y和z中的最小值是{}，最大值是{}。'.format(*min_max3(x, y, z)))
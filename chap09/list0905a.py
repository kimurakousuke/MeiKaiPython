# 计算两个值的最大值（另解：使用条件运算符）

def max2(a, b):
    """计算并返回a和b的最大值""" 
    return a if a > b else b 	# 利用条件运算符if else

n1 = int(input('整数n1：'))
n2 = int(input('整数n2：'))

print('最大値是', max2(n1, n2), '。')

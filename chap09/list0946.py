"""lambda表达式计算两个值的和（其二）"""


a = int(input('整数a：'))
b = int(input('整数b：'))
print('a和b的和是', (lambda x, y: x + y)(a, b), '。') 

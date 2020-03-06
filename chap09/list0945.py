"""lambda表达式计算两个值的和""" 

a = int(input('整数a：'))
b = int(input('整数b：'))

add2 = lambda x, y: x + y
print('a和b的和是', add2(a, b), '。')

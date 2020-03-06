# 进行乘法和除法的程序（try-finally语句）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b 等于', a * b, '。')
    print('a / b 等于', a / b, '。')

finally:
    print('您辛苦了。')

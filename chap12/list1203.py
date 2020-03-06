# 进行乘法和除法运算的程序（异常处理：其二）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b 等于', a * b, '。')
    print('a / b 等于', a / b, '。')

except (ValueError, ZeroDivisionError):
    print('无法识别或除零运算！')

else:
    print('正常结束！')

finally:
    print('您辛苦了。')
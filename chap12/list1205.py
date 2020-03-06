# 进行乘法和除法运算的程序（异常处理：其四）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b 等于', a * b, '。')
    print('a / b 等于', a / b, '。')

except ValueError:
    print('无法识别为整数！')
    
except ZeroDivisionError:
    print('除零运算！')

except:
    print('产生异常！')


else:
    print('正常结束！')

finally:
    print('您辛苦了。')

# 打印输出读取的整数符号（条件运算符） 

n = int(input('整数：')) 

print('该数字为' + ('正数' if n > 0 else '0' if n == 0 else '负数') + '。')
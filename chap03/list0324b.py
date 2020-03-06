# 如果读取的整数为正数，则判断并打印输出“偶数”或“奇数” 

n = int(input('正整数：')) 

if n > 0: 
    print('该数字为正{}。'.format('奇数' if n % 2 else '偶数')) 
else: 
    print('输入的数字不为正数。')
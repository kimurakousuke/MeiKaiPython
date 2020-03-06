# 使用格式化运算符%进行格式化

a = int(input('整数a：'))
b = int(input('整数b：'))
n = int(input('整数n：'))
f1 = float(input('实数f1：'))
f2 = float(input('实数f2：'))
s1 = input('字符串s1：')
s2 = input('字符串s2：')

print('n的10进制表示＝%d。' % n) 
print('n的16进制表示＝%o。' % n) 
print('%d用8进制表示为%o，用16进制表示为%x。' % (n, n, n)) 

print('n为%5d，f1为%9.5f，f2为%9.5f。' % (n, f1, f2)) 

print('"%s"+"%s"等于"%s"。' % (s1, s2, s1 + s2)) 

print('%d与%d的和为%d。' % (a, b, a + b)) 

print('%(no1)d+%(no2)d和%(no2)d+%(no1)d都等于%(sum)d。' % 
                {'no1': a, 'no2': b, 'sum': a + b}) 
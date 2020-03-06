# 打印输出比特位的逻辑与、逻辑或、逻辑异或以及取反值

a = int(input('正整数a：')) 
b = int(input('正整数b：')) 

w = int(input('表示位数：')) 
f = '{{:0{}b}}'.format(w) 
m = 2 ** w - 1 # 全部w位相当于2进制数的1

print('a = ' + f.format(a)) 
print('b = ' + f.format(b)) 
print('a & b = ' + f.format(a & b)) 
print('a | b = ' + f.format(a | b)) 
print('a ^ b = ' + f.format(a ^ b)) 
print('~a = ' + f.format(~a & m)) 
print('~b = ' + f.format(~b & m))
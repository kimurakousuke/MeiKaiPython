#第3章 总结 

a = int(input('整数a：')) 
b = int(input('整数b：')) 
c = int(input('整数c：')) 
d = int(input('整数d：')) 


if a: print('a不等于0。')# 如果不为0则为真 
if not b: print('b等于0。')# 如果不为0则为真取非后的值 

# 若a、b和c均为0，则x赋值为d 
x = a or b or c or d 
print('x =', x) 

if d % c: # d除以c的余数不为0 
    print('c不是d的约数。') 
else: 
    print('c是d的约数。') 

print('c是' + ('奇数' if c % 2 else '偶数') + '。') 

print('分数d是否及格：', end='') 
if d < 0 or d > 100: # 0～100以外 
    print('不正确的值。') 
elif d >= 60: # 60～100 
    print('及格') 
else: # 0～59 
    print('不及格') 
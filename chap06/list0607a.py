# 字符串txt是否包含字符串ptn（使用not in运算符）

txt = input('字符串txt：') 
ptn = input('字符串ptn：') 

if ptn not in txt:
    print('txt不包含ptn。')
else:
    print('ptn包含于txt。')

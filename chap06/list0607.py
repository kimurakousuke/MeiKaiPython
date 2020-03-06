# 字符串txt是否包含字符串ptn

txt = input('字符串txt：') 
ptn = input('字符串ptn：') 

if ptn in txt: 
    print('ptn包含于txt。') 
else: 
    print('txt不包含ptn。')
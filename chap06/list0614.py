# 搜索字符串中包含的字符串 

txt = input('字符串txt：') 
ptn = input('字符串ptn：') 

c = txt.count(ptn) 

if c == 0: 
    print('txt不包含ptn。') 
elif c == 1: # 只包含一个 
    print('txt包含的ptn索引为：', txt.find(ptn)) 
else: # 包含多个
    print('txt包含的第一个ptn索引为：', txt.find(ptn)) 
    print('txt包含的最后一个ptn索引为：', txt.rfind(ptn))
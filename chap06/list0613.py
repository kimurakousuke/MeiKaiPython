# 搜索字符串中包含的字符串

txt = input('字符串txt：') 
ptn = input('字符串ptn：') 

try: 
    print('ptn被包含在txt[{}]。'.format(txt.index(ptn))) 
except ValueError: 
    print('ptn不在txt内。') 

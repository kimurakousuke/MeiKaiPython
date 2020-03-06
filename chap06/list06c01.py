# 读取的字符是字母表的第几个字母

from string import * 

c = input('字母表：') 

idx = ascii_lowercase.find(c) 
if idx != -1: 
    print('小写字母的第{}个。'.format(idx + 1)) 
else: 
    idx = ascii_uppercase.find(c) 
    if idx != -1: 
        print('大写字母的第{}个。'.format(idx + 1)) 
    else: 
        print('错误字符。') 
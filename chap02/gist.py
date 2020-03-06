#第2章 总结    chap02/gist.py
print('ABC', 'XYZ')  
print('ABC', 'XYZ', end='') # 最后不换行  
print('ABC', 'XYZ', sep='') # 不插入分隔符 
print() # 换行
print('ABC\n\nXYZ', sep='') # 中间换行2次  
print() # 换行 

s = input('字符串：')  
print('你输入了' , s , '这些内容。')  
print('你输入了' + s + '这些内容。')  
print('你输入了{}这些内容。'.format(s)) 
print()  

no = int(input('正整数：'))  
print('最低位：', str(no % 10), sep='')  
print('2进制：' + bin(no)) # 转换为2进制字符串 
print('8进制：' + oct(no)) # 转换为8进制字符串 
print('10进制：' + str(no)) # 转换为10进制字符串 
print('16进制：' + hex(no)) # 转换为16进制字符串 
print() 

PI = 3.14159 # 表示圆周率的常量  
print('计算长方形和圆的面积。')  
width = float(input('长方形的宽：'))  
length = float(input('长方形的长：')) 
radius = float(input('圆的直径：'))  

print('长方形：{}'.format(width * length))  
print('圆  ：{}'.format(PI * radius * radius))

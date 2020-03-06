"""输出模块put的应用实例""" 

import put 

print('直角在左下角的等腰三角形') 
n = int(input('腰长：')) 

# 使用'*'打印输出腰长为n且直角在左下角的等腰三角形
for i in range(1, n + 1): 
    put.put_star(i) 
    print() 

print('长方形') 
h = int(input('宽度：')) 
w = int(input('高度：')) 

# 使用'+'打印输出宽为h、长为w的长方形
for _ in range(1, h + 1): 
    put.puts(n=w, s='+') 
    print() 
    
# 打印输出模块put的文档字符串
print('\n' + put.__doc__) 
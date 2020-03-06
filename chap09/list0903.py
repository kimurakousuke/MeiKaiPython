# 打印输出直角在左下角的等腰三角形和长方形

def put_star(n): 
    """连续输出n个*""" 
    for _ in range(n):     
        print('*', end='') 
        
print('直角在左下角的等腰三角形')      
n = int(input('腰长：')) 

for i in range(1, n + 1): 
    put_star(i)
    print() 
    
print('长方形') 
h = int(input('宽度：')) 
w = int(input('长度：')) 

for i in range(1, h + 1): 
    put_star(w)
    print() 
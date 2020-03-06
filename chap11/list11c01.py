# 确认名称修饰

class C(): 
    __abc = 5 
    
# 可通过修改后的名字进行访问
print(C._C__abc) 

# 不可通过修改后的名字进行访问
print(C.__abc)
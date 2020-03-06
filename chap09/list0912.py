# 更新列表任意元素的值

def change(lst, idx, val): 
    """lst[idx]的值更新为val""" 
    lst[idx] = val 
    
x = [11, 22, 33, 44, 55] 
print('x =', x) 

index = int(input('索引：')) 
value = int(input('新的值  ：')) 

change(x, index, value) 
print('x =', x) 
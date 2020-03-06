"""插入标注和文档字符串后的函数puts""" 


def puts(n: int, s: str) -> None: 
    """连续打印输出n个s
    
    虚参:
        n -- 打印输出的字符串个数
        s -- 打印输出的字符串 
    返回值: 
        无
    
    """ 
    for _ in range(n): 
        print(s, end='') 
        
        
print(puts.__doc__) # 打印输出文档字符串
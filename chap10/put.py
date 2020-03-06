"""输出模块put 
    函数：
        puts -- 连续输出n个s
        put_star -- 连续输出n个'*'
""" 
def puts(*, n: int, s: str) -> None: 
    """连续输出n个s
    虚参: 
        关键字参数n -- 输出字符串的个数
        关键字参数s -- 输出的字符串
    返回值: 
        无 
    """ 
    for _ in range(n): 
        print(s, end='') 
    
def put_star(n: int) -> None: 
    """连续输出n个'*'
    虚参: 
        参数n -- 输出的个数
    返回值: 
        无 
    """ 
    puts(n=n, s='*')
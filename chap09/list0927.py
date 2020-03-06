# 打印输出自定义函数puts和内置函数max的文档

def puts(n, s): 
    """连续打印输出n个s"""
    for _ in range(n):
        print(s, end='')

help(puts)
help(max)

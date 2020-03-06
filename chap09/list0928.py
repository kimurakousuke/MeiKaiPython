# 添加了标注的函数puts 

def puts(n: int, s: str) -> None:
    """连续打印输出n个s""" 
    for _ in range(n):
        print(s, end='')

puts(5, '*')
print()
print(puts.__annotations__)
print()
puts('*', 5)

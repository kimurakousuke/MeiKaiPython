# 列表的所有元素均变为两倍（函数） 

def double(n):
    return 2 * n

x = [1, 2, 3, 4]
y = map(double, x)

print(list(y))

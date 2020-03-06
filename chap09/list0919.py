# 打印输出求各参数之和的数学表达式并进行计算

def print_sum(a, *no): 
    """返回各参数之和（同时输出表达式）""" 
    sum = a
    print(a, end='')
    n = len(no)
    if n > 0:
        print(' + ', end='')
        for i in range(n - 1):
            sum += no[i]
            print(no[i], '+ ', end='')
        sum += no[n - 1]
        print(no[n - 1], end='')
    print(' =', sum)
    return sum

print_sum(5)

print_sum(9, 3)

print_sum(3, 6, 8, 2, 7)

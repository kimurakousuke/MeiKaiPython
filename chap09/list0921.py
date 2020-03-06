# 打印输出求各参数之和的数学表达式并进行计算（实参的解包） 

def print_sum(a, *no):
    """返回参数之和（同时打印输出表达式）"""
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

lst1 = [1, 3, 5, 7]
print_sum(*lst1)

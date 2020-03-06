"""打印输出乘法表""" 

upper = int(input('从1到几：')) 

def multiplication_table(n: int) -> bool: 
    """打印输出1～n的乘法表"""
    if    1 <= n <=  3: w = 2
    elif  4 <= n <=  9: w = 3
    elif 10 <= n <= 31: w = 4
    else              : return False

    f = '{{:{}d}}'.format(w)
    print('-' * n * w)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f.format(i * j), end='')
        print()
    print('-' * n * w)
    return True

multiplication_table(upper)

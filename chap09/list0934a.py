"""打印输出乘法表（其二）""" 

upper = int(input('从1到几：')) 

def multiplication_table() -> bool:
    """打印输出1～n的乘法表"""
    if    1 <= upper <=  3: w = 2
    elif  4 <= upper <=  9: w = 3
    elif 10 <= upper <= 31: w = 4
    else                  : return False

    f = '{{:{}d}}'.format(w)
    print('-' * upper * w)
    for i in range(1, upper + 1):
        for j in range(1, upper + 1):
            print(f.format(i * j), end='')
        print()
    print('-' * upper * w)
    return True

multiplication_table()

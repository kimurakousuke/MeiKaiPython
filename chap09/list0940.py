# 有nonlocal语句

def outer():
    n = 1
    def inner():
        nonlocal n
        n = 2
        print('n =', n)

    print('n =', n)
    inner()
    print('n =', n)

outer()

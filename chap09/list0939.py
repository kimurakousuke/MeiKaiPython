# 无nonlocal语句

def outer():
    n = 1
    def inner():
        # 编写同名变量
        n = 2
        print('n =', n)

    print('n =', n)
    inner()
    print('n =', n)

outer()

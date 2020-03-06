# 打印输出可变参数的信息

def print_args(*args): 
    """打印输出接受可变参数的args信息""" 
    print('type(args) = ', type(args))
    print('len(args)  = ', len(args))
    print('args       = ', args)

print_args()
print()
print_args(1, 2, 3)

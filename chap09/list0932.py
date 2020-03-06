"""计算平均值""" 

def ave(*args) -> float: 
    """计算可变参数的平均值""" 
    return sum(args) / len(args)

print('ave(1, 2, 3) = {}'.format(ave(1, 2, 3)))
print('ave(5, 7.77, 5) = {}'.format(ave(5, 7.77, 5)))
print('ave(3.5, 4.7, 8.2) = {}'.format(ave(3.5, 4.7, 8.2)))

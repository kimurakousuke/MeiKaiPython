"""转换为列表形式的字符串""" 

def list_str(*args) -> str: 
    """可变参数转换为列表形式的字符串后返回该字符串""" 
    return str(list(args))

print('list_str(1, 2, 3) = {}'.format(list_str(1, 2, 3)))
print('list_str(5, 7.77, 5) = {}'.format(list_str(5, 7.77, 5)))
print('list_str(3.5, 4.7, 8.2) = {}'.format(list_str(3.5, 4.7, 8.2)))

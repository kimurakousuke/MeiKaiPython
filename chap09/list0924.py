# 打印输出字典中存储的人员信息

def put_person(name=None, visa=None, age=None): 
    """打印输出关键字参数接受的人员信息""" 
    if name != None: print('名字 =', name, end=' ') 
    if visa != None: print('国籍 =', visa, end=' ') 
    if age != None: print('年龄 =', age, end=' ') 
    print() # 换行

put_person(name='中田', visa='日本', age=27) 
put_person(name='赵', visa='中国') 
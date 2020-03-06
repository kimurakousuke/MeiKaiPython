# 打印输出字典中存储的人员信息

def put_person(**person): 
    """打印输出字典person中的信息""" 
    if 'name' in person: print('名字 =', person['name'], end=' ') 
    if 'visa' in person: print('国籍 =', person['visa'], end=' ') 
    if 'age' in person: print('年龄 =', person['age'], end=' ') 
    print() # 换行

put_person(name='中田', visa='日本', age=27) 
put_person(name='赵', visa='中国') 
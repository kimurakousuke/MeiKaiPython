# 使用敬称进行问候的函数（带默认值的虚参） 

def hello(name, honorific = '同志'): 
    """使用敬称进行问候""" 
    print('你好，{}{}。'.format(name, honorific)) 
    
hello('田中') 
hello('关根', '君') 
hello('西田', '先生') 
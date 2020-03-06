# 宠物类 

class Pet: 
    """宠物类""" 
    
    def __init__(self, name: str, master: str) -> None: 
        """构造器""" 
        self._name = name # 名字
        self._master = master # 主人的名字
        
    def introduce(self) -> None: 
        """自我介绍""" 
        print('我的名字是{}！'.format(self._name)) 
        print('我的主人是{}！'.format(self._master)) 
        
    def __str__(self) -> str:
        """字符串化""" 
        return self._name + ' <<' + self._master + '>>' 

    def print(self) -> None: 
        """打印输出（打印输出__str__返回的字符串后换行）""" 
        print(self.__str__()) 

# 测试宠物类
kurt = Pet('Kurt', '阿怡') 
kurt.introduce() 
print(kurt) 
print('str(Kurt) = ' + str(kurt)) 
kurt.print()
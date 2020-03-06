# 宠物类和机器宠物类 

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
        """打印输出（打印输出__str__返回的字符串并换行）""" 
        print(self.__str__()) 

class RobotPet(Pet):
    """机器宠物类""" 
    
    def __init__(self, name: str, master: str, type_no: str) -> None: 
        """构造器""" 
        super().__init__(name, master) # 调用基类的构造器
        self._type_no = type_no 
        
    def introduce(self) -> None: 
        """自我介绍""" 
        print('◆我是机器宠物。我的名字是{}。'.format(self._name)) 
        print('◆类型编号是{}。'.format(self._type_no)) 
        print('◆我的主人是{}。'.format(self._master)) 

    def __str__(self) -> str: 
        """字符串化""" 
        return(self._name + ' [[' + self._type_no + ']]' 
        + ' <<' + self._master + '>>') 

    def work(self, sw: int) -> None: 
        """进行家务""" 
        if sw == 0: print('打扫。') 
        elif sw == 1: print('洗涤。') 
        elif sw == 2: print('烹饪。') 
            
# 测试各个宠物类

kurt = Pet('Kurt', '阿怡') 
kurt.introduce() 
print(kurt) 

r2d2 = RobotPet('R2D2', '卢克', 'R2') 
r2d2.introduce() 
print(r2d2) 

def self_introduce(obj: object) -> None: 
    """请求obj进行自我介绍""" 
    obj.introduce() 

self_introduce(kurt) 
self_introduce(r2d2)

# 测试多个宠物类（后续） 

# kurt是Pet类的实例 
kurt.print()

# r2d2是RobotPet类的实例 
r2d2.print()
r2d2.work(1) 
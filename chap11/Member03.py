# 健身房会员类（第3版） 

class Member: 
    """健身房会员类（第3版）""" 

    def __init__(self, no: int, name: str, weight: float) -> None: 
        """构造器""" 
        self.__no = no 
        self.__name = name 
        self.__weight = weight 

    def lose_weight(self, loss: float) -> None: 
        """减重loss千克""" 
        self.__weight -= loss 

    def print(self) -> None: 
        """打印输出数据""" 
        print('{}: {} {}kg'.format(self.__no, self.__name, self.__weight)) 

# 测试会员类 
yamada = Member(15, '山田太郎', 72.7) 
sekine = Member(37, '关根信彦', 65.3) 

yamada.lose_weight(3.5) # 山田君减重3.5kg
sekine.lose_weight(5.3) # 关根君减重5.3kg

yamada.print() 
sekine.print() 
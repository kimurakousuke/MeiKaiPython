# 健身房会员类（第4版）

class Member:
    """健身房会员类（第4版）""" 

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

    @property
    def weight(self) -> float:
        """获取体重（访问器）""" 
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """修改体重（修改器）""" 
        self.__weight = weight if weight > 0.0 else 0.0

# 测试会员类 

yamada = Member(15, '山田太郎', 72.7)

yamada.weight = 67.3                        # 修改山田君的体重 
print('yamada.weight =', yamada.weight)     # 获取山田君的体重 

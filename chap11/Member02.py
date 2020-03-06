# 健身房会员类（第2版） 

class Member: 
    """健身房会员类（第2版）""" 
    
    def __init__(self, no: int, name: str, weight: float) -> None: 
        """构造器""" 
        self.no = no # 会员号码 
        self.name = name # 名字 
        self.weight = weight # 体重 

    def print(self) -> None: 
        """打印输出数据""" 
        print('{}: {} {}kg'.format(self.no, self.name, self.weight)) 

# 测试会员类

yamada = Member(15, '山田太郎', 72.7) 
sekine = Member(37, '关根信彦', 65.3) 

yamada.print() 
sekine.print() 
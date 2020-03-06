# 带标识号的武将类 

class Commander:
    """武将类"""

    __counter = 0   # 所赋予的最后一个标识号

    def __init__(self, name: str) -> None:
        """构造器"""
        self.__name = name
        Commander.__counter += 1
        self.__id = Commander.__counter

    def id(self) -> int:
        """"获取标识号"""
        return self.__id

    @classmethod
    def max_id(cls) -> int:
        """"当前所赋予的最后一个标识号"""
        return cls.__counter

    def print(self) -> None:
        """打印输出数据"""
        print('{}:{}'.format(self.__name, self.__id))

oda = Commander('织田信长')      # 标识号为1 
toyotomi = Commander('丰臣秀吉') # 标识号为2 
tokugawa = Commander('德川家康') # 标识号为3 

print('oda.id() = {}'.format(oda.id()))
print('toyotomi.id() = {}'.format(toyotomi.id()))
print('tokugawa.id() = {}'.format(tokugawa.id()))

print('Commander.max_id() = {}'.format(Commander.max_id()))
print('oda.max_id() = {}'.format(oda.max_id()))

# 健身房会员类（第1版：错误） 

class Member: 
    """健身房会员类（第1版）""" 
    pass

# 测试会员类

yamada = Member()
yamada.no = 15
yamada.name = '山田太郎'
yamada.weight = 72.7

sekine = Member()
sekine.no = 38
sekine.name = '关根信彦' 
sekine.weigth = 65.3    # 拼写错误

print('{}: {} {}kg'.format(yamada.no, yamada.name, yamada.weight))
print('{}: {} {}kg'.format(sekine.no, sekine.name, sekine.weight))

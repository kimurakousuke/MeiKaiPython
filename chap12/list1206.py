# 基于raise语句抛出异常

def func(sw: int) -> None:
    if sw == 0:
        raise ValueError
    elif sw == 1:
        raise ZeroDivisionError

sw = int(input('sw：'))

try:
    func(sw)

except BaseException as e:
    print('捕获异常！')
    print(type(e))

# 抛出自定义异常（不使用raise抛出异常）

class MyException(Exception):
    """自定义异常"""
    pass

def raise_my_exception() -> None:
    raise MyException

def func(sw: int) -> None:
    try:
        if sw == 0:
            raise_my_exception()
    except MyException as e:
        print('捕获自定义异常。')
        # 尝试对自定义异常进行处理。
        # 判断程序无法恢复运行。
        print('程序无法恢复运行。')
        # 不执行raise

sw = int(input('sw：'))

try:
    func(sw)
except Exception as e:
    print('捕获异常！')
    print(type(e))

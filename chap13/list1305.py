# 从文件读取并输出字符串（异常处理）

try:
    f = open('hello.txt', 'r')
    try:
        for line in f:
            print(line, end='')
    except OSError:
        pass             # 读取失败时的处理
    finally:
        f.close()
except OSError:
    pass                 # 打开失败时的处理

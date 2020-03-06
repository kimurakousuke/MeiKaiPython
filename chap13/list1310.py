# 转储文件（以代码或字符形式输出文件内容）

import string

def is_print(ch: str) -> bool:
    """ch字符是否是可打印字符？"""
    return (ch == ' ' or ch in string.digits or ch in string.ascii_letters
                      or ch in string.punctuation)

fname = input('文件名：')

with open(fname, 'rb') as f:
    count = 0    # 位置（从头开始第几个字节）
    while True:
        buf = f.read(16)
        n = len(buf)
        if n == 0:
            break
        print('%08x' % count, end=' ')         # 位置
        for i in range(n):                     # 字符编码
            print('%02x' % buf[i], end=' ')
        if n < 16:
            print('   ' * (16 - n), end='')
        for i in buf:                          # 字符
            ch = chr(i)
            print('%c' % ch if is_print(ch) else '.', end='')
        print()
        if n < 16:
            break
        count += 16

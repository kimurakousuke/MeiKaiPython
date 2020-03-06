# 从文件读取并输出字符串（with语句）

with open('hello.txt', 'r') as f:
    for line in f:
        print(line, end='')

# 打印输出从文件读取的所有行字符串（遍历的对象是文件对象）

f = open('hello.txt')       # 打开（文本＋读取模式）

for line in f:
    print(line, end='')

f.close()                   # 关闭

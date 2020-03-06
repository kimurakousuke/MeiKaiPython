# 打印输出从文件读取的所有行字符串（readlines方法）

f = open('hello.txt')       # 打开（文本＋读取模式）

lines = f.readlines()
for line in lines:
    print(line, end='')

f.close()                   # 关闭

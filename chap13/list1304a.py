# 打印输出从文件读取的所有行字符串（read方法）

f = open('hello.txt')       # 打开（文本＋读取模式）

lines = f.read()
print(lines, end='')

f.close()                   # 关闭

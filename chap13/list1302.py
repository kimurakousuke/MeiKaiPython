# 从文件读取两行字符串并进行输出

f = open('hello.txt') # 打开（文本＋读取模式）

line1 = f.readline() # 读取一行
line2 = f.readline() # 读取一行

print(line1, end='')
print(line2, end='')

f.close() # 关闭
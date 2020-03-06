# 打印输出从文件读取的所有行字符串

f = open('hello.txt') # 打开（文本＋读取模式）

while True:
    line = f.readline()
    if not line: # 没有读取到内容（达到了结尾）
        break
    print(line, end='')
    
    
f.close() # 关闭
# 从二进制文件读取内容

with open('binfile.bin', 'br') as f:
    bin = f.read() # 读取所有内容
    for c in bin:
        print(int(c))

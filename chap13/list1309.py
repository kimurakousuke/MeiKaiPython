# 读取二进制文件中任意位置的字符

with open('binfile.bin', 'br') as f:
    while True:
        pos = int(input('位置：'))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('再读取一次[Y/N]：')
        if retry in {'N', 'n'}:
            break
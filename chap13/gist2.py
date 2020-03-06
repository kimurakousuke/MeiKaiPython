# 第13章 总结（其二）
# 对清单13-7所示程序创建的二进制文件进行任意位置字符的读写

with open('binfile.bin', 'br+') as f:
    while True:
        pos = int(input('位置：'))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('值的修改[Y/N]：')
        if retry in {'Y', 'y'}:
            value = int(input('0～255的值：'))
            if 0 <= value <= 255:
                f.seek(pos)
                f.write(bytes([value]))
            else:
                print('不正确的值。')

        retry = input('再读取一次[Y/N]：')
        if retry in {'N', 'n'}:
            break

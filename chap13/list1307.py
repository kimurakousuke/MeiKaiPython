# 二进制文件写入0x00～0xff

with open('binfile.bin', 'bw') as f: # 二进制写入模式
    f.write(bytes(range(0, 256)))

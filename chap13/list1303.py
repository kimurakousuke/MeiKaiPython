# 向文件追加了两行字符串

f = open('hello.txt', 'a') # 打开（文本＋追加模式）

f.write('Fine, thanks.\n')
f.write('And you?\n')

f.close() # 关闭
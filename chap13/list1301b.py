# 向文件写入两行字符串（writelines方法）

f = open('hello.txt', 'w')      # 打开（文本＋写入模式）

print('Hello!\nHow are you?', file=f)   # 结尾自动输出换行符

f.close()                       # 关闭

# 不断读取整数并对正整数进行加法运算

print('对正整数进行加法运算（输入-9999表示结束）。')

sum = 0
while True:
    n = int(input('整数：'))
    if n == -9999:
        break
    if n <= 0:
        continue
    sum += n
print('正整数总和为', sum, '。')

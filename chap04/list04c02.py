# 对整数1到12进行循环但跳过8（其一）

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()

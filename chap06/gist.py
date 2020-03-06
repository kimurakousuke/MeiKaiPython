# 第６章 总结 

s1 = input('字符串s1：') 
s2 = input('字符串s2：') 

idx = s1.find(s2)
if idx == -1:
    print('s1中不包含s2。') 
else:
    print(s1)
    # 输出idx个空格后输出s2
    print(' ' * idx, end='')
    print(s2)

    # s1中包含的s2全部反转
    s1 = s1.replace(s2, s2[::-1])
    print()
    print('反转对应部分。')
    print(s1)

    # 删除s1中包含的s2[::-1]
    s1 = s1.replace(s2[::-1], '')
    print()
    print('删除对应部分。')
    print(s1)
print()

# format方法的应用实例
x = float(input('实数值：')) 
w = int(input('表示所有位数：')) 
p = int(input('小数部分位数：')) 

print('{{:{}.{}f}}'.format(w, p).format(x))

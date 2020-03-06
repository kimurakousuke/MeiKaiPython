# 函数名作为变量名

a, b, c = 3, 7, 5
max = max(a, b, c) # 第一次执行：OK （max = 7） 
print('a、b和c中的最大值是', max, '。') 

max = max(a, b, c) # 第二次执行：错误（max = 7(a, b, c)） 
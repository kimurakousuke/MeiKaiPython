# 整数的递增（打印输出count的最终值） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

a, b = sorted([a, b]) # 按照升序排列

counter = a

while counter<=b:
    print(counter,end=' ')
    counter = counter + 1 # counter加1
print('\ncounter的值是', counter, '。')
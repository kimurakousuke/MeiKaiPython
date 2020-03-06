# 整数的递增（每隔一个递增） 

a = int(input('整数a：')) 
b = int(input('整数b：')) 

a, b = sorted([a, b]) # 按照升序排列

counter = a

while counter<=b:
    print(counter,end=' ')
    counter = counter + 2 # counter加2
print('\ncounter的值是', counter, '。')
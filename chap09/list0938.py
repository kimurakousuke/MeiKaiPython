# 有global语句

n = 1

def func():
    global n
    n = 2    # n为全局变量 
    print('n =', n)

print('n =', n)
func()
print('n =', n)

# 无global语句

n = 1 

def func(): 
    # 编写同名变量
    n = 2 # n是局部变量 
    print('n =', n)

print('n =', n)
func()
print('n =', n)

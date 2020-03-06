"""确认函数内外变量的値""" 

g1 = 1
g2 = 2

def outer():
    def inner():
        f2 = 6
        print('[2] inner() g1, g2 = ', g1, g2)
        print('    inner() f1, f2 = ', f1, f2)

    f1 = 3
    f2 = 4
    g2 = 5
    inner()
    print('[3] outer() g1, g2 = ', g1, g2)
    print('    outer() f1, f2 = ', f1, f2)

print('[1] global  g1, g2 = ', g1, g2)
outer()
print('[4] global  g1, g2 = ', g1, g2)

# 第５章 总结

a, b = 5, 7
c = b
print('a, b, c = {}, {}, {}'.format(a, b, c))
print('id(5) = {}'.format(id(5)))
print('id(7) = {}'.format(id(7)))
print('id(a) = {}'.format(id(a)))
print('id(b) = {}'.format(id(b)))
print('id(c) = {}'.format(id(c)))
print()

a, b = b, a
c += 1

print('交换a和b的值并对c进行递增')
print('a, b, c = {}, {}, {}'.format(a, b, c))
print('id(5) = {}'.format(id(5)))
print('id(7) = {}'.format(id(7)))
print('id(8) = {}'.format(id(8)))
print('id(a) = {}'.format(id(a)))
print('id(b) = {}'.format(id(b)))
print('id(c) = {}'.format(id(c)))
print('a is 5 = {}'.format(a is 5))
print('a is 7 = {}'.format(a is 7))
print('a is 8 = {}'.format(a is 8))

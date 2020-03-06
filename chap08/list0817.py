# 转换两个字符串为集合后进行集合运算

set1 = set(input('字符串s1：')) 
set2 = set(input('字符串s2：')) 

print('set1：', set1)
print('set2：', set2)
print()
print('set1 == set2：', set1 == set2)
print('set1 != set2：', set1 != set2)
print('set1 <  set2：', set1 <  set2)
print('set1 <= set2：', set1 <= set2)
print('set1 >  set2：', set1 >  set2)
print('set1 >= set2：', set1 >= set2)
print()
print('set1 | set2：', set1 | set2)
print('set1 & set2：', set1 & set2)
print('set1 - set2：', set1 - set2)
print('set1 ^ set2：', set1 ^ set2)
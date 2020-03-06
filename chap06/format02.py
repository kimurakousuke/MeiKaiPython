# 基于format方法指定填充字符和对齐方式

print('{:<12}'.format(77)) # 左对齐 
print('{:>12}'.format(77)) # 右对齐 
print('{:^12}'.format(77)) # 居中 
print('{:=12}'.format(-77)) # 符号 填充字符 数字 
print('{:*<12}'.format(77)) # 在此之后使用'*'作为填充字符 
print('{:*>12}'.format(77))
print('{:*^12}'.format(77))
print('{:*=12}'.format(-77))

# 使用f字符串进行格式化（打印输出生成的字符串）

a = int(input('整数a：')) 
b = int(input('整数b：')) 
c = int(input('整数c：')) 
n = int(input('整数n：')) 
f1 = float(input('实数f1：')) 
f2 = float(input('实数f2：')) 
s = input('字符串s：') 
print() 
print(f'a / b = {a / b}') 
print(f'a % b = {a % b}') 
print(f'a // b = {a // b}') 
print(f'b是a的{a / b:%}') # 百分率 
print() 
print(f' a b c') # 正 负 
print(f'[+]{a:+5}{b:+5}{c:+5}') # '+' '-' 
print(f'[-]{a:-5}{b:-5}{c:-5}') #   '-' 
print(f'[ ]{a: 5}{b: 5}{c: 5}') # ' ' '-' 
print() 
print(f'{c:<12}') # 左对齐 
print(f'{c:>12}') # 右对齐 
print(f'{c:^12}') # 居中 
print(f'{c:=12}') # 在符号后填充字符 
print() 
print(f'n = {n:4}') # 至少4位
print(f'n = {n:6}') # 至少6位
print(f'n = {n:8}') # 至少8位
print(f'n = {n:,}') # 每3位插入,
print() 
print(f'n = ({n:b})2') # 2进制数
print(f'n = ({n:o})8') # 8进制数
print(f'n = ({n})10') # 10进制数
print(f'n = ({n:x})16') # 16进制数（小写字符） 
print(f'n = ({n:X})16') # 16进制数（大写字符） 
print() 
print(f'f1 = {f1:e}') # 指数形式
print(f'f1 = {f1:f}') # 固定小数点形式
print(f'f1 = {f1:g}') #自动判断格式
print() 
print(f'f1 = {f1:.7f}') # 精度位7 
print(f'f1 = {f1:12f}') # 总位数为12？？
print(f'f1 = {f1:12.7f}') # 总位数为12且精度位7 
print() 
print(f'f2 = {f2:.0f}') # 如果没有小数部分则省略
print(f'f2 = {f2:#.0f}') # 小数部分即使不存在也保留小数点 
print() 
print(f'{s:*<12}') # 左对齐 
print(f'{s:*>12}') # 右对齐 
print(f'{s:*^12}') # 居中 
print() 

for i in range(65, 91):   # 65～90个字符
    print(f'{i:c}', end='') 
print()

# 第13章 总结（其一：带行号输出程序文件本身的内容）

with open('gist1.py', 'r', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        print(f'{i:04} {line}', end='')

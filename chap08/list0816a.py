# 字符串中字符的出现次数存储至字典（其三：字典解析式改进版）

txt = input('字符串：')

count = {ch: txt.count(ch) for ch in set(txt)}

print('分布=', count)

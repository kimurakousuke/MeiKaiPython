# 字符串中字符的出现次数存储至字典（其一） 

txt = input('字符串：') 

count = {}
for ch in txt: 
    if ch not in count: 
        count[ch] = 1 # 插入字典
    else: 
        count[ch] += 1 # 更新元素的值

print('分布=', count) 
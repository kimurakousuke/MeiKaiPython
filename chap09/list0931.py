"""基于字典元素中特定值对应的键生成列表""" 

def keys_of(dic: dict, val: 'value') -> list: 
    """返回一个列表，该列表的元素是字典dic中值为val的元素的键""" 
    return [k for k, v in dic.items() if v == val] 

txt = input('字符串：') 
count = {ch: txt.count(ch) for ch in txt} 
print('分布=', count) 

num = int(input('字符数量：')) 
print('{}个字符={}'.format(num, keys_of(count, num))) 
# 从已有列表生成字典

s = ['春', '夏', '秋', '冬']
season = {k: v for k, v in enumerate(s)}    # {0:'春', 1:'夏', 2:'秋', 3:'冬'}

for item in season.items():
    print(item)

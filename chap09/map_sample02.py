# map的应用实例（其二：所有元素的单位从厘米转换为英寸）

x = [1, 2, 3, 4]

print(list(map(lambda n: 2.54 * n , x)))

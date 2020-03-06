# 第9章 总结

def range_of(*v):
    """返回最大值和最小值的差"""
    return abs(max(v) - min(v))

print('range_of(1, 5)           = ', range_of(1, 5))
print('range_of(1, -3, 2, 5, 4) = ', range_of(1, -3, 2, 5, 4))
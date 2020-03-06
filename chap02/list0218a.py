# 计算圆的周长和面积（其三：使用math.pi作为圆周率）

from math import pi

r = float(input('半径：'))

print('圆的周长是', 2 * pi * r, '。')
print('面积是', pi * r * r, '。')
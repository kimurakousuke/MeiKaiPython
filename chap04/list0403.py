# 1からnまでの和を求める

print('1からnまでの和を求めます。')
n = int(input('nの値：'))

sum = 0
i = 1
while i <= n:
    sum += i   # sumにiを加える
    i += 1     # iに1を加える
print('1から', n, 'までの和は', sum, 'です。')

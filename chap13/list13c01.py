# 打印输出上一次运行时的日期和时间

import os.path
import pickle
import datetime

CONFIG_FILE = 'config.dat'

previous = None

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'rb') as f:
        previous = pickle.load(f)
        print('上一次：', previous)
        pass
else:
    print('本程序第一次运行。')

# 各种处理

current = datetime.datetime.now()

with open(CONFIG_FILE, 'wb') as f:
    pickle.dump(current, f)

"""计算某年份的天数""" 

def is_leapyear(year: int) -> bool: 
    """公历year年是否为闰年""" 
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0 

print('计算某年的天数。') 
y = int(input('年份：')) 
print('该年份有{}天。'.format(365 + is_leapyear(y))) 
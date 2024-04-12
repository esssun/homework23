from datetime import datetime

date_st = '2020/11/04 14:53:00'
date_ob = datetime.strptime(date_st, '%Y/%m/%d %H:%M:%S')

print(date_ob.strftime('%Y/%m/%d %H:%M:%S %p'))
print(date_ob.strftime('%a, %Y %B %d'))
print(date_ob.strftime('%A, %Y, %B %d'))
print('Weekday:', date_ob.weekday())
print('Day of the year:', date_ob.timetuple().tm_yday)
print('Week number of the year:', date_ob.isocalendar()[1])

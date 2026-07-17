#date and time module:
from datetime import date,time,datetime,timedelta
'''d=date.today()#to get cuurent date
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.weekday())#days as 0 to 6
print(d.isoweekday())#for international

print(time(21,59,50))'''

d=datetime.now()
'''print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

print(d.strftime('%Y/%m/%d'))
print(d.strftime('%y/%m/%d'))
print(d.strftime('%y/%m/%d %H:%M:%S %p'))
print(d.strftime('%Y/%m/%d %I:%M:%S %p'))
print(d.strftime('%a %y/%m/%d %I:%M:%S %p'))
print(d.strftime('%A %d/%b/%Y %I:%M:%S %p'))
print(d.strftime('%A %d/%B/%Y %I:%M:%S %p'))'''


n=date.today()
a15=n+timedelta(minutes=15)
a7=d+timedelta(days=20)
print(a15)
print(a7)

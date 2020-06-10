#Python Program for DateTime Format

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)


date_object =  datetime.date.today()
print(date_object)

a = 2020
b = 6
c = 8
date = datetime.date(a,b,c)
print(date)

from datetime import date
today = date.today()
print('Current Date = ', today)


timestamp = date.fromtimestamp(135135135)
print('Date = ',timestamp)

today = date.today()
print('Current Year : ', today.year,  '\n' + 'Current Month: ' , today.month , '\n'
      + 'Current Day: ',today.day )

from datetime import time
a = time()
print('a = ', a)

b = time(11,33,56)
print('b = ', b)

d = time(11,34,56,364554)
print('d = ', d)

print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)


from datetime import datetime, date

t1 = date(year = 2019, month = 5, day = 27)
print(t1)

t2 = date(year = 2021, month = 11, day = 16)
t3 = t2 - t1
print(t3)

from datetime import timedelta
t1 = timedelta(weeks = 3, days =  5, hours =  3, seconds = 22)
print(t1)

t2 = timedelta(days = 4, hours = 11, minutes = 5, seconds = 57)
print(t2)

print(t1-t2)

now = datetime.now()
print(now)

t = now.strftime('%H:%M:%S')
print(t)

t1 = now.strftime('%m/%d/%y, %H:%M:%S')
print(t1)

date_string = '27 May 2020'
print(date_string)

date_object = datetime.strptime(date_string, '%d %B %Y')
print(date_object)


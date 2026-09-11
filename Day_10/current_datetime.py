#Example 1: Get Current Date and Time
import datetime
# get the current date and time
now = datetime.datetime.now()
print(now)

#Example 2: Get Current Date

#get current date
current_date = datetime.date.today()
print(current_date)
#Example 3: Date object to represent a date
d=datetime.date(2024, 6, 15)
print(d)
#Example 4: Get the current date using today()
from datetime import date

#todat() to get current date
todays_date = date.today()
print("Current date:", todays_date)

#Example 5: Get the date from a timestamp
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
#Example 6: Print today's year, month and day

today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)    
print("Current day:", today.day)
#Example 7: Time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)

#Example 8: Print hour, minute, second and microsecond
a = time(11, 34, 56, 234566)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
#Python strftime() Method
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

#Handling timezone in Python
from datetime import datetime
from zoneinfo import ZoneInfo

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = ZoneInfo('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = ZoneInfo('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
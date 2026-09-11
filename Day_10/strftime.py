#Python strftime()
#Example 1: datetime to string using strftime()

from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
print("Year:", year)
month = now.strftime("%m")
print("Month:", month)
day = now.strftime("%d")
print("Day:", day)
time = now.strftime("%H:%M:%S")
print("Time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

#Example 2: Creating string from a timestamp
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)	

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

#Example 3: Locale's appropriate date and time
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Output 1:", d)	

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%X")
print("Output 3:", d)
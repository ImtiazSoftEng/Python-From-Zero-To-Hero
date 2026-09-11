#python sleep
import time
time.sleep(2)
print("This message is printed after 2 seconds")
#Example: sleep() Method
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#Create a Digital Clock in Python
while True:
    #get current local time as structured time
    currernt_time = time.localtime()
    #format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", currernt_time)
    print(formatted_time)
    time.sleep(5)
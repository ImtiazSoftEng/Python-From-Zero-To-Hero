#Python Program to Create a Countdown Timer
import time 
def countdown(tiem_sec):
    while tiem_sec:
        mins,secs = divmod(tiem_sec,60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        tiem_sec -= 1
    print("stop")

countdown(5)
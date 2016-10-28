# Author: Bojan G. Kalicanin
# Date: 28-Oct-2016
# Write a function called print_time that takes a Time object and prints
# it in the form hour:minute:second.
# Hint: the format sequence '%.2d' prints an integer using at least
# two digits, including a leading zero if necessary.

class Time(object):
    """Object that represents a time."""
    
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def print_time(time):
    """Print time in the format hour:minute:second."""
    print("{0:02d}:{1:02d}:{2:02d}".format(time.hour, time.minute, time.second))

def is_after(t1, t2):
    """Check if t1 is chronologically after t2."""
    return t1.hour > t2.hour or (t1.hour == t2.hour and (t1.minute > t2.minute
        or (t1.minute == t2.minute and t1.second > t2.second)))

def add_time(t1, t2):
    sum = Time(None, None, None)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

def increment(time, seconds):
    time.second += seconds
    if time.second // 60 >= 1:
        time.second = time.second % 60
        time.minute += time.second // 60
    
    if time.minute // 60 >= 1:
        time.minute = time.minute % 60
        time.hour += time.minute // 60
        
def pure_increment(seconds):
    time = Time(0, 0, 0)
    time.second += seconds
    if time.second // 60 >= 1:
        time.second = time.second % 60
        time.minute += time.second // 60
    
    if time.minute // 60 >= 1:
        time.minute = time.minute % 60
        time.hour += time.minute // 60

def time_to_int(time):
    minutes = time.hour*60 + time.minute
    seconds = minutes*60 + time.second
    return seconds
    
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
 def add_time_v2(t1, t2):
     seconds = time_to_int(t1) + time_to_int(t2)
     return int_to_time(seconds)
     
def increment_v2(time, seconds):
    seconds = time_to_int(time) + seconds
    return int_to_time(seconds)

time = Time(11, 59, 30)
print_time(time)
time2 = Time(10, 59, 30)
print(is_after(time, time2))

start = Time(9, 45, 0)
duration = Time(1, 35, 0)
done = add_time(start, duration)
print_time(done)
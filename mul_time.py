# Author: Bojan G. Kalicanin
# Date: 31-Oct-2016
# Write a function called mul_time that takes a Time object and a number
# and returns a new Time object that contains the product of the
# original Time and the number.
# Then use mul_time to write a function that takes a Time object that
# represents the finishing time in a race, and a number that represents
# the distance, and returns a Time object that represents the average
# pace (time per mile).

import time_obj_v2 as time

def mul_time(t, n):
    """Return a product of the time and the number."""
    p = time.Time()
    p.seconds = t.seconds * n
    return p

def avg_pace(t, d):
    """
    Calculate the average pace (time per mile).
    t: finishing time.
    d: distance.
    """
    return mul_time(t, 1/d)


if __name__ == '__main__':
    t = time.Time(2, 30, 24)
    f = mul_time(t, 3)
    f.print_time()

    # calculate average pace
    finish_time = time.Time(1, 30, 12)
    distance = 12 # 12 miles
    p = avg_pace(finish_time, distance)
    p.seconds = int(p.seconds)
    p.print_time()
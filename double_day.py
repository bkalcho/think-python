# Author: Bojan G. Kalicanin
# Date: 31-Oct-2016
# 1. For two people born on different days, there is a day when one is
#    twice as old as the other. That's their Double Day. Write a program
#    that takes two birthdays and computes their Double Day.
# 2. For a little more challenge, write the more general version that
#    computes the day when one person is n times older than the other.

import datetime

def n_day(b_day1, b_day2, n):
    """Computes double day."""
    if b_day1 > b_day2:
        start_date = b_day1
    else:
        start_date = b_day2

    for i in range(100*365):
        c_date = start_date + datetime.timedelta(days=i)
        d1 = c_date - b_day1
        d2 = c_date - b_day2
        if d1 > d2:
            if d1.days == n*d2.days:
                print(c_date.strftime('%d-%m-%Y'))
        else:
            if d2.days == n*d1.days:
                print(c_date.strftime('%d-%m-%Y'))
                
                
b_day1 = input("Input first birthday (DD-MM-YYYY HH:MI:SS)? ")
b_day1 = datetime.datetime.strptime(b_day1, '%d-%m-%Y %H:%M:%S')
b_day2 = input("Input second birthday (DD-MM-YYYY HH:MI:SS)? ")
b_day2 = datetime.datetime.strptime(b_day2, '%d-%m-%Y %H:%M:%S')
n_day(b_day1, b_day2, 3)
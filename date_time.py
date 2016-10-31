# Author: Bojan G. Kalicanin
# Date: 31-Oct-2016
# The datetime module provides date and time objects that are similar to
# the Date and Time objects in this chapter, but they provide a rich set
# of methods and operators. Read the documentation at
# http://docs.python.org/2/library/datetime.html.
# 1. Use the datetime module to write a program that gets the current
#    date and prints the day of the week.
# 2. Write a program that takes a birthday as input and prints the
#    user's age and the number of days, hours, minutes and seconds until
#    their next birthday.

import datetime
import calendar

c_time = datetime.datetime.today()
d = c_time.weekday()
print(calendar.day_name[d])

birthday = input("Enter the birthday in the format dd-mm-yyyy HH:MM:SS? ")
b_day = datetime.datetime.strptime(birthday, '%d-%m-%Y %H:%M:%S')
next_bday = str(int(c_time.strftime('%Y')) + 1) + "-" + b_day.strftime('%m-%d %H:%M:%S')
n_bday = datetime.datetime.strptime(next_bday, '%Y-%m-%d %H:%M:%S')
print(next_bday)
if datetime.datetime.strptime(c_time.strftime("%d-%m"), "%d-%m") >= datetime.datetime.strptime(b_day.strftime("%d-%m"), "%d-%m"):
    age = int(c_time.strftime('%Y')) - int(b_day.strftime('%Y')) - 1
else:
    age = int(c_time.strftime('%Y')) - int(b_day.strftime('%Y'))

print("User is old: " + str(age))
until_next = n_bday - c_time
print("Until next birthday: " + str(until_next.days) + " days.")
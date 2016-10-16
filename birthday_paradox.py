# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# The (so-called) Birthday Paradox:
# 1. Write a function called has_duplicates that takes a list and
#    returns True if there is any element that appears more than once.
#    It should not modify the original list.
# 2. If there are 23 students in your class, what are the chances that
#    two of you have the same birthday? You can estimate this
#    probability by generating random samples of 23 birthdays and
#    checking for matches.
#    Hint: you can generate random birthdays with the randint function
#    in the random module.

import random

def has_duplicates(t):
    """Check for duplicate elements in a list."""
    for i in range(len(t) - 1):
        if t[i] in t[i+1:]:
            return True
    return False
    
def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length (n)."""
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t
    
def count_matches(students, samples):
    """
    Generate samples of students, and count how many of them have at
    least one pair of students with the same birthday.
    """
    count = 0
    for i in range(samples):
        t = random_bdays(students)
        if has_duplicates(t):
            count += 1
    return count
    
    
num_students = 23
num_simulations = 1000
count = count_matches(num_students, num_simulations)

print("After {0:d} simulations".format(num_simulations))
print("with {0:d} students".format(num_students))
print("there were {0:d} simulations with at least one match".format(count))
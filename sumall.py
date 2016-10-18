# Author: Bojan G. Kalicanin
# Date: 18-Oct-2016
# Write a function called sumall that takes any number of arguments and
# returns their sum.

def sumall(*args):
    """Take any number of arguments and calculate their sum."""
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == '__main__':
    t = (1, 2, 3, 5)
    s = sumall(*t)
    print(s)
    s = sumall(4, 5, 10)
    print(s)
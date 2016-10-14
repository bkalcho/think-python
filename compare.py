# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Function that return 1 if x > y, 0 if x = y and -1 if x < y.

def compare(x, y):
    """Return 1 if x > y, 0 if x = y, and -1 if x < y."""
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0
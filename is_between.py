# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Write function that checks if some number is between other two numbers

def is_between(x, y, z):
    """Check if x <= y <= z."""
    return (x <= y) and (y <= z)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    a = is_between(4, 5, 7)
    b = is_between(8, 23, 5)
    print(a, b)
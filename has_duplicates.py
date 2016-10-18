# Author: Bojan G. Kalicanin
# Date: 18-Oct-2016
# If you did Exercise 10.8, you already have a function named
# has_duplicates that takes a list as a parameter and returns True if
# there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

def has_duplicates(t):
    """
    Take a list, and return True if some element appears more than once
    in the list.
    """
    d = dict()
    for i in t:
        d[i] = d.get(i, 0) + 1
        if d[i] > 1:
            return True
    return False
    # 2nd solution
    #for i in t:
    #    if i in d:
    #        return True
    #    else:
    #        d[i] = 1
    #return False


if __name__ == '__main__':
    s = 'banana'
    t = list(s)
    r = has_duplicates(t)
    print(r)
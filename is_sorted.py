# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Write a function called is_sorted that takes a list as a parameter and
# returns True if the list is sorted in ascending order and False
# otherwise. You can assume (as a precondition) that the elements of the
# list can be compared with the relational operators <, >, etc.

def is_sorted(t):
    """Return True if a list is sorted in ascending order."""
    i = 0
    while i < len(t) - 1:
        if t[i + 1] < t[i]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    t = [1, 2, 2, 4]
    a = ['a', 'b', 'c']
    b = ['b', 'a', 'd']
    print(is_sorted(t))
    print(is_sorted(a))
    print(is_sorted(b))
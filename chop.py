# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Write a function called chop that takes a list, modifies it by
# removing the first and last elements, and returns None.

def chop(t):
    """Chop first and last elements from the list."""
    t.pop()
    t.pop(0)


if __name__ == '__main__':
    a= [1, 2, 3, 5, 8]
    b = chop(a)
    print(a, b)
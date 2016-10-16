# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Write a function called remove_duplicates that takes a list and
# returns a new list with only the unique elements from the original.
# Hint: they don't have to be in the same order.

def remove_duplicates(t):
    """Return new list with only unique elements."""
    a = []
    for i in t:
        if i not in a:
            a.append(i)
    return a
  
  
s =[1, 2, 3, 2, 2, 5, 6, 6, 8, 8]
a = remove_duplicates(s)
print(a)
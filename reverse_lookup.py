# Author: Bojan G. Kalicanin
# Date: 17-oct-2016
# Modify reverse_lookup so that it builds and returns a list of all keys
# that map to v, or an empty list if there are none.

def reverse_lookup(d, v):
    """
    Reverse lookup in dictionary. If you know a value, find a
    corresponding key.
    """
    t = []
    for k in d:
        if d[k] == v:
            t.append(k)
    if t:
        return t
    else:
        return None
        

d = {1: 'banana', 2: 'flower', 5: 'banana', 10: 'orange'}
v = 'banana'
t = reverse_lookup(d, v)
print(t)
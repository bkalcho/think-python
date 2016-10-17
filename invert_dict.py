# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Read the documentation of the dictionary method setdefault and use it
# to write a more concise version of invert_dict.

def invert_dict(d):
    """
    Invert dictionary. Keys will be values, and values will be keys. If 
    the one value has been assigned to more keys, than in the new
    dictionary, the key will be that value, but the value will be a list
    of keys.
    """
    t = dict()
    for k in d:
        value = d[k]
        t[value] = t.setdefault(value, []) + [k]
        #if value in t:
        #    t[value].append(k)
        #else:
        #    t[value] = [k]
    return t
    

d = {1: 'banana', 2: 'flower', 5: 'banana', 10: 'orange'}
s = invert_dict(d)
print(s)
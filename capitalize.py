# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Capitalize all strings in nested lists

def capitalize_all(t):
    """Capitalize all strings from the list."""
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
    
def capitalize_nested(l):
    """Capitalize all the strings in nested lists."""
    final = []
    for i in l:
        final.append(capitalize_all(i))
    return final
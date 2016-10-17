# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list. Modify print_hist to
# print the keys and their values in alphabetical order.

import histogram

def print_hist(d):
    k = d.keys()
    for c in sorted(k):
        print(c, d[c])
        
a = histogram.histogram('banana')
print_hist(a)
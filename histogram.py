# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Dictionaries have a method called get that takes a key and a default
# value. If the key appears in the dictionary, get returns the
# corresponding value; otherwise it returns the default value.
# Use get to write histogram more concisely. You should be able to
# eliminate the if statement

def histogram(s):
    """Count apperance of the letters in the string."""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
        
        
if __name__ == '__main__':
    s = 'banana'
    print(histogram(s))
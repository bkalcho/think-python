# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Return True if the word contains only letters in the list

def uses_only(word, letters):
    """Check if word contains only letters."""
    for w in word:
        if w not in letters:
            return False
    return True
    

s = uses_only('alfalfa', 'acefhlo')
print(s)
k = uses_only('going', 'aer')
print(k)
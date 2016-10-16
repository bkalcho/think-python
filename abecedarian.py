# Author: Bojan G. Kalicani
# Date: 16-Oct-2016
# Return True if letters in the word appear in alphabetical order

def is_abecedarian(word):
    """Check if letters are in alphabetical order."""
    previous = word[0]
    for w in word:
        if w < previous:
            return False
        previous = c
    return True
    
#def is_abecedarian(word):
#    i = 0
#    while i < len(word) - 1:
#        if word[i+1] < word[i]:
#            return False
#        i += 1
#    return True

#def is_abecedarian(word):
#    if len(word) <= 1:
#        return True
#    if word[0] > word[1]:
#        return False
#    return is_abecedarian(word[1:])
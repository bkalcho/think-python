# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Is one word reverse from another

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
        i = 0
        j = len(word2) - 1
        while j >= 0:
            if word1[i] != word2[j]:
                return False
            i = i+1
            j = j-1
    return True
    
a = is_reverse('stop', 'pots')
print(a)
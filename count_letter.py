# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
#  Count letters in the word

import search_string as ss
def count(string, letter):
    index = 0
    count = 0
    while index < len(string):
        a = ss.find(string, letter, index)
        if a != -1:
            count += 1
            index = a + 1
        else:
            break
    return count
    # Second version
    #count = 0
    #for l in word:
    #    if l == letter:
    #        count += 1
    #return count
    
    
n = count('latitude', 't')
print(n)
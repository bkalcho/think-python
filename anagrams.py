# Author: Bojan G. Kalicanin
# Date: 19-Oct-2016
# 1. Write a program that reads a word list from a file
# (see Section 9.1) and prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a set of
# letters to a list of words that can be spelled with those letters.
# The question is, how can you represent the set of letters in a way
# that can be used as a key?
# 2. Modify the previous program so that it prints the largest set of
# anagrams first, followed by the second largest set, and so on.
# 3. In Scrabble a “bingo” is when you play all seven tiles in your
# rack, along with a letter on the board, to form an eight-letter word.
# What set of 8 letters forms the most possible bingos?
# Hint: there are seven.

def read_file(filename):
    """Function that reads file and return a list of words."""
    t = []
    f_obj = open(filename)
    for line in f_obj:
        word = line.strip().lower()
        t.append(word)
    return t

def word_sig(word):
    """Returns word in alphabetical order."""
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t
        
def search_anagrams(words):
    """Search for the list of anagrams."""
    d = {}
    for w in words:
        s = word_sig(w)
        if s not in d:
            d[s] = [w]
        else:
            d[s].append(w)
    return d

def print_anagram_sets(d):
    """Print the anagram sets in d."""
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)
            
def print_anagram_sets_in_order(d):
    """Print anagram sets in d in descending order."""
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    
    t.sort()
    
    for i in t:
        print(i)

def filter_length(d, n):
    """Select only anagrams in d which have length of n."""
    res ={}
    for k, v in d.items():
        if len(k) == n:
            res[k] = v
    return res

s =[]
filename = 'words.txt'
t = read_file(filename)
d = search_anagrams(t)
print_anagram_sets_in_order(d)

eight_letter = filter_length(d, 8)
print_anagram_sets_in_order(eight_letter)
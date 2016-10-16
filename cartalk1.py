# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Exercise 9.7. This question is based on a Puzzler that was broadcast
# on the radio program Car Talk
# (http: // www. cartalk. com/ content/ puzzlers ): Give me a word with
# three consecutive double letters. I'll give you a couple of words
# that almost qualify, but don't. For example, the word committee,
# c-o-m-m-i-t-t-e-e. It would be great except for the 'i'' that sneaks in
# there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out
# those i's it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge this may
# be the only word. Of course there are probably 500 more but I can only
# think of one. What is the word? Write a program to find it.

def test_consecutive(word):
    """Test if word has three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False
    
def find_tripple_double():
    """Read word list and find tripple doubles words."""
    f_obj = open('words.txt')
    for line in f_obj:
        line = line.strip()
        if test_consecutive(line):
            print(line)
            
            
print("Tripple doubles from the list:\n")
find_tripple_double()
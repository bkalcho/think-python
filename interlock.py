# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Two words "interlock" if taking alternating letters from each forms a
# new word. For example, "shoe" and "cold" interlock to form "schooled."
#
# 1. Write a program that finds all pairs of words that interlock.
#    Hint: don't enumerate all pairs!
# 2. Can you find any words that are three-way interlocked; that is,
#    every third letter forms a word, starting from the first, second or
#    third?

import bisect

def interlock(l_words, word):
    """Check if the word can be split into two interlocked words."""
    evens = word[::2]
    odds = word[1::2]
    return bisect.bisect(l_words, evens) and bisect.bisect(l_words, odds)

def general_interlock(l_words, word, n=3):
    """Checks if the word can be split into n interlocked words."""
    for i in range(n):
        inter = word[i::n]
        if not bisect.bisect(l_words, inter):
            return False
    return True


if __name__ == '__main__':
    t = []
    f_obj = open('words.txt')
    for line in f_obj:
        w = line.strip()
        t.append(w)
    f_obj.close()

    for word in t:
        if interlock(t, word):
            print(word, word[::2], word[1::2])

    for word in t:
        if general_interlock(t, word, 3):
            print(word, word[::3], word[1::3], word[2::3])
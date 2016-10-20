# Author: Bojan G. Kalicanin
# Date: 20-Oct-2016
# Exercise 13.6. Python provides a data structure called set that
# provides many common set operations. Read the documentation at
# http://docs.python.org/2/library/stdtypes.html#types-set and write a
# program that uses set subtraction to find words in the book that are
# not in the word list.

import string

def common_words(s, words):
    """
    Find the words in the set that are not in the word list.

    s: set of words.
    words: list of words.
    """
    w = set(words)
    sub = s - w
    return sub


def read_book(filename):
    """Read a filename and return a set of words, from a file."""
    s = set()
    f_obj = open(filename)
    for line in f_obj:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation + string.whitespace)
            if word not in s:
                s.add(word)
    f_obj.close()
    return s


if __name__ == '__main__':
    filename = 'art_of_war.txt'
    t = list()
    f_obj = open('words.txt')
    for line in f_obj:
        word = line.strip()
        t.append(word)
    f_obj.close()
    s = read_book(filename)
    res = common_words(s, t)
    print("Words not in the list:")
    for i in res:
        print(i)
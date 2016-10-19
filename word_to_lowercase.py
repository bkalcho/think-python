# Author: Bojan G. Kalicanin
# Date: 19-Oct-2016
# Write a program that reads a file, breaks each line into words, strips
# whitespace and punctuation from the words, and converts them to
# lowercase.

import string

def read_file(filename):
    """Function that reads a file, and returns list of words."""
    t = list()
    flag = False
    f_obj = open(filename)
    for line in f_obj:
        # Skip header of the book, using flag variable
        if line.strip() == "Changes made are listed at the end of the text.":
            flag = True
            continue
        if flag == True:
            words = line.split()
            for word in words:
                t.append(word)
    return t

def convert_to_lower(word):
    """Convert word to lowercase, and strip punctuation."""
    separators = string.whitespace + string.punctuation
    word = word.lower().strip(separators)
    return word

def not_in_book(t):
    """
    Read a word list, and print word from the list t, which are not in
    list words.
    """
    d = {}
    f_obj = open('words.txt')
    for line in f_obj:
        word = line.strip()
        d[word] = word
        
    for w in t:
        if w not in d:
            print(w)


if __name__ == '__main__':
    filename = 'art_of_war.txt'
    t = read_file(filename)
    for i in range(len(t)):
        t[i] = convert_to_lower(t[i])

    word_num = len(t)
    d = {}
    for i in t:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    diff_words = len(d)
    print("Total number of words in a book: " + str(word_num))
    print("Number of different words used in a book: " + str(diff_words))
    h = []
    for k, v in d.items():
        h.append((v, k))
    h.sort(reverse=True)
    print("Word occurences in descending order (top 20):")
    for i in range(20):
        print(h[i][0], h[i][1])
        
    not_in_book(t)
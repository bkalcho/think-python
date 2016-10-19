# Author: Bojan G. Kalicanin
# Date: 18-Oct-2016
# Two words are "rotate pairs" if you can rotate one of them and get the
# other (see rotate_word in Exercise 8.12).
# Write a program that reads a wordlist and finds all the rotate pairs.

def rotate_letter(letter, n):
    """Rotate letter for n spaces."""
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    """Rotate word for n spaces."""
    w = ''
    for c in word:
        w += rotate_letter(c, n)
    return w

def make_word_dict(filename):
    """Make word dictionary from the list of words in the file."""
    d = dict()
    f_obj = open(filename)
    for line in f_obj:
        word = line.strip()
        d[word] = word
    f_obj.close()
    return d

def rotate_pairs(word, d):
    """Print all words that can be generated by rotating a word."""
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in d:
            print(word, i, rotated)


if __name__ == '__main__':
    filename = 'words.txt'
    word_dict = make_word_dict(filename)
    for w in word_dict:
        rotate_pairs(w, word_dict)
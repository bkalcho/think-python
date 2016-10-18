# Author: Bojan G. Kalicanin
# Date: 18-Oct-2016
# Write a function called most_frequent that takes a string and prints
# the letters in decreasing order of frequency. Find text samples from
# several different languages and see how letter frequency varies
# between languages.

def histogram(string):
    h = {}
    for i in string:
        h[i] = h.get(i, 0) + 1
    return h

def most_frequent(string):
    h = histogram(string)
    t = []
    for c, f in h.items():
        t.append((f, c))

    t.sort(reverse=True)

    k = []
    for f, c in t:
        k.append(c)
    return k


if __name__ == '__main__':
    string = open('words.txt').read()
    t = most_frequent(string)
    for i in t:
        print(i)
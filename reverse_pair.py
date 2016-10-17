# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Two words are a "reverse pair" if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.

import bisect

t = []
f_obj = open('words.txt')
for line in f_obj:
    w = line.strip()
    t.append(w)
f_obj.close()

r = []
for l in t:
    if l not in r:
        i = bisect.bisect(t, l[::-1])
        if i:
            r.append([l, t[i]])

print("The list of all reversed pairs:")
print(r)
# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Write a function that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn't matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in
# the dictionary.

import bisect
import time

def search_dict(filename, string):
    """
    Read words from a filename and store them as keys in a dictionary.
    """
    d = dict()
    f_obj = open(filename)
    for line in f_obj:
        w = line.strip()
        d[w] = ''
    f_obj.close()
    
    return string in d

start_time = time.time()
filename = 'words.txt'
string = 'zymurgy'
print(search_dict(string=string, filename=filename))
end_time = time.time() - start_time
print("Execution time: " + str(end_time) + " seconds.")

start_time = time.time()
t = []
f_obj = open('words.txt')
for line in f_obj:
    w = line.strip()
    t.append(w)
f_obj.close()
result = bisect.bisect(t, string)
print(result)
end_time = time.time() - start_time
print("Execution time: " + str(end_time) + " seconds.")

start_time = time.time()
if string in t:
    print(True)
else:
    print(False)
end_time = time.time() - start_time
print("Execution time: " + str(end_time) + " seconds.")
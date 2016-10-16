# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Write a function that reads the file words.txt and builds a list with
# one element per word. Write two versions of this function, one using
# the append method and the other using the idiom t = t + [x]. Which one
# takes longer to run? Why?
# Hint: use the time module to measure elapsed time.

import time

time.perf_counter()
def list_words1(filename):
    t = []
    f_obj = open(filename)
    for line in f_obj:
        word = line.strip()
        t.append(word)
    return t
        
def list_words2(filename):
    t = []
    f_obj = open(filename)
    for line in f_obj:
        word = line.strip()
        t = t + [word]
    return t
    
    
start_time = time.time()
t = list_words1('words.txt')
elapsed_time = time.time() - start_time
print(len(t))
print(t[:10])
print(str(elapsed_time) + " seconds")

start_time = time.time()
t = list_words2('words.txt')
elapsed_time = time.time() - start_time
print(len(t))
print(t[:10])
print(str(elapsed_time) + " seconds")
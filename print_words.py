# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Print only words with more than 20 characters

f_obj = open('words.txt')
for line in f_obj:
    if len(line.strip()) > 20:
        print(line)
        
f_obj.close()
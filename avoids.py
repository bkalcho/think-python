# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# 

def avoids(word, letters):
    """Take a word, and a string of forbidden letters."""
    for l in word:
        if l in letters:
            return False
    return True
    

while True:
    prompt = "Enter the string of forbidden letters."
    prompt += "\n(enter 'done' to quit) "
    s = input(prompt)
    if s == 'done':
        break
    f_obj = open('words.txt')
    count = 0
    for line in f_obj:
        r = avoids(line.strip(), s)
        if r:
            count += 1
    f_obj.close()
    print(count)
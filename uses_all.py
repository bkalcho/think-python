# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Return true if the word uses all the required letters from the string
# at least once.

def uses_all(word, letters):
    """
    Checks if word uses all letters from string letters at least once.
    """
    for l in letters:
        if not l in word:
            return False
    return True
    

while True:
    prompt = "Enter required letters"
    prompt += "\n(enter 'done' to quit) "
    required = input(prompt)
    if required == 'done':
        break
    f_obj = open('words.txt')
    count = 0
    for line in f_obj:
        line = line.strip()
        if uses_all(line, required):
            count += 1
    
    f_obj.close()
    print(count)
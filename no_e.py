# Author: Bojan G. Kalicanin
# Date: 26-Oct-2016
# Chek for e letter

def has_no_e(word):
    """Check if there is no e letter in word."""
    for w in word:
        if w == 'e':
            return False
    return True
           

has_e = 0
count = 0            
while True:
    prompt = "Enter words for which you wish to check if they have 'e'."
    prompt +="\n(enter 'done' to quit) "
    s = input(prompt)
    if s == 'done':
        p = (has_e / count) * 100
        print(round(p, 2))
        break
    if has_no_e(s):
        has_e += 1
        print(s)
    count += 1
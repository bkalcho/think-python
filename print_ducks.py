# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Print duck names in order
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter != 'O' and letter != 'Q':
        print(letter + suffix)
    else:
        print(letter + 'u' + suffix)
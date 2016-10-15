# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Displays the string backwards

def reverse_string(string):
    """Display string backwards."""
    i = 0
    s = ''
    while i < len(string):
        s += string[len(string) - (i + 1)]
        i += 1
        
    print(s)
    
    
reverse_string('example')
# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Evaluates expression that user enters

def eval_loop():
    """Evaluate users input."""
    while True:
        string1 = "Enter expression you wish to be evaluated?"
        string1 += "\n(write 'done' if you wish to stop) "
        exp = input(string1)
        if exp == 'done':
            break
        print("The result of expression " + exp + " is: " + \
            str(eval(exp)))
            
            
eval_loop()
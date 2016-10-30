# Author: Bojan G. Kalicanin
# Date: 30-Oct-2016
# 1. Write a program that creates a Canvas and a Button. When the user
# presses the Button, it should draw a circle on the canvas.
# 2. Modify your solution to Exercise 19.2 by adding an Entry widget and
# a second button. When the user presses the second button, it should
# read a color name from the Entry and use it to change the fill color
# of the circle. Use config to modify the existing circle; don’t create
# a new one.
# Your program should handle the case where the user tries to change the
# color of a circle that hasn't been created, and the case where the
# color name is invalid.

import swampy.Gui as gui

def create_circle():
    """Create circle on the canvas."""
    global item
    item = canvas.circle([0, 0], 80, fill='cyan')
    item.config(outline='magenta', width=3)
    
def handle_event():
    """Handle events, when the user presses 'change color' button."""
    if item == None:
        return
    color = entry.get()
    try:
        item.config(fill=color)
    except:
        # an unknown color name
        print('Unknown color')


g = gui.Gui()
g.title('Canvas title')
button = g.bu(text='create circle', command=create_circle)
canvas = g.ca(width=500, height=500, bg='white')
entry = g.en()
button2 = g.bu(text='change color', command=handle_event)

g.mainloop()
# Author: Bojan G. Kalicanin
# Date: 30-Oct-2016
# Write a program that creates a GUI with a single button. When the
# button is pressed it should create a second button. When that button
# is pressed, it should create a label that says, "Nice job!".

import swampy.Gui as gui

def create_label():
    """Function which creates a label."""
    g.la(text="Nice job!")
    
def create_button():
    """Function which creates a button widget."""
    g.bu(text='button', command=create_label)
    
# Create a frame, which will hold the widgets
g = gui.Gui()
g.title('Button demo')
# Create a button widget
button1 = g.bu(text='first button', command=create_button)

g.mainloop()
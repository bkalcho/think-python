# Author: Bojan G. Kalicanin
# Date: 30-Oct-2016
#

from swampy.Gui import *

def make_label():
    """Function which creates a label."""
    g.la(text='Thank you.')
    
def set_color(color):
    mb.config(text=color)
    print(color)


# Creates a frame, which will contain a widgets
g = Gui()
g.title('Gui')

# Creates a button widget
button = g.bu(text='Press me')
# Create a label widget
label = g.la(text='Press the button')
button2 = g.bu(text='No, press me!', command=make_label)
# Create a canvas widget
#canvas = g.ca(width=500, height=500)
# Use config method to change canvas options
#canvas.config(bg='white')
# To draw a circle item on the canvas use circle method
#item = canvas.circle([0, 0], 100, fill='red')
# Use config method to change any of the item circle options
#item.config(fill='yellow', outline='orange', width=10)

canvas1 = g.ca(width=500, height=300, bg='white')
# Draw a rectangle by taking coordinates of the two opposite corners,
# lower left and upper right
item1 = canvas1.rectangle([[0, 0], [200, 100]], fill='blue',
    outline='orange', width=10)
# oval takes a bounding box and draws an oval within the specified
# rectangle
item2 = canvas1.oval([[0, 0], [200, 100]], outline='orange', width=10)

# line takes a sequence of coordinates and draws a line that connects
# the points.
#item3 = canvas.line([[0, 100], [100, 200], [200, 100]], width=10)

# polygon takes the same arguments, but it draws the last leg of the
# polygon (if necessary) and fills it in.
#item4 = canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='red',
#    outline='orange', width=10)

# en method creates an entry, a widget that allows a user to type text
# but on a single line.
entry = g.en(text='Default text.')
# The text option allows you to put text into the entry when it is
# created. The get method returns the contents of the Entry (which may
# have been changed by the user)
entry.get()

# te creates a Text widget -> a multiline text input field
text = g.te(width=100, height=5)
text.insert(END, 'A line of the text.')
text.get(0.0, END)
text.delete(1.2, END)
text.get(0.0, END)

# Create a menu button
g.la('Select a color:')
colors = ['red', 'green', 'blue']
mb = g.mb(text=colors[0])
for color in colors:
    g.mi(mb, text=color, command=Callable(set_color, color))


g.mainloop()
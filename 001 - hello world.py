
# free code camp - tkinter tutorial

from tkinter import *

root = Tk() # the window, all other widgets will sit on

#1 create label widget
myLabel = Label(root, text="hello world")

#2 pack it in / add to screen / unsophisticated, non-specific placing
myLabel.pack()

#3 gui needs to loop continuously (ie respond to mouse movement, clicks etc)
root.mainloop()


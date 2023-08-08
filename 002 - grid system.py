
# free code camp - grid system

from tkinter import *

root = Tk()

#creating widgets
myLabel1 = Label(root, text="hello world")
myLabel2 = Label(root, text="Alex")
myLabel3 = Label(root, text="x")

#adding widgets to the root object / put on screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=1,column=1)

#looping the mindow
root.mainloop()
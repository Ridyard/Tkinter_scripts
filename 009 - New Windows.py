# codemy - new windows

from tkinter import *

root = Tk()
root.title('First Window')

def openNewWindow():
    top = Toplevel() # use top level rather than using multiple instances of the Tk() object
    top.title('my second window')
    lbl = Label(top, text='you opened me!').pack()
    b2 = Button(top, text='close window', command=top.destroy).pack() # seemingly command arg doesn't require parentheses

b1 = Button(root, text='open second window', command=openNewWindow).pack()


root.mainloop()
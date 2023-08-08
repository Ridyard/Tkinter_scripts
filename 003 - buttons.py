
# free code camp - buttons

from tkinter import *

root = Tk()


#define a function to run when the button is clicked
def myClick():
    myLabel = Label(root, text='you clicked a button!')
    myLabel.pack()


myButton = Button(root, text="click me", command=myClick) # command executes upon button click; dont need trailing () when executing a button click
myButton.pack()

root = mainloop()


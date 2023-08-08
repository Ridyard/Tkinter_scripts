# codemy - radiobuttons, basic, ver1

from tkinter import *

root = Tk()
root.title('radio buttons')

r = IntVar() # to hold the radiobutton value / variable
r.set('2') # set a default value

# when a radio button is clicked, the relevant value is passed in and the label is updated
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#radio button widgit
Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack() # when radio is clicked, the value is 1
Radiobutton(root, text='option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# will show the corresponding value from the radio button selected
myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text='click me', command= lambda: clicked(r.get()))
myButton.pack()
mainloop()

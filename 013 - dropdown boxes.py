# codemy - dropdown box

from tkinter import *
root = Tk()
root.geometry("400x400")

# add dropdown selection to the label
def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

options = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

clicked=StringVar()
clicked.set("Select Day") # set default option on dropdown

d1 = OptionMenu(root, clicked, *options) #d1 relates to clicked obj; options refers to the dropdown options list (mon-fri), the syntax is *options
d1.pack()

myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()
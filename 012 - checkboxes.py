# codemy - tkinter, checkboxes

from tkinter import *

root = Tk()
root.title('checkboxes')
root.geometry('400x400')

#update the label with the checkbox return value, 0 or 1
def screenUpdate():
    myLabel = Label(root, text=var.get()).pack()

# update label with string values    
def screenUpdate2():
    myLabel2 = Label(root, text=var2.get()).pack()
 


# need to use tkinter variables, using getters and setters
var = IntVar()
var2 = StringVar()

cb = Checkbutton(root, text='ham', variable=var, command=screenUpdate)
cb2 = Checkbutton(root, text='cheese', variable=var2, command=screenUpdate2, onvalue='on', offvalue='off')

cb.pack()
cb2.pack()


root.mainloop()
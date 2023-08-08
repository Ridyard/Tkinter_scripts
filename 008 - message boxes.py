
#codemy - tkinter, message boxes

from tkinter import *
from tkinter import messagebox

#declare the root window
root = Tk()
root.title('message boxes')

#functions to handle the message box commands triggered by the button 'command' parameter
# different functions will have different return items (0/1, y/n, ok etc)
def popupInfo():
    messagebox.showinfo('info pop-up', 'you clicked the button') # will show info msgbox, with title & msg content

def popupYN():
    response = messagebox.askyesno('Warning pop-up', 'did you intend to click that button?') # 'askyesno' will return a boolean value. will assign the user choice to 'responce'
    if response == 1:
        Label(root, text='okiedoke, you clicked \'yes\'').pack()
    else:
        Label(root, text='you clicked \'no\'').pack()

def popupQuestion():
    response = messagebox.askquestion('info pop-up', 'did you click the button?') # will show 'ask q' msgbox, with title & msg content
    if response == 'yes': # ask question returns 'yes' or 'no', not a boolean 0/1 value
        Label(root, text='okiedoke, you clicked \'yes\'').pack()
    else:
        Label(root, text='you clicked \'no\'').pack()

#create buttons, attach functions & pack on root
b1 = Button(root, text='pop-up 1', command=popupInfo).pack()
b2 = Button(root, text='pop-up 2', command=popupYN).pack()
b3 = Button(root, text='pop-up 3', command=popupQuestion).pack()




mainloop()


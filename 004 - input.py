
# free code camp - input boxes
# get user to enter name and output a greeting

from tkinter import *
import random

root = Tk()
greetings = ['hello','good morning','greetings','good evening','salutations','ahoy']

# input fields are entry objects
e = Entry(root, width=30, bg='#88d5ff')
e.insert(0,'enter your name:')
e.pack()

#runs when the button is clicked
def myClick():
    gr = random.choice(greetings) + ' ' + e.get()
    myLabel = Label(root, text=gr) # prints a random greeting & the user's name / entry
    myLabel.pack()


myButton = Button(root, text="click me", command=myClick) # command executes upon button click; dont need trailing () when executing a button click
myButton.pack()

root = mainloop()
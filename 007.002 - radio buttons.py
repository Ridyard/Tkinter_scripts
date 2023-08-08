#codaemy - radiobuttons using loops, ver 2

from tkinter import *

root = Tk()
root.title('radio buttons')

# list of tuples to hold the radiobutton values
toppings = [
    ("pepperoni","pepperoni"), # items taken as text & topping
    ("cheese","cheese"), # items taken as text & topping...
    ("mushroom","mushroom"),
    ("chicken","chicken")
]

pizza = StringVar()
pizza.set("pepperoni")

# we use a loop rather than manually adding radiobuttons
for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# when a radio button is clicked, the relevant value is passed in and the label is updated
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text='click me', command= lambda: clicked(pizza.get()))
myButton.pack()
mainloop()


# build a simple calculator app

#TODO:
# review if there is a better way to implement, ie the use of global variables
# make front end look like windows calc
# add scientific calcs
# add binary converter (see projects)

from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, pady=10, columnspan=3) # file will "span" 3 columns (or buttons)

#handle the number-button clicks
def button_click(num):
    #handles getting the correct number on screen by clearing & concatenating nums entered, ie for > single digit numbers
    currentNum = e.get() 
    e.delete(0, END) 
    e.insert(0, str(currentNum) + str(num)) 

# handle clear button
def button_clear():
    e.delete(0, END)
    

# handle arithetic buttons
def button_add():
    first_number = e.get()
    global f_num # to be used by button_equal
    global operation
    operation = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num # to be used by button_equal
    global operation
    operation = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num # to be used by button_equal
    global operation
    operation = "divide"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num # to be used by button_equal
    global operation
    operation = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get() # pull number from text box
    e.delete(0, END)
    if operation == "add":
        e.insert(0, f_num + int(second_number))
    if operation == "subtract":
        e.insert(0, f_num - int(second_number))
    if operation == "divide":
        e.insert(0, f_num / int(second_number))
    if operation == "multiply":
        e.insert(0, f_num * int(second_number))




# define the buttons
#you can't call functions & pass parameters within a button eg "butt_click(1)"...
#you have to use a lambda function and call the funct with a parameter that way.
#pass the number associated with the button to the button_click function.
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=39, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=39, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=39, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add) #not passing an arg so don't need the lambda
buttonSub = Button(root, text="-", padx=41, pady=20, command=button_sub) #not passing an arg so don't need the lambda
buttonDiv = Button(root, text="/", padx=41, pady=20, command=button_div) #not passing an arg so don't need the lambda
buttonMultiply = Button(root, text="*", padx=39, pady=20, command=button_multiply) #not passing an arg so don't need the lambda

buttonEqual = Button(root, text="=", padx=86, pady=20, command=button_equal)
buttonClear = Button(root, text="C/E", padx=80, pady=20, command=button_clear) #command=lambda: button_clear()) #strictly speaking we don't need the lambda as we're not passing a parameter


#put buttons on the screen / root object
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonSub.grid(row=6, column=0)
buttonDiv.grid(row=6, column=1)
buttonMultiply.grid(row=6, column=2)

# loop the main window
root.mainloop()


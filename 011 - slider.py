# codemy - tkinter; sliders
# resize the tkinter window using sliders

from tkinter import *

root = Tk()
root.title('sliders')
root.geometry('350x350')

#this will get the slider x & y values and re-size the root window accordingly
def slide():
    myLabel = Label(root, text=f'{str(horiz.get())}x{str(vert.get())}')
    myLabel.pack()
    root.geometry(f'{str(horiz.get())}x{str(vert.get())}')


#scale() refers to the slider - they retunr a number (that the user slides to)
#from_ arg has to have the trailing _ for some reason
#default axis is vertical; you would need to specify if this is meant to be horizontal
vert = Scale(root, from_=200, to=600)
vert.pack() # you have to pack() sliders on their own line, ie you can't pack on the end of the above line

horiz = Scale(root, from_=200, to=600, orient=HORIZONTAL)
horiz.pack()

myButton = Button(root, text='click me', command=slide)
myButton.pack()

root.mainloop()
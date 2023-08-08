# codemy - file dialog
# user to select image from a given dir and opens in a label

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title('file dialog boxes')

def open():
    global myImage #need to reference the global variable when working with images in a function with tkinter

    #filedialog.askopenfile() is a method of the filedialog class, whjich we imported. It returns a file path, 
    # so in this case, the fp to the user-selected item 
    #initialdir shows the default location for the dialog window
    #filetypes takes a tuple of a user given desc (this is free-typed), followed by the file type delimiter, in this case .jpg & all files
    root.filename = filedialog.askopenfilename(initialdir=r'C:\Users\alexa\Pictures\Wallpapers', title='select a .jpg wallpaper', filetypes=(('jpg files', '*.jpg'),('all files','*.*')))

    myLabel = Label(root, text=root.filename).pack()
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel = Label(image=myImage).pack()


myButton = Button(root, text='open file:', command=open).pack()


root.mainloop()
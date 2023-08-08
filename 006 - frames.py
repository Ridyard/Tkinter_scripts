from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("working with frames")

#create widgit
frame1 = LabelFrame(root, text="my frame...", padx=5, pady=5) # padding relative to the inside of the frame
frame1.pack(padx=100, pady=100) # padding relative to the outside of the frame

b = Button(frame1, text="don't click me...") # not we add the button to frame1 (not root), which sits on root
b.pack()

root.mainloop()
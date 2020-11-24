from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


myButton = Button(root, text="Click me!", padx=50, command=myClick).pack()

root.mainloop()


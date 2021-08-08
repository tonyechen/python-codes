from tkinter import *
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg = colorchooser.askcolor()[1]) # change background color

window = Tk()

window.geometry("420x420")
# if no master window is passed, the widget will appear on the first declared window
button = Button(window, text = "lick me", command = click)
button.pack()

window.mainloop()

from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x) + ", " + str(event.y))

def leave(event):
    quit()

window = Tk()

window.bind("<Button-1>", doSomething) # mouse left click
window.bind("<Button-2>", doSomething) # scroll whell click
window.bind("<Button-3>", doSomething) # mosue right click
window.bind("<ButtonRelease>", doSomething) # release
window.bind("<Enter>", doSomething) # enter the window
window.bind("<Leave>", leave) # leave the window
window.bind("<Motion>", doSomething) # Where the mouse moved

window.mainloop()


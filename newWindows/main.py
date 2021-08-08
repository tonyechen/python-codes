from tkinter import *

def createWindow():
    new_window = Tk()       # Toplevel() ew window 'on top' of other windows, linked to a 'bottom' window
                            # Tk() = new independent window
    old_window.destroy()    # close out of old window


old_window = Tk()

Button(old_window, text ="create new window", command = createWindow).pack()

old_window.mainloop()
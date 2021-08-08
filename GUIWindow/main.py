# Graphical User Interface

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("1920x1280") # width x height
window.title("Tony's first GUI program")
window.config(background = "orange") # can also use a hex color representation

icon = PhotoImage(file = "dices.png") # have to use PIL for jpg images
window.iconphoto(True, icon)


window.mainloop() # placed window on computer screen, listen for events

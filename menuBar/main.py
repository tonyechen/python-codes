from tkinter import *

def openFile():
    print("File has been opened.")

def saveFile():
    print("File has been saved.")

def cut():
    print("You cut some text.")

def copy():
    print("You copied some text.")

def paste():
    print("You paste some text.")
window = Tk()

image = PhotoImage(file = "hamburger.png")

menubar = Menu(window)
window.config(menu = menubar)
print(menubar.keys())

fileMenu = Menu(menubar, tearoff = 0, font = ("MV Boli", 15))
menubar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Open", command = openFile, image = image, compound = LEFT)
fileMenu.add_command(label = "Save", command = saveFile, image = image, compound = LEFT)
fileMenu.add_separator() # add separater
fileMenu.add_command(label = "Exit", command = quit, image = image, compound = LEFT)

editMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut", command = cut)
editMenu.add_command(label = "Copy", command = copy)
editMenu.add_command(label = "Paste", command = paste)

sideMenu = Menu(editMenu, tearoff = 0)
editMenu.add_cascade(label = "Secret Stuff", menu = sideMenu)
sideMenu.add_command(label = "some secrets")



window.mainloop()
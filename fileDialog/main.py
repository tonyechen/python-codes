from tkinter import *
from tkinter import filedialog

def openFile():
    filePath = filedialog.askopenfilename(initialdir = "C:\\Users\\fchen\\PycharmProjects\\fileDialog",
                                        title = "Open file okay?",
                                        filetypes = (("text files", "*.txt"),("all files", "*.*")))
    file = open(filePath, "r")
    print(file.read())
    file.close()

window = Tk()

button = Button(text = "Open", command = openFile)
button.pack()

window.mainloop()
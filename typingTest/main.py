# typing speed test program
# 8/1/2021

from tkinter import *
import time
from TextLine import *

def clear(event):
    global current_index
    current_index += 1

    str = entry.get()
    print(str)

    entry.delete(0, END)


window = Tk()

WIDTH = 1500
font = ("Arial", 20)
window.geometry(str(WIDTH) + "x500")

text = TextLine(window, 1000, "light green", font)
text2 = TextLine(window, 1000, "light green", font)

entry = Entry(window, font = font)
entry.pack()

button = Button(window, font = font, text = "start")
button.pack()

window.bind("<space>", clear)

current_index = 0
while True:
    text.select(current_index)
    window.update()

window.mainloop()
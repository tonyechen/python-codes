# frame = a rectangular comtainer to group and hold widgets

from tkinter import *

window = Tk()
window.geometry("500x500")

frame = Frame(window, bg = "light blue", bd = 5, relief = SUNKEN, width = 100)
frame.pack()

Button(frame, text = "W", font = ("Consolas", 25), width = 3).pack(side = TOP)
Button(frame, text = "A", font = ("Consolas", 25), width = 3).pack(side = LEFT)
Button(frame, text = "S", font = ("Consolas", 25), width = 3).pack(side = LEFT)
Button(frame, text = "D", font = ("Consolas", 25), width = 3).pack(side = LEFT)

print(frame.winfo_width())
window.mainloop()
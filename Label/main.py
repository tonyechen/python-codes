# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file = 'C:\\Users\\fchen\\Pictures\\dices.png')

label = Label(window,
              text = "Hello World",
              font = ("Arial", 40, "bold"),
              fg = "#00FF00",
              bg = "black",
              relief = RAISED,  # or sunken
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = "bottom")
label.pack()
#label.place(x = 100, y = 100)

window.mainloop()
# button = you click it, then it does stuff

from tkinter import *

count = 0

def click():
    global count
    print("You clicked the button!")
    count += 1
    print(count)

window = Tk()
window.title("Button")

photo = PhotoImage(file = "dices.png")

button = Button(window,text = "click me!",
                command = click,
                font = ("Commic Sans", 30),
                fg = "#00FF00",
                bg = "black",
                activeforeground="#00FF00",
                activebackground="black",
                state = ACTIVE,
                image = photo,
                compound = "bottom")

button.pack()

window.mainloop()

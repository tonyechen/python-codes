# radio button = similar to checkbox, but you can only selet on from a group
from tkinter import *

def order():
    if(x.get() == 0):
        print("You ordered pizza!")
    elif(x.get() == 1):
        print("You ordered a hamburger!")
    elif(x.get() == 2):
        print("You ordered a hotdog")
food = ["pizza", "hamburger", "hotdog"]

window = Tk()

pizzaImage = PhotoImage(file='pizza.png', width = 50, height = 50)
hamburgerImage = PhotoImage(file='hamburger.png', width = 50, height = 50)
hotdogImage = PhotoImage(file='hotdog.png', width = 50, height = 50)
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for i in range(len(food)):
    radiobutton1 = Radiobutton(window,
                              text = food[i], # adds text to radio buttons
                              variable = x, # groups radiobuttons together if they share the same variable
                              value = i, # assign each radiobutton a different value
                              padx = 100, # adds padding on x-axis
                              font = ("Impact", 50),
                              image = foodImages[i], # adds image to radiobutton
                              compound = 'left', # adds image # text
                              indicatoron = 0, # eliminate circle indicators
                              width=375,
                              command = order # set command of radio button to function
                              )
    radiobutton1.pack(anchor=W)

window.mainloop()
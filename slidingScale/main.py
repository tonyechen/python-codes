from tkinter import *

def submit():
    print("the tempterature is: " + str(scale.get()) + " degrees C")

window = Tk()
hotImage = PhotoImage()
coolImage = PhotoImage()

scale  = Scale(window,
               from_ = 100,
               to = 0,
               fg = "black",
               bg = "#add99a",
               font = ("Times New Roman", 20), # orientation of scale
               length = 600,
               orient = VERTICAL,
               tickinterval = 10, # adds numeric indicators for value
               #showvalue = 0, # hide current value
               resolution = 5, #increment of slider
               troughcolor='white',
               width = 8
               )

scale.set((scale['from'] - scale['to']) / 2 + scale['to']) # set scale position
scale.pack()

button = Button(window,
                text = 'submit',
                command = submit,
                fg = "white",
                bg = "#add99a",
                font = ("Impact", 20),
                width = scale['width'])

button.pack()
window.mainloop()
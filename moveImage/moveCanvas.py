from tkinter import *

def up(event):
    canvas.move(myimage, 0, -10)
def down(event):
    canvas.move(myimage, 0, 10)
def left(event):
    canvas.move(myimage, -10, 0)
def right(event):
    canvas.move(myimage, 10, 0)

window = Tk()

canvas = Canvas(window, width = 500, height = 500)
canvas.pack()

image= PhotoImage(file = "racecar.png")
myimage = canvas.create_image(0,0, image = image, anchor = NW)

window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<a>", left)
window.bind("<d>", right)

window.mainloop()
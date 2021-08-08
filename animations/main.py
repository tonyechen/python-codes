from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

xVelocity = 10
yVelocity = 10

window = Tk()

canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "light blue")
canvas.pack()

photo = PhotoImage(file = "racecar.png")
myImage = canvas.create_image(0, 0, image = photo, anchor = NW)

image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)
    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(myImage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
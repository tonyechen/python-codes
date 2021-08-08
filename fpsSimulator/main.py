from tkinter import *
import time
from Car import *
import threading

def start():
    start_button.config(state = DISABLED, disabledforeground = "red")

    car1.initiate(running)
    car2.initiate(running)
    car3.initiate(running)

def stop():
    car1.running = False
    car2.running = False
    car3.running = False
    car1.car.place(x = 0)
    car2.car.place(x = 0)
    car3.car.place(x = 0)

    start_button.config(state = ACTIVE)

window = Tk()
window.geometry("800x350")
window.config(bg = "light blue")

running = True

# create car objects
car1 = Car(window, 0, 0, 60, 300)
car2 = Car(window, 0, car1.y + car1.height, 30, 300)
car3 = Car(window, 0, car2.y + car2.height, 10, 300)

# stop button
stop_button = Button(window, text = "stop", font = ("Arial", 15), command = stop, padx = 30)
stop_button.pack(anchor = "w", side = BOTTOM)

# start button
start_button = Button(window, text = "start", font = ("Arial", 15), command = start, padx = 30)
start_button.pack(anchor = "w", side = BOTTOM)

entry = Entry(window, font = ("Arial", 20), width = 4)
entry.pack(anchor = "w", side = BOTTOM)

window.mainloop()
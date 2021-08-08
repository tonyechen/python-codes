from tkinter import *
import time
import threading

class Car():
    def __init__(self, window, x, y, fps, speed):
        # assign variables
        self.window = window
        self.fps = fps
        self.speed = speed
        self.x = x
        self.y = y

        # create image
        self.myimage = PhotoImage(file = "racecar.png")
        self.width = self.myimage.width()
        self.height = self.myimage.height()

        # create Label
        self.car = Label(self.window, image = self.myimage, bg = "light blue")
        self.label_fps = Label(self.window, text = "fps:", bg = "light green")
        self.entry_fps = Entry(self.window, width = 5)
        self.entry_fps.insert(0, self.fps)
        self.submit_button = Button(self.window, text = "+", command = self.update)
        self.display_fps = Label(window, text = "fps: " + str(self.fps))

        # place Label
        self.car.place(x = x, y = y)
        self.label_fps.place(x = x, y = y + self.height - 20)
        self.entry_fps.place(x = x + 25, y = y + self.height - 20)
        self.submit_button.place(x = x + 55, y = y + self.height - 20)
        self.display_fps.place(x = x + self.width, y = y + self.height / 2)

    def move(self, running):
        self.running = running
        t = time.time()
        count = 0
        while self.running and self.car.winfo_x() + self.width < 800:
            self.car.place(x = self.speed / self.fps * self.fps * (time.time() - t))
            time.sleep(1 / self.fps)
            self.window.update()
            count += 1
        print(count)
        print(time.time() - t)

    def initiate(self, running):
        a = threading.Thread(target=self.move, args=(running,))
        a.start()

    def update(self):
        self.fps = int(self.entry_fps.get())
        self.display_fps.config(text = "fps: " + str(self.fps))
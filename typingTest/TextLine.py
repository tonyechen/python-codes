from tkinter import *
import random

class TextLine():

    def __init__(self, window, width, color, font):
        # create instance variables
        self.window = window
        self.width = width
        self.color = color
        self.font = font
        self.words = []

        # create frame
        self.frame = Frame(self.window, width = self.width, height = 100, bg = self.color)
        self.frame.pack_propagate(False)
        self.frame.pack()

        # extract word list from words.text
        with open("words.txt") as file:
            words_list = file.read().split()

        # create labels inside frame + create the list of words
        count = 0
        length = 0
        while length < self.frame.winfo_width():
            label = Label(self.frame,
                          text = words_list[random.randint(0, len(words_list) - 1)],
                          font = self.font,
                          bg = self.color)
            space = Label(self.frame, bg = self.color, font = self.font, text = " ")

            self.words.append(label)

            label.pack(side = LEFT)
            space.pack(side = LEFT)

            self.window.update()
            length += label.winfo_width() + space.winfo_width()
            count += 1

        # remove and hide last word because tkinter widgets are weird
        self.words[len(self.words) - 1].config(bg = self.color, fg = self.color)
        self.words.pop(len(self.words) - 1)

        self.frame.config(height=self.words[0].winfo_height() + 10)

    def select(self, index):
        self.words[index].config(bg = "white")
        if index > 0:
            self.words[index - 1].config(bg = self.color)






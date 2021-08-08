# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello ", username)
    entry.config(state = DISABLED) #.config() can change the property of the object

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)


def show():
    if show_button['text'] == "show":
        entry.config(show = "")
        show_button.config(text = "hide")
    else:
        entry.config(show = "*")
        show_button.config(text = "show")


window = Tk()

entry = Entry(window,
              font = ("Arial", 20),
              fg = "#00FF00",
              bg = "black",
              show = "*" # replace each character, good for something like password
              )
entry.insert(2, "Spongebob")

entry.pack(side = LEFT)


submit_button = Button(window, text = "submit", command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "backspace", command = backspace)
backspace_button.pack(side = RIGHT)

show_button = Button(window, text = "show", command = show)
show_button.pack(side = RIGHT)
print(show_button.keys)
window.mainloop()



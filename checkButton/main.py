# Check Button

from tkinter import *

def display():
    if(x == 1):
        print("You agree!")
    else:
        print("You don't agree.")

window = Tk()

# It's not possible to hand over a regular Python variable to a widget through a variable or textvariable option.
# The only kinds of variables for which this works are variables that are subclassed from a class called Variable,
# defined in the Tkinter module. They are declared like this:
#x = StringVar() # Holds a string; default value ""
#x = IntVar() # Holds an integer; default value 0
#x = DoubleVar() # Holds a float; default value 0.0
#x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True

x = IntVar() # needed for a widget to pass value back to the variable

a = {"text": "I agree to something",
     "variable": x,
     "onvalue": 1, # what is going to be stored in the variable if it is toggled on, can be any value
     "offvalue": 0,# what is going to be stored in the variable if it is toggled off
     "command": display,
     "font": ('Arial', 20),
     "fg": '#00FF00',
     "bg": 'black',
     'activeforeground': '#00FF00',
     "activebackground": 'black',
     'padx': 25,
     'pady': 10}
check_button = Checkbutton(window, a)
check_button.pack()

print(a.items())

window.mainloop()
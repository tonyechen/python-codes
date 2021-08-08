# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():
    food = []
    print(type(listbox.curselection())) # curseselection returns a tuple of selected index
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
    #print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    try:
        # listbox.delete(listbox.curselection())
        for index in reversed(listbox.curselection()):
            listbox.delete(index)
    except Exception as e:
        print(e)
    else:
        listbox.config(height=listbox.size())


window = Tk()
window.geometry("500x500")

listbox = Listbox(window,
                  bg = '#f7ffde',
                  font = ("Constantia", 20),
                  width = 12,
                  selectmode = MULTIPLE)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, "salad")

listbox.config(height = listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text = "submit", command = submit)
submitButton.pack()

addButton = Button(window, text = "add", command = add)
addButton.pack()

deleteButton = Button(window, text = "delete", command = delete)
deleteButton.pack()


window.mainloop()
# **kwargs =    parameter that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    print(kwargs)
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello")
    for key,value in kwargs.items():
        print(value, end = " ")

hello(first="Bro", midle="Dude", last="Code")
# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments


def add(*stuff):  # doesn't have to be args, can be named anything else
    sum = 0
    print(stuff)
    stuff = list(stuff)
    print(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3))
# scope = The region that a variable is recognized
#          A variable is only available from inside the region it is created.
#          a global and locally scoped version of a variable can be created

name = "Bro" # global scope is available inside and outside functions

def display_name():
    name = "Code" # local scope is only available inside this function
    print(name)

display_name()
print(name)

# Local > Enclosing > Global > Built-in


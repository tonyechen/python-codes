# accepting user inputs
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age += 1
# input always record String data type, not numbers
# need to use data casting to convert value

print("Your name is " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + "cm tall")
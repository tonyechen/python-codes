# variable = a container for a value. Behaves as the value that it contains

# String variables
first_name = "Anthony"
last_name = "Chen"
full_name = first_name + " " + last_name
# print(type(name)) - type(variable) identify data type
print(full_name)

# Int variables - store whole integer numbers
age = 18
age = age + 1
# age += 1
print(age)
print(type(age))

print("Your age is: " + str(age))

# Float variables - store decimal numbers
height = 250.5
print("Your height is " + str(height) + "cm")
print(type(height))

# Boolean variables
human = False
print("Are you a human: " + str(human))
print(type(human))

#   str.format() =      oprtional method that gives users more control when displaying output

animal = "Cow"
item = "moon"

print("the " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(item, animal))
print("The {1} jumped over the {0}".format(item, animal)) # positional argument
print("The {animal} jumped over the {item}".format(item="moon", animal="cow")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Tony"
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {name:^10}. Nice to meet you".format(name="Tony"))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number)) #binary
print("The number pi is {:o}".format(number)) #Octave
print("The number pi is {:x}".format(number)) #Hex
print("The number pi is {:e}".format(number)) #scientific notation






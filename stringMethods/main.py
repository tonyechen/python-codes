# string methods

name = "hello world"

# len() = length of string
print(len(name))

# str.find() - find index of the first appearance of string
print(name.find("Bro"))

# str.capitalize() - only the first letter is capitalized
print(name.capitalize())

# str.upper() + str.Lower() - all cap or all lower-case
print(name.upper())
print(name.lower())

# str.isdigit() - true or false depending on if the string is a digit
print(name.isdigit())

# str.isalpha() - are these all alphabetical characters
print(name.isalpha())

# str.count("String") - count the number of appearance
print(name.count("o"))

# str.replace("String", "String") - replace string
print(name.replace("o", "x"))

print(name * 3) # print a string multiple times





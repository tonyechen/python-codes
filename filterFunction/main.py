# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Ayush",19),
           ("Connor",18),
           ("Seth", 17),
           ("Davis", 16),
           ("Audrey", 21),
           ("Chris", 20)]

age = lambda data:data[1] >= 18

drinking_buddies = filter(age, friends)

print(dict(list(drinking_buddies)))

for i in drinking_buddies:
    print(i)

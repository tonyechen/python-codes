# 2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

for i in range(0, len(food)):
    print(food[i])

food.sort()
print(food)
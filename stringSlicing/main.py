# slicing = create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]
# start = starting index, defult is 0
# stop = last index(exclusive), defult is end of string
# step = counting every "step" character, defult is 1
name = "Tony Chen"

first_name = name[:4]
last_name = name[5:]
funky_name = name[0:9:2]
reversed_name = name[::-1] # reverse the string

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com" # there are positive and negative index 0,1,2,3......... -3,-2,-1
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
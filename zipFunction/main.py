# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames, passwords)
print(list(users))

users = zip(usernames, passwords,login_date)
print(list(users))






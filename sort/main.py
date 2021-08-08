# sort() method      =  used with lists
# sort() function    =  used with iterables

students = list()
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort()
#students.sort(reverse = True) # reverse

for i in students:
    print(i)
#----------------------------------------------------------------------
print()

students1 = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
sorted_students = sorted(students, reverse = True)

for i in sorted_students:
    print(i)

print()
#----------------------------------------------------------------------

students2 = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

grade = lambda grades:grades[1]
students2.sort(key=grade)

print(students2)

print()
#----------------------------------------------------------------------
students3 = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

age1 = lambda ages:ages[2]

sorted_students3 = sorted(students3, key=age1)
print(sorted_students3)

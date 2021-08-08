# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#dishes.update(utensils)

#dinner_table = utensils.union(dishes)

#for x in dinner_table:
   #print(x)



print(dishes.difference(utensils))
print(utensils.intersection(dishes))

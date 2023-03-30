# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

data = {"vit" , "bit","pilani"}
print(data) # not in same order

# not allows duplicates -> print uniques
# true and 1 are considered same
d = {True,"mohit",1,3,2,1 , "mohit" , 2,3,True}
print(d) 

# possible to use the set() constructor to make a set.
names = set(("aby" , "binay" , 2 , False ,"hero"))
print(names)


# inserting
data.add("Manipal")
print(data)

#remove
data.remove("Manipal")
print(data)

# concate 2 sets
# argument of update can be anything - tuple , set , list etc
d.update(names)
print(d)


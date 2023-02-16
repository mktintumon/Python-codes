# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

myTuple = ("MCA" , "MSC" , "MBA" , "MCA")
print(myTuple)
print(len(myTuple)) # length

mixedTuple = ("Mohit" , 55 , True)
print(mixedTuple)
print(type(mixedTuple)) # <class 'tuple'>


# tuple with one item
myTup = ("apple",)
print(myTup)

#NOT a tuple----> string
my_tuple = ("apple")
print(my_tuple)



# UPDATE TUPLES

"""
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. 
You can convert the tuple into a list, change the list, 
and convert the list back into a tuple.
"""

myList = list(myTuple)
myList[3] = "BCA"
myTuple = tuple(myList)
print(myTuple)


# using asterisk notation
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # rest of them

# (green, *tropic, red) = fruits  ----> (green-apple) (all middle-yellow) (red-rasperry)

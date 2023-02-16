# Lists are used to store multiple items in a single variable.
# List items are ordered(not sorted), changeable, and allow duplicate values.

myList = ["MCA" , "MSC" , "MBA" , "MCA"]
print(myList)
print(len(myList)) # length

mixedList = ["Mohit" , 55 , True]
print(mixedList)
print(type(mixedList)) # <class 'list'>


# list() constructor
listConst = list(("mohit","govind",55,66))
print(listConst)


# OPERATIONS 

print(myList[2])  # from front
print(myList[-1]) # from back

if "MSC" in myList:
    print("available")
else:
    print("not available")


myList.insert(3,"BTECH")
myList.append("MTECH")
print(myList)

myList.extend(mixedList) # merge 2 lists or use (+)
print(myList)

myList.pop() # remove last
myList.pop(6)
del myList[6]
# del myList ---> deletes the list
# myList.clear() ---> clear list but not delete list
print(myList)


# LOOPS
for x in myList:
    print(x)

x = 0
while x < len(myList):
    print(myList[x])
    x += 1

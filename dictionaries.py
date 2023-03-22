'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
--> after python 3.7 its ordered , before it was unordered
'''

details = {
    "name": "mohit",
    "city": "patna",
    "courses": ["MCA" , "BSC" , 12 , 10],
    "pin" : 813101
}

print(details)
print(details['courses'])
print(details.keys())
print(details.values(),"\n")


# Duplicate values will overwrite existing values
data = {
    "name": "riya",
    "city": "vellore",
    "state": "delhi",
    "state": "kerala",
    "pin" : 632014
}

print(data)

# adding and deleting
# del data --> deletes complete dict
data['grade'] = 9.58
data.pop("city")
print(data,"\n")


# items() method will return each item in a dict, as tuples in a list.
print(data.items())


# update values
data.update({"pin":201122})
print(data)
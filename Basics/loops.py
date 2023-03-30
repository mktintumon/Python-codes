# while loop
i = 0
while i < 5:
 print(i , end=" ")
 i += 1

# break 
print("\n")
j = 1
while j < 6:
  print(j, end=" ")
  if j == 3:
    break
  j += 1


# while and ELSE 
print("\n")
k = 1
while k < 6:
  print(k, end=" ")
  k += 1
else:
  print("k is no longer less than 6")


# FOR loop
print("\n")
names = ["mohit","sobhik","sanket","govind","kishan","abhilash"]
for x in names:
    print(x, end=" ")


# range (0 to n-1)
print("\n")
for x in range(6):
    print(x, end=" ")

# increment ----> default increment is 1
print("\n")
for x in range(1,10,2):
    print(x, end=" ")


# for and else
print("\n")
for x in range(6):
  print(x)
else:
  print("Finally finished!")



# Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''
A person 'X' has a farm which is rectangular in shape. 'X' wants to plant 
coconut trees in the farm and he has heard that every tree has to be separated 
by 2 feet. He needs to calculate the number of plants to be purchased. 
Write a program to calculate the number of plants when provided with the length 
and breadth of the farm (in feet). The program should display the number of 
rows and columns along with the total number of plants required for the farm. 
For example, if the length and breadth of the farm is 9 feet * 4 feet 
then the farmer can plant trees in  positions 0, 2, 4, 6, 8 along the length 
and 0,2,4 along the breadth therefore number of trees to be purchased is 5*3 = 15.
'''

import math

length = float(input("Enter the length of the farm : "))
breadth = float(input("Enter the breadth of the farm : "))

rows = math.floor(length / 2) + 1
columns = math.floor(breadth / 2) + 1

total_trees = rows * columns

print("Number of rows :", columns)
print("Number of columns :", rows)
print("Total number of trees : ", total_trees)


# Write a python program that prints Pascal’s triangle

from math import factorial
 
n = int(input("Enter no. of rows: "))

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
 
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    print()


'''
n = int(input("Enter no. of rows: "))

def pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        row = []
        row.append(1) # adding 1 as first element

        # Calculating the rest elements in the row
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        
        if i > 0:
            row.append(1) # adding 1 as last element

        triangle.append(row)
    
    return triangle

print(pascals_triangle(n))
'''
'''
Given 'n' points, design a flowchart or an algorithm and write the Python code 
to determine the pair of points that are far from each other. Distance between 
two points (x1, y1) and (x2, y2) is determined using the formula√((x1-x2)^2+(y1-y2)^2 ). 
Write a function to determine distance between the two points. Consider only two 
decimal places of distance for comparison.
'''

''' 
ALGORITHM

--> Take the value of n
--> Taking n points as tuple(x,y)
--> Initialize a variable max_dist to 0 and 
    two empty variables as far_coord1 and far_coord2
--> For each pair of points (coord1, coord2) do the following:
        --> Calculate the distance between coordinates using the formula
        --> If the distance is greater than max_dist, 
            update max_dist , far_coord1, and far_coord2
--> Print the farthest pair of points far_coord1 and far_coord2
'''


import math

def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    dist = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
    return dist

def farthest_points(coordinates):
    n = len(coordinates)
    max_dist = 0
    far_coord1 = None
    far_coord2 = None
    
    for i in range(n):
        for j in range(i+1, n):
            coord1 = coordinates[i]
            coord2 = coordinates[j]
            dist = distance(coord1, coord2)
            if dist > max_dist:
                max_dist = dist
                far_coord1 = coord1
                far_coord2 = coord2
                
    return far_coord1, far_coord2 , max_dist

# given coordinates
coordinates = [(-1,3), (4,4), (6,1), (6,3)]

far_coord1, far_coord2 , dist = farthest_points(coordinates)

print("Given coordinates -> " , coordinates)
print(f"The farthest points are {far_coord1} and {far_coord2} with distance {dist}")


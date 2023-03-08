'''
Students in a class are appreciated based on the following factors
Number of 'S' grade >= 3
Attendance >= 90
Participation in sports activity in a semester >= 2
Appreciation is given as follows: 
(i) 'Excellent' if all three conditions are met 
(ii)'Very Good' if conditions (i) and (ii) are met 
(iii)'Good' if conditions (i) and (iii) are met 
Given the Number of 'S' grades, Attendance and Participation in sports activity in a semester, write the python code to output the appreciation for the student. Check boundary conditions and print 'Invalid input' for wrong input.

'''

# Taking input values for grades , attendance and participation
grades = int(input("Enter the number of 'S' grades: "))
attendance = float(input("Enter the attendance percentage: "))
participation = int(input("Enter the no. of Participation in sports activity: "))

# Checking the boundary conditions and given conditions
if grades < 0 or attendance < 0 or participation < 0:
    print("Invalid input")
else:
    if grades >= 3 and attendance >= 90 and participation >= 2:
        print("Excellent")
    elif grades >= 3 and attendance >= 90:
        print("Very Good")
    elif grades >= 3 and participation >= 2:
        print("Good")
    else:
        print("Sorry !!! No Appreciation")

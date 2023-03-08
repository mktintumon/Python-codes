'''
VIT follows relative grading based on the class average to grade the performance 
of students in various examinations. Write a program that accepts the marks secured 
by a student for a given subject along with the average marks of the respective class. 
Then display the grade he has secured, based on the following instructions.

a) Grading is done based on the deviation from class average. 
b) If the deviation from class average of the student’s mark is greater than or equal to 20, 
   the student has scored S grade
c) If the deviation from class average of the student’s mark is greater than or equal to 10, 
   the student has scored A grade
d) If the deviation from class average of the student’s mark is within the range of -5 to + 5, 
   the student has scored B grade
e) If the deviation from class average of the student’s mark is less than or equal to 10, 
   the student has scored C grade
f) If the deviation from class average of the student’s mark is less than or equal to 15, 
   the student has scored D grade
g) If the deviation from class average of the student’s mark is less than 20, 
   the student has scored F grade
'''

marks = float(input("Enter the marks of student: "))
class_avg = float(input("Enter the class average: "))

deviation = abs(marks - class_avg)

# Computing grades
if deviation >= 20:
    grade = "S"
elif deviation >= 10:
    grade = "A"
elif deviation >= -5 and deviation <= 5:
    grade = "B"
elif deviation <= 10:
    grade = "C"
elif deviation <= 15:
    grade = "D"
else:
    grade = "F"

print("The student has secured", grade, "grade.")

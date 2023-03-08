'''
A company wants its employees to work for 'X' hours on average per day in a week (Monday to Friday).  
Given the number of hours worked by an employee on each day of a week, design a flowchart and write 
a Python code to compute the average number of hours worked by the employee. Number of hours worked 
can be floating point values. For example, 7 hours 30 minutes is entered as 7.5 hours
'''

# Taking user input for 5 days
workingHours = []
for i in range(5):
    # input expected at most 1 arguments
    workingHours.append(float(input(f"Enter number of hours worked on day {i+1}: ")))

avgWorkingHour = sum(workingHours) / 5

# checking --> target satisfied or not
print("\n")
target = float(input("Enter target no. of hours to work per day: "))

print("\n")
if avgWorkingHour >= target:
    print("Employee worked according to target hours of" , target)
else:
    print("Employee DID NOT worked according to target hours of" , target)


print("Total hours worked:", sum(workingHours))
print("Average hours worked per day:", avgWorkingHour)

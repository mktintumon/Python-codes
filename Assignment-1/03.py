'''
A man engaged 'n' labourers to make ’t’ toys in ’d’ days. 
Assume that all men work with same speed and efficiency. 
After 'd1' days, he found that only 't1' toys were made. 
Design an algorithm and write a Python code to determine the number of 
additional men to be employed to complete the task in time. 
For example, if n is 10, t is 320, d is 5, d1 is 3, and t1 is 120 
then the number of additional men to be employed is 12. 
Assume that the speed of making toys is uniform for all men.
'''

# Get the necessary inputs from the user
n = int(input("Enter the number of labourers: "))
t = int(input("Enter the total number of toys to be made: "))
d = int(input("Enter the number of days to complete the task: "))
d1 = int(input("Enter the number of days after which progress was checked: "))
t1 = int(input("Enter the number of toys made after d1 days: "))

''' 
LOGIC
eq_1 = (n*d1) / t1
eq_2 = (n+x)*(d-d1) / (t-t1)

eq_1 == eq_2 --> find x
'''

days_left = d-d1
toys_left = t-t1

additional_men_needed = ((n * d1 * toys_left) / (t1 * days_left) ) - n

print("\n")
print("Additional men needed : " , int(additional_men_needed))



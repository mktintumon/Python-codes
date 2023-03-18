'''
A bag contains a total of 'T' nuts and bolts. Out of which there are 'N' nuts. 
In a quality check, x% of the nuts and y% of bolts in the bag were found to be 
defective. Design an algorithm and write a Python code to determine the 
percentage of non-defective items in the bag. For example if T is 200, N is 150, 
x is 50 and y is 20 then the percentage of non-defective items in bag is 57.5. 
Round the answer to two decimal places using format function.
'''

total = int(input("Enter total items in Bag : "))
nuts = int(input("Enter count of nuts : "))
x = int(input("Percent of defective nuts : "))
y = int(input("Percent of defective bolts : "))

bolts = total - nuts

non_defect_nuts = nuts - ((nuts * x) / 100)
non_defect_bolt = bolts - ((bolts * y) / 100)

total_non_defected = non_defect_bolt + non_defect_nuts

percent_non_defected = (total_non_defected / total) * 100

# format function
print("Percentage of non-defective " , format(percent_non_defected , ".2f"))
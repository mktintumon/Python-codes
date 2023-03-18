'''
A finance consultant decides to create an application for the public 
who wants to decide on the type of investment they can make. He needs 
an application, which when given with the initial amount, no of years 
of investment ‘n’ and the expected amount after ‘n’ years, should tell 
the  rate of interest based on which the customers will choose their 
investments. Assume that the application works with only simple interest 
calculation. Can you code for Raman? 
Use Rate of interest = ((expected amount-initial amount) / (initial amount * no of years))*100.
'''

initial_amount = float(input('Initial Amount : '))
expected_amount = float(input('Expected Amount : '))
years = int(input('After Year : '))

rate = ((expected_amount - initial_amount) / (initial_amount * years)) * 100

print('Required Rate of interest : ' , rate , '%')
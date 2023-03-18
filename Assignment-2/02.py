'''
Calculate the number of birthdays celebrated by Mr.X. If Mr.X was born 
on 29th February of a leap year then he celebrates birthday only in leap 
years. Given the date of birth of Mr.X and the current year, design an 
algorithm and write the Python code to determine the number of birthdays 
celebrated by Mr.X. A year is a leap year if it is divisible by 4 and not 
divisible by 100 or when the year is divisible by 400. For example, year 
1996 and 2000 are leap years whereas 1900 is not a leap year. 
Assume that the current day and month is greater than day and month of birthday.
'''

'''
ALGORITHM
--> Take input from the user for Mr.X's birth year, birth month, and birth date.
--> Take input from the user for the current year, current month, and current date.
--> Calculate the number of leap years between the birth year and the current year. 
    To do this, we will loop through all the years between the birth year and the current 
    year and check if each year is a leap year. If it is, we will increment a counter.
--> If the birth month and date are after February 29th, we need to subtract 1 from the 
    total number of birthdays celebrated.
--> Print the total number of birthdays celebrated by Mr.X
'''

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_date = int(input("Enter birth date: "))

curr_year = int(input("Enter current year: "))
curr_month = int(input("Enter current month: "))
curr_date = int(input("Enter current date: "))

leap_count = 0
for year in range(birth_year, curr_year + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_count += 1

if (birth_month > 2) or (birth_month == 2 and birth_date > 29):
    leap_count -= 1

print("Total birthdays celebrated by Mr.X:", leap_count)

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

def birthday(day,month,birth_year,current_year):
    if(current_year > birth_year):
        diff = current_year - birth_year
        if(day == 29 and month == 2):
            x = diff // 4
        else:
            x = diff 
        print(x)
    else:
        print('Wrong entry')

birthday(29 , 2, 1960 , 2010)
birthday(31 , 1, 1975 , 2100)
birthday(3 , 2 , 1960 , 1950)
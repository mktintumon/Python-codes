'''
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the
username and company name of a given email address. Both user names and
company names are composed of letters only.
'''


import re

email = input("Enter an email address: ")

# Using regex
match = re.match('^(\w+)@(\w+)\.com$', email)

# Check if the match is successful
if match:
    # Extract the user name and company name
    username = match.group(1)
    companyname = match.group(2)
    
    print("User Name: ", username)
    print("Company Name: ", companyname)
else:
    print("Invalid email address.")

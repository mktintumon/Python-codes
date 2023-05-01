'''
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords that match the
criteria are to be printed, each separated by a comma
Example : ABd1234@1,a F1#,2w3E*,2We3345,Mohit@12345

'''

import re

def validate_password(password):
    # password conditions
    if re.search('[a-z]', password) and \
        re.search('[0-9]', password) and \
        re.search('[A-Z]', password) and \
        re.search('[$#@]', password) and \
        len(password) >= 6 and len(password) <= 12:
        return True
    else:
        return False

# Input of comma separated passwords
passwords = input("Enter comma separated passwords: ")

password_list = passwords.split(',')

# To store valid passwords
valid_passwords = []

for password in password_list:
    password = password.strip()
    if validate_password(password):
        valid_passwords.append(password)

# Print the valid passwords separated by a comma
print(','.join(valid_passwords))

'''
Write a code in python for validating your VIT email address in form by using
string methods such as indexOf() and lastIndexOf() method for @symbol,
dot symbol, and space symbol.
'''


email = input("Enter your VIT email address: ")

# Checking space
if " " in email:
    print("Invalid email address...Enter without spaces")
else:
    # Check the position of the '@' symbol
    at_index = email.find('@')
    if at_index == -1:
        print("Invalid email address. Email should contain '@' symbol.")
    else:
        # Check the position of the last '.' symbol
        last_dot_index = email.rfind('.')
        if last_dot_index == -1:
            print("Invalid email address. Email should contain '.' symbol.")
        else:
            # Check if the last '.' symbol appears after the '@' symbol
            if last_dot_index < at_index:
                print("Invalid email address. '.' symbol should appear after '@' symbol.")
            else:
                print("Valid email address.")

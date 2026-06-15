# Ask the user for a password
password = input("Enter a password: ")

# Check 1: Length of password
length_check = len(password) >= 8

# Check 2: At least one digit
digit_check = False
for char in password:        # loop through each character
    if char.isdigit():       # check if it's a number
        digit_check = True
        break                # stop once we find one

# Check 3: At least one uppercase letter
uppercase_check = False
for char in password:        # loop through each character
    if char.isupper():       # check if it's uppercase
        uppercase_check = True
        break

# Final decision
if length_check and digit_check and uppercase_check:
    print("Password is Strong")
else:
    print("Password is Weak")



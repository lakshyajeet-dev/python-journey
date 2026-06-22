# Ask the user for their age. Print "You are an adult" if age is 18 or above, else print "You are a minor.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   

# Ask the user for their marks (out of 100). Print their grade:

# 90 and above → "Grade A"
# 75 and above → "Grade B"
# 60 and above → "Grade C"
# 40 and above → "Grade D"
marks = int(input("Enter your marks (out of 100): "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")              

# Ask the user for their age and whether they have a driving license (yes/no). Print:

# If age >= 18 and has license → "You can drive"
# If age >= 18 but no license → "You need a license to drive"
# If age < 18 → "You are too young to drive"      

age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ")
if age>= 18:
    if license.lower() == "yes":
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")     

# Build a simple login system:

# Store a correct username and password in your code
# Ask the user to enter username and password
# If both match → "Login successful"
# If username matches but password doesn't → "Wrong password"
# If username doesn't match → "User not found"       
correct_username = "admin"
correct_password = "12345"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("User not found.")        
# Ask the user for their name, age, and CGPA
# Store them in proper types — name as string, age as integer, CGPA as float
# Print this output using an f-string:

# Hello Lakshyajeet! You are 21 years old and your CGPA is 7.5

name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your cgpa: "))
print(f"Hello {name}! You are {age} years old and your cgpa is {cgpa}")

# Ask the user to enter two numbers. Add them, subtract them, multiply them, and divide them. Print all four results like this:
# Addition: 30
# Subtraction: 10
# Multiplication: 200
# Division: 2.0

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# Ask the user for their birth year. Calculate their age by subtracting from 2026. Print:
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print(f"You are {age} years old.")
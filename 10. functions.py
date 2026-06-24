# Write a function called greet_user that takes a name as input and prints "Hello [name]! Welcome." Call it 3 times with different names.
def greet_user(name):
     print(f"Hello {name}! Welcome.")
greet_user("Lakshyajeet")
greet_user("Shagun")
greet_user("Ansh")

# Write a function called calculate_area that takes length and width as parameters and returns the area. Print the result outside the function.
def calculate_area(length, width):
     return(length * width)
area = calculate_area(10, 5)
print(f"The area is {area}")

# Write a function called is_even that takes a number and returns True if even, False if odd. Use it to print whether 5 numbers are even or odd.
def is_even(number):
     return number % 2 == 0
numbers = [2 , 7 ,10 , 20 , 30]
for num in numbers:
     if is_even(num):
          print(f"{num} is even")
     else:
          print(f"{num} is odd")

# Write a function called calculate_grade that takes marks as a parameter and returns the grade (use the same A/B/C/D/Fail logic from before). Test it with at least 4 different marks.          
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
print(f"Marks: 95 → Grade:", calculate_grade(95)) 
print("Marks: 80 → Grade:", calculate_grade(80))
print("Marks: 65 → Grade:", calculate_grade(65))
print("Marks: 30 → Grade:", calculate_grade(30))  

# Write a function called calculator that takes two numbers and an operator (+, -, *, /) as parameters. Perform the correct operation and return the result. Handle division by zero — if second number is 0 and operator is /, return "Cannot divide by zero".
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

# Testing the function
print(calculator(10, 5, "+"))   # 15
print(calculator(10, 5, "-"))   # 5
print(calculator(10, 5, "*"))   # 50
print(calculator(10, 0, "/"))   # Cannot divide by zero


# Write a function called find_largest that takes 3 numbers using *args and returns the largest one. Don't use Python's built-in max() function — figure out the logic yourself.
def find_largest(*args):
    # Assume the first number is the largest
    largest = args[0]
    
    # Compare each number with the current largest
    for num in args:
        if num > largest:
            largest = num
    
    return largest

# Test the function with 3 numbers
print("Largest is:", find_largest(10, 25, 7))
print("Largest is:", find_largest(100, 50, 75))
print("Largest is:", find_largest(3, 3, 3))
print("Largest is:", find_largest(-5, -2, -10))

      
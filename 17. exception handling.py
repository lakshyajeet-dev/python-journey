# Task 1 — Basic exception handling
# Ask the user to enter two numbers and divide them. Handle:

# ValueError — if user types text instead of numbers
# ZeroDivisionError — if second number is 0
# Print a success message if no error occurs using else
# Always print "Program ended." using finally
try:
    # Ask user for input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1/num2
except ValueError:
    print("Error: Please enter valid number.:")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Program ended.")

# Task 2 — File exception
# Ask the user to enter a filename. Try to open and read it. Handle FileNotFoundError with a clean message. If file exists, print its contents.    
try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        contents = file.read()
        print("File contents:\n")
        print(contents)
except FileNotFoundError:
       print("Error: The file you entered was not found.")

# Task 3 — Custom exception with raise
# Write a function called validate_age that:

# Takes age as input
# Raises ValueError if age is below 0 or above 150 with a proper message
# Returns the age if valid
# Test it with ages: -5, 200, 25       
def validate_age(age):
    # Check for invalid age values
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 150:
        raise ValueError("Age cannot be greater than 150.")
    else:
        return age

# Testing the function
test_ages = [-5, 200, 25]

for age in test_ages:
    try:
        valid_age = validate_age(age)
        print(f"Valid age entered: {valid_age}")
    except ValueError as e:
        print(f"Error: {e}")


# Task 4 — Real world input validation
# Write a function called get_valid_number that:

# Keeps asking the user for a number until they enter a valid one
# Uses a while loop + try/except
# Returns the valid number once entered
def get_valid_num():
    while True:
        try:
            num = int(input("Enter a valid number: "))
            return num         # If successful, return the number and exit the loop
        except ValueError:
            print("Error: Please enter a valid number.")
valid_num = get_valid_num()
print(f"You entered a valid number: {valid_num}")          


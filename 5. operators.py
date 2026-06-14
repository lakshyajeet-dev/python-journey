# 1. Take two numbers as input from the user. Perform all 7 arithmetic operations and print results clearly with labels.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2
print("\n--- Arithmetic Results ---")
print(f"1. Addition (+):        {num1} + {num2} = {addition}")
print(f"2. Subtraction (-):    {num1} - {num2} = {subtraction}")
print(f"3. Multiplication (*):  {num1} * {num2} = {multiplication}")
print(f"4. Division (/):        {num1} / {num2} = {division}")
print(f"5. Modulus (%):         {num1} % {num2} = {modulus}")
print(f"6. Exponentiation (**): {num1} ** {num2} = {exponentiation}")
print(f"7. Floor Division (//): {num1} // {num2} = {floor_division}")

# 2. Take a number as input. Check if it is even or odd using % and print the result like:

# 8 is even
# 7 is odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 3. Take a student's marks as input (out of 100). Using only comparison operators and print statements check and print:
# Is the student passing? (passing mark is 40)
# Did the student score above 75?
# Did the student score exactly 100? 

marks = float(input("Enter the student's marks (out of 100): "))
if marks >= 40:
    print("The student is passing.")
else:
    print("The student failed.")

if marks > 75:
    print("The student scored above 75.")
else:
    print("The student did not score above 75.")

if marks == 100:
    print("The student scored exactly 100.")
else:
    print("The student did not score exactly 100.")

# 4. Take age and country code as input. Using logical operators check:

# Is the person eligible to vote in India? (age >= 18 and country == "IN")
# Print True or False 
# Take age and country code as input
age = int(input("Enter age: "))
country_code = input("Enter country code (e.g., IN, US): ")
is_eligible = (age >= 18) and (country_code == "IN" or country_code == "in")
print(is_eligible)

# 5. Start with a score = 0. Add 10 three times and subtract 5 once using assignment operators only. Print the final score.
score = 0
score += 10
score += 10
score += 10
score -= 5
print(score)
# Store the string "100" in a variable called marks. Convert it to an integer and add 20 to it. Print the result
marks = "100"
marks = int(marks)
result = marks + 20
print(result)

# Store the float 9.8 in a variable called gpa. Convert it to an integer and print it. Also print what value was lost.
gpa = 9.8
gpa = int(gpa)
print(gpa)
print(gpa - 9.8)

# Store the integer 0 and the integer 5 in two variables. Convert both to bool and print them. Write a comment explaining why each result is what it is.
num1 = 0
num2 = 5
bool1 = bool(num1)
bool2 = bool(num2)
print(bool1)  # False, because 0 is considered falsy in Python
print(bool2)  # True, because any non-zero number is considered truthy in 

# Take this string "3.14" — convert it to a float, then to an int, then print all three versions with their types.
pi = "3.14"
print(pi, type(pi))

# Convert to float
pifloat = float(pi)
print(pifloat, type(pifloat))

# Convert to int
piint = int(pifloat)
print(piint, type(piint))



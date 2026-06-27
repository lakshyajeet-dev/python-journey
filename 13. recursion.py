# Write a recursive function called countdown that counts down from n to 1 and then prints "Blast off!"
def countdown(n):
    if n == 0:   # base case
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)   # recursive case

countdown(5)

# Write a recursive function called factorial that calculates the factorial of a number. Test with 5 and 10.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print("Factorial of 5:", factorial(5))   # 120
print("Factorial of 10:", factorial(10))

# Write a recursive function called sum_list that takes a list of numbers and returns their sum — without using Python's built-in sum() function.
# Test with: [1, 2, 3, 4, 5]
def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])
test_list = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(test_list)) 

# Write a recursive function called fibonacci that returns the nth Fibonacci number.

# Test with: n = 0, 1, 5, 7, 10
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)   # recursive case
print("Fibonacci(0):", fibonacci(0))   # 0
print("Fibonacci(1):", fibonacci(1))   # 1
print("Fibonacci(5):", fibonacci(5))   # 5
print("Fibonacci(7):", fibonacci(7))   # 13
print("Fibonacci(10):", fibonacci(10))
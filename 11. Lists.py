# Create a list of 5 of your favourite movies. Print the first, last, and middle one using indexing.
favorite_movies = ["HEAT" , "GODFATHER" , "GOODFELLAS" , "MARTIAN" , "CASINO"]
print(favorite_movies[0])
print(favorite_movies[4])
print(favorite_movies[2])

# Take a list of numbers: [5, 3, 8, 1, 9, 2, 7]

# Sort it in ascending order
# Sort it in descending order
# Find the sum, min, and max without loops
numbers = [5, 3, 8, 1, 9, 2, 7]
ascending = sorted(numbers)
print("Ascending:", ascending)
descending = sorted(numbers, reverse=True)
print("Descending:", descending)
total = sum(numbers)
print("Sum:", total)
minimum = min(numbers)
print("Minimum:", minimum)
maximum = max(numbers)
print("Max:", maximum)

# Start with an empty list. Ask the user to enter 5 names one by one using a loop and add each to the list. Then print the full list, the total count, and the names in sorted order.
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
print("Full List:", names)    
print("Total count:", len(names))
print("Sorted list:", sorted(names))

# Given this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension create two new lists:

# One with only even numbers
# One with the square of every number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)
squares = [n**2 for n in numbers]
print("Squares:", squares)

# Write a function called remove_duplicates that takes a list and returns a new list with duplicates removed. Don't use any built-in duplicate removal — think through the logic yourself.
# Test with: [1, 2, 2, 3, 4, 4, 4, 5]
def remove_duplicates(lst):
    # Step 1: Create an empty list to store unique items
    unique_list = []
    
    # Step 2: Loop through each item in the original list
    for item in lst:
        # Step 3: Check if the item is not already in unique_list
        if item not in unique_list:
            # Step 4: Add the item if it's new
            unique_list.append(item)
    
    # Step 5: Return the list with duplicates removed
    return unique_list
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
result = remove_duplicates(numbers)
print("Original:", numbers)
print("Without duplicates:", result)



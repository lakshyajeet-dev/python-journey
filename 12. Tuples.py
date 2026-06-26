# Create a tuple storing your personal info — name, age, city, course. Unpack it into separate variables and print each one using an f-string.
info = ("Lakshyajeet", 21 , "Kota", "Computer Science")
name , age , city , course = info
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I am studying {course}.")

# Create a tuple of 7 colors. Print the first 3, last 2, and every alternate color using slicing.
colors = ("Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink")
print("First 3 colors: ", colors[:3])
print("Last 2 colors: ", colors[-2:])
print("Alternate color: ", colors[::2])

# Write a function called min_max that takes a tuple of numbers and returns both the minimum and maximum as a tuple. Unpack the result when calling the function.
# Test with: (5, 3, 8, 1, 9, 2, 7)
def min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum , maximum)
data = (5, 3, 8, 1, 9, 2, 7)
low , high = min_max(data)
print(f"The minimum is {low}")
print(f"The maximum is {high}")

# Create a tuple of 5 numbers with some duplicates. Convert it to a list, remove all duplicates using your remove_duplicates function from the lists topic, sort it, then convert it back to a tuple and print it.
def remove_duplicates(lst): 
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list        
numbers_tuple = (4, 2, 7, 2, 4) 
numbers_list = list(numbers_tuple)
no_duplicates = remove_duplicates(numbers_list)
sorted_list = sorted(no_duplicates)
final_tuple = tuple(sorted_list)
print("Original tuple:", numbers_tuple)
print("After removing duplicates and sorting:", final_tuple)   


# Create a tuple called student_records containing 3 tuples inside it — each inner tuple has a student's name and marks:
# python(("Lakshyajeet", 85), ("Shagun", 92), ("Ansh", 78))
# Loop through it and print each student's name, marks, and grade using your calculate_grade function from the functions topic.
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return"D"
    else:
        return "Fail"
student_records = (
    ("Lakshyajeet", 85),
    ("Shagun", 92),
    ("Ansh", 78)
)
for name, marks in student_records:
    grade = calculate_grade(marks)
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

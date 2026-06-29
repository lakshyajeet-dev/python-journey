# Create a dictionary of your own profile — name, age, city, course, cgpa, is_employed. Print each key and value using a loop.
my_profile = {
    "name": "Lakshyajeet Rathod",
    "age": 21,
    "city": "Kota",
    "course": "Computer Science",
    "cgpa": 8.5,
    "is_employed": False
}
for key, value in my_profile.items():
    print(f"{key}: {value}")


# Start with this dictionary:
# pythonproducts = {
#     "laptop": 75000,
#     "phone": 25000,
#     "tablet": 35000,
#     "headphones": 5000
# }

# Add a new product "smartwatch" with price 15000
# Update the price of "phone" to 28000
# Remove "tablet"
# Print all product names
# Print all prices
# Print the most expensive product name and its price
pythonproducts = {
    "laptop": 75000,
    "phone": 25000,
    "tablet": 35000,
    "headphones": 5000
}
pythonproducts["smartwatch"] = 15000
pythonproducts["phone"] = 28000
del pythonproducts["tablet"]
print("Product names: ", list(pythonproducts.keys()))
print("Prices:", list(pythonproducts.values()))
max_product = max(pythonproducts, key=pythonproducts.get)
print(f"Most expensive: {max_product} → {pythonproducts[max_product]}")

# Write a function called word_count that takes a sentence as input and returns a dictionary where each key is a word and each value is how many times that word appears.
# Test with: "the cat sat on the mat the cat"
# Expected output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
def word_count(sentence):
    words = sentence.split()
    count_dict = {}
    for word in words:
        if word in count_dict:          # if word already exists
            count_dict[word] += 1       # increase its count
        else:                           # if word is new
            count_dict[word] = 1        # start count at 1
    return count_dict

print(word_count("the cat sat on the mat the cat"))


# Create a nested dictionary for 3 students — each student has a name, marks list (3 subjects), and city. Write a function that loops through all students and prints:

# Their name
# Their average marks
# Their grade based on average (use your calculate_grade function)
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"
students = {
    "student1": {"name": "Lakshyajeet", "marks": [85, 90, 88], "city": "Kota"},
    "student2": {"name": "Shagun", "marks":  [92, 95, 89], "city": "Jaipur"},
    "student3": {"name": "Ansh", "marks": [78, 65, 80], "city": "Kota"}
}    
for sid, info in students.items():
    name = info["name"]                          # get student name
    avg = sum(info["marks"]) / len(info["marks"]) # calculate average
    grade = calculate_grade(avg)                 # get grade
    print(f"Name: {name}, Average: {avg:.2f}, Grade: {grade}")


# Write a function called flip_dict that takes a dictionary and returns a new dictionary with keys and values swapped.
# Test with: {"a": 1, "b": 2, "c": 3}

# Expected output: {1: "a", 2: "b", 3: "c"}
def flip_dict(d):
    return {value: key for key, value in d.items()}

print(flip_dict({"a": 1, "b": 2, "c": 3}))

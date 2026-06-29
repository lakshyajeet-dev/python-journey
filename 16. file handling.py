# Task 1 — Basic write and read

# Write these 3 lines to a file called my_notes.txt:

# Name: Lakshyajeet
# City: Kota
# Goal: Python Developer

# Then read the file and print each line cleanly (without extra blank lines)
with open("my notes.txt", "w") as file:
    file.write("Name: Lakshyajeet\n")
    file.write("City: Kota\n")
    file.write("Goal: Python Developer\n")
with open("my notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Task 2 — Append

# Open my_notes.txt and append this line at the end:

# Status: Learning Python 
    
# Step 1: Append the new line
with open("my notes.txt", "a") as file:
    file.write("Status: Learning Python\n")

# Step 2: Read the file back and print each line
with open("my notes.txt", "r") as file:
    for line in file:
        print(line.strip())



# Task 3 — JSON write and read

# Create a dictionary with details of 2 students (name, age, city)
# Save it to a file called students.json
# Read it back and print each student's details using a loop
import json
import os

filename = "students.json"

# --- Step 1: Create dictionary with 2 students ---
students = {
    "student1": {"name": "Lakshyajeet", "age": 21, "city": "Kota"},
    "student2": {"name": "Shagun", "age": 22, "city": "Jaipur"}
}

# --- Step 2: Save dictionary to students.json ---
with open(filename, "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully.")

# --- Step 3: Read dictionary back safely ---
if os.path.exists(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)

    print("\nLoaded data from file:")
    for sid, info in loaded_data.items():
        print(f"{sid} -> Name: {info['name']}, Age: {info['age']}, City: {info['city']}")
else:
    print("File not found!")





# Task 4 — Practical

# Write a program that asks the user to enter their name and a note
# Save both to a JSON file called user_note.json
# Read it back and print: "[name] wrote: [note]"
import json
import os

filename = "user_note.json"

# --- Step 1: Ask user for input ---
name = input("Enter your name: ")
note = input("Enter your note: ")

# --- Step 2: Save both to user_note.json ---
user_data = {"name": name, "note": note}

with open(filename, "w") as file:
    json.dump(user_data, file, indent=4)

print("Note saved successfully.")

# --- Step 3: Read data back safely ---
if os.path.exists(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)
    print(f"{loaded_data['name']} wrote: {loaded_data['note']}")
else:
    print("No notes found yet!")

# Part A — Indexing & Slicing
# Given:
# pythontext = "Programming"

# Print the first character
# Print the last character using negative indexing
# Print the first 4 characters using slicing
# Print the last 4 characters using slicing
# Print the string reversed using slicing
# Print every alternate character

text = "Programming"
print(text[0]) # First Character
print(text[-1]) # Lat character using negative slicing
print(text[0:4]) # first 4 characters using slicing
print(text[-4:]) # last 4 characters
print(text[::-1]) # string reversed
print(text[::2]) # every alternate character


# 1. Take user's first name and last name as separate inputs.
#    Concatenate them with a space and print the full name.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# 2. Print a separator line of 30 dashes using repetition.
print("-" * 30)

# 3. Take a sentence as input. Check and print whether the word "Python" exists in it.
sentence = input("Enter a sentence: ")
print("Python" in sentence)


# 1. Take a sentence as input with extra spaces at the start/end
#    (user types "   hello world   "). Strip it and print the clean version.
sentence_with_spaces = input("Enter a sentence with spaces")
clean_sentence = sentence_with_spaces.strip()
print("Cleaned Sentence:", clean_sentence)

# 2. Take an email as input. Print it in lowercase 
#    (emails should always be normalized to lowercase).
email = input("Enter your email: ")
normalized_email = email.lower()
print("Normalized Email:", normalized_email)

# 3. Take a sentence as input. Count how many times the letter "a" appears
#    (case-insensitive — count both "a" and "A").
count_sentence = input("Enter a sentence to count 'a': " )
lower_sentence = count_sentence.lower()
a_count = lower_sentence.count("a")
print("Number of 'a' or 'A' letters:", a_count)


# 4. Take a full name as input.
#    Split it into first and last name and print them separately
# Take full name as input
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Extract first and last name
first_name = name_parts[0]
last_name = name_parts[-1]

# Check if there are middle names
if len(name_parts) > 2:
    middle_names = " ".join(name_parts[1:-1])
    print("First Name:", first_name)
    print("Middle Name(s):", middle_names)
    print("Last Name:", last_name)
else:
    print("First Name:", first_name)
    print("Last Name:", last_name)

# 5. Take a sentence as input. Replace the word "good" with "great" and print the result.
sentence = input("Enter a sentence: ")
modified_sentence = sentence.replace("good", "great")
print("Modified Sentence: ", modified_sentence)
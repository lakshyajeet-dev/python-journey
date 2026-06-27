# Create two sets — one with your favourite sports, one with your friend's favourite sports. Print:

# All sports both of you like combined
# Sports both of you have in common
# Sports only you like
my_sports = {"Cricket", "Football", "Badminton", "Tennis"}
friend_sports = {"Football", "Basketball", "Tennis", "Hockey"}
all_sports = my_sports | friend_sports  # union
common_sports = my_sports & friend_sports  # intersection
my_unique_sports = my_sports - friend_sports  # difference
print("All sports combined:", all_sports)
print("Common sports:", common_sports)
print("Only my sports:", my_unique_sports)

# Take this list: [1, 1, 2, 3, 3, 4, 5, 5, 5]

# Use a set to remove duplicates and print the unique values.
numbers = [1, 1, 2, 3, 3, 4, 5, 5, 5]
unique_numbers = set(numbers)
print("Unique values:" , unique_numbers)

# Take two sentences as input from the user. Find and print the common words between them using sets.
# Hint for Task 3 — split both sentences into words using .split(), convert to sets, then find intersection.
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")
words1 = set(sentence1.split())
words2 = set(sentence2.split())
common_words = words1 & words2   # intersection
print("Common words:", common_words)
# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# Print all even numbers from 1 to 20 using range() with a step.
for i in range(2,21,2):
    print(i)


# Ask the user to enter a word. Loop through each character and print it on 
# separate line. Also count how many characters the word has (without using len()).
word = input("Enter a word: ") 
count = 0
for char in word:
    print(char)
    count +=1
print("The word has", count, "characters.")   


# Print this pattern using nested loops:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()


# Ask the user to enter 5 numbers one by one using a loop. Add them all up and print the total at the end. (Don't store all 5 — just keep a running total.)
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    total += num
    print("Running total:", total)
print("Final total:", total)


# Loop through numbers 1 to 20. If the number is divisible by both 3 and 5, print "FizzBuzz". If only by 3, print "Fizz". If only by 5, print "Buzz". Otherwise print the number.
for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        

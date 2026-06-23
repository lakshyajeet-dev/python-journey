# Print numbers 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1


# Ask the user to keep entering numbers until they type 0. Print the total of all numbers entered (not counting the 0).
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    print("Running total: ", total)

# Build a simple ATM — store a balance of 5000. Keep showing this menu in a loop:
# 1. Check balance
# 2. Withdraw
# 3. Exit

# If they choose 1 → print balance
# If they choose 2 → ask how much to withdraw. If amount > balance print "Insufficient funds." Otherwise subtract and print new balance.
# If they choose 3 → exit the loop
# If they enter anything else → print "Invalid option"    
# Store initial balance
balance = 5000
while True:
    print("\n--- ATM Menu ---")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Check balance
        print(f"Your balance is: {balance}")
    elif choice == 2:
        # Withdraw money
        amount = int(input("Enter amount to withdraw: "))
        
        if amount > balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Please enter a valid amount greater than zero.")
        else:
            balance = balance - amount
            print(f"Withdrawal successful. New balance: {balance}")
            
    elif choice == 3:
        # Exit the loop
        print("Thank you for using the ATM!")
        break
    else:
        # Invalid option
        print("Invalid option. Please choose between 1, 2, or 3.")

# Ask the user to guess a number between 1 and 10. The correct answer
# is stored in your code. Keep asking until they get it right.
# is stored in your code. Keep asking until they get it right.
# When correct print "Correct! You got it in X guesses."        
# Store the correct answer
# Store the correct answer
correct_number = 7

# Counter for guesses
guesses = 0

# Keep asking until correct
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses = guesses + 1   # increase guess count

    if guess == correct_number:
        print("Correct! You got it in", guesses, "guesses.")
        break
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

     
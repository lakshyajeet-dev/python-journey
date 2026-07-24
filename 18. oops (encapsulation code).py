# Define a class called BankAccount (blueprint for creating bank accounts)
class BankAccount:
    
    # Constructor method: runs automatically when a new BankAccount object is created
    def __init__(self, owner, balance):
        self.owner = owner           # public attribute → can be accessed directly
        self.__balance = balance     # private attribute → cannot be accessed directly outside the class
    
    # Method to deposit money
    def deposit(self, amount):
        """Add money to account."""
        if amount > 0:   # check if deposit amount is positive
            self.__balance += amount   # add money to balance
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount.")   # reject negative or zero deposits
    
    # Method to withdraw money
    def withdraw(self, amount):
        """Remove money from account."""
        if amount > self.__balance:   # check if withdrawal is more than balance
            print("Insufficient funds.")   # cannot withdraw more than you have
        elif amount <= 0:   # check if withdrawal is zero or negative
            print("Invalid amount.")   # reject invalid withdrawal
        else:
            self.__balance -= amount   # subtract money from balance
            print(f"Withdrawn {amount}. New balance: {self.__balance}")
    
    # Method to safely check balance
    def get_balance(self):
        """Returns current balance safely."""
        return self.__balance   # return balance (but still protected from direct access)


# ------------------- USING THE CLASS -------------------

# Create a BankAccount object named 'account' with owner Lakshyajeet and balance 5000
account = BankAccount("Lakshyajeet", 5000)

# Correct way: use methods to interact with balance
account.deposit(1000)        # adds 1000 → balance becomes 6000
account.withdraw(2000)       # subtracts 2000 → balance becomes 4000
print(account.get_balance()) # prints 4000 (safe access through method)

# Wrong way: trying to access private attribute directly
print(account.__balance)     #  Error → '__balance' is private, not accessible outside






# ✅ Correct way to access balance
# You must use the getter method:

# python
# print(account.get_balance())   # Safe access → prints 4000
# ⚡ If you really want to see the hidden attribute (not recommended, but for learning)
# You can access it using name mangling:

# python
# print(account._BankAccount__balance)   # Prints 4000
# But this breaks encapsulation rules — the whole point of __balance is to protect it from direct access.
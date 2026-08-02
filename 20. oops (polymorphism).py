class Animal:                            # Define a parent/base class called Animal
    def __init__(self, name):            # Constructor method, runs when you create an Animal object
        self.name = name                 # Store the 'name' inside the object
    
    def speak(self):                     # Define a method called speak  
        pass                             # base version does nothing

class Dog(Animal):                       # Define a Dog class that inherits from Animal
    def speak(self):                     # Override the speak method
        print(f"{self.name} says: Woof!")

class Cat(Animal):                       # Define a Cat class that inherits from Animal
    def speak(self):                     # Override the speak method
        print(f"{self.name} says: Meow!")

class Duck(Animal):                      # Define a Duck class that inherits from Animal
    def speak(self):                     # Override the speak method
        print(f"{self.name} says: Quack!")

# create objects
animals = [Dog("Tommy"), Cat("Kitty"), Duck("Donald")]

# same method call, different behavior
for animal in animals:
    animal.speak()
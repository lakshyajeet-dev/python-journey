# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class — inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent's __init__
        self.breed = breed            # dog's own attribute
    
    def bark(self):
        print(f"{self.name} is barking!")

# Child class — inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says meow!")

# create objects
dog = Dog("Tommy", 3, "Labrador")
cat = Cat("Kitty", 2, "White")

# dog can use Animal methods AND its own
dog.eat()     # inherited from Animal
dog.sleep()   # inherited from Animal
dog.bark()    # Dog's own method

# cat can use Animal methods AND its own
cat.eat()     # inherited from Animal
cat.meow()    # Cat's own method



# What is super()?

# super() calls the parent class's method. In Dog.__init__() we call super().__init__(name, age) — this runs Animal.__init__() so we don't have to rewrite that code.

# Write parent code once — all children get it automatically. That's the power of inheritance.
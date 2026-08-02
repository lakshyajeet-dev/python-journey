from abc import ABC, abstractmethod

class Shape(ABC):   # abstract class
    
    @abstractmethod
    def area(self):
        pass   # no implementation here — child must implement
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.area())        # 78.5
print(rectangle.area())     # 24
print(circle.perimeter())   # 31.4
print(rectangle.perimeter()) # 20


# Shape is the abstract class — it defines WHAT methods must exist but not HOW they work. Each child class implements them in their own way.
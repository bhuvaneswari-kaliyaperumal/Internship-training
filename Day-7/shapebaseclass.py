import math


# Animal Base Class (Polymorphism)


class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


class Cow(Animal):
    def speak(self):
        print("Cow says: Moo!")



class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")   # Calls Shape constructor
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"{self.name}(Length={self.length}, Width={self.width})"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")      # Calls Shape constructor
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Main Program

rectangle = Rectangle(10, 5)
circle = Circle(7)

print(rectangle)
print("Rectangle Area =", rectangle.area())

print()
print("Circle Area =", round(circle.area(), 2))

print("\nPolymorphism Example")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()

    """output Rectangle(Length=10, Width=5)
Rectangle Area = 50

Circle Area = 153.94

Polymorphism Example
Dog says: Woof!
Cat says: Meow!
Cow says: Moo!"""
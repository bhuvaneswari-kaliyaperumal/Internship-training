class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog woofs")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
a1 = Dog()
a1.sound()
a2 = Cat()
a2.sound()
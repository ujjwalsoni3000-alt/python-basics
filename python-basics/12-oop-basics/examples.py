class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

class Puppy(Dog):          # inheritance
    def bark(self):
        return f"{self.name} says yip!"

d = Dog("Bruno", 5)
print(d.bark())
print(Puppy("Coco", 1).bark())

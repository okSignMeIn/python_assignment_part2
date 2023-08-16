# __init__ is the constructor which will run as soon as the object is created.

class Person:
    def __init__(self, name, age):
        print("Constructor called as soon as the object is created")
        self.name = name
        self.age = age
print("Before creating object")
person1 = Person("Alice", 30)



from abc import ABC, abstractmethod




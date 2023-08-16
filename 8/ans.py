# super() is used to call a method from a base class in a subclass

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("Child class")

child = Child()
child.show()
# It's the order in which classes are searched when a method is called on an object. With the help of MRO, we can conclude which method will be called when there's different methods with the same name that are inherited from other classes.

class A:
    def method(self):
        print("inside A's method")
class B: 
    def method(self):
        print("inside B's method")
class C(A,B):
    def show(self):
        self.method()
c=C()
c.show()

# Now, there's 2 methods with the same name "method", but when we call the method(), A's method gets called because it was inherited first. If we want to call B's method, then we need to change the order of inheritance. The method that will be called without running the code is determined by MRO.

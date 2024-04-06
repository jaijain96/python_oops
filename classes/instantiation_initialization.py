"""
"""
from typing import Self

class A:
    x = 0
    y = 0

    def __new__(cls) -> Self:
        # the __new__() dunder method creates a new empty object, i.e, instantiates a new object but doesn't initialize the instance
        print("A __new__() called")

        # calling super() creates an object of the super class, the super class for any class in python is the object class, therefore, we are first creating an empty object instance and then calling its __new__ dunder method with the current class reference -> TODO: this is probably related to python data model and metaclasses -> which we will cover later
        return super().__new__(cls) # the __new__() dunder method passes the instantiated object to the __init__() method
    
    def __init__(self) -> None:
        # the __init__() dunder method initializes the object received from the __new__() dunder method
        print("A __init__() called")
        self.z = 0

        # note that __init__ shouldn't explicitly return anything; implicitly, it returns None
        # return None # although this will work but is not needed since python implicitly returns None from any method that doesn't return anything
        # return self.z  # this will raise a TypeError exception
    
    def __repr__(self) -> str:
        # the __repr__() dunder method should return a string representation of the object whenever printed
        print("from __repr__ of class A")
        if hasattr(self, "z"):
            return f"x: {self.x}, y: {self.y}, z: {self.z}"
        else:
            print("z not initialized, omitting")
            return f"x: {self.x}, y: {self.y}"

# we can create a initialized instance of A class using the constructor
a0 = A()
print(a0)

# we can create a non-initialized instance
a1 = A.__new__(A)
print(a1) # not that at this point only class attributes would have been initialized and any instance attributes would only get initialized after __init__() dunder method call
a1.__init__()
print(a1)

# somewhat interesting behaviour with __new__() dunder method, a class's __new__() dunder method can return an instance of a different class

class B:

    def __new__(cls) -> Self:
        print("B __new__() called")
        return A()  # returning a fully initialized instance of class A
    
    def __init__(self) -> None:
        print("B __init__() called")

b = B()  # when __new__() returns an instance of a different class, python constructor call will not call __init__(); note that b's init is not initialized, it is not an instance of class B even though it seems like that
print(b)  # note that since B's __new__() does initialize and return an instance of A but doesn't initialize b, printing an b is like printing an instance of A, and as such, A's representation, i.e, __repr__() for A will be called
# this is also evident if we check whether b is instance of B or of A
print(f"isinstance(b, B): {isinstance(b, B)}")  # returns False
print(f"isinstance(b, A): {isinstance(b, A)}")  # returns True

# but what if we explicitly call b's __init__() 
b.__init__()  # ambiguous? -> no, since b is an instance of class A, A's __init__ will be called

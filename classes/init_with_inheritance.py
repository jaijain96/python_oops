"""
"""
from typing import Self

class A:
    x = 0
    y = 0

    def __new__(cls) -> Self:
        print("A __new__() called")
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print("A __init__() called")
        self.z = 0
    
    def __repr__(self) -> str:
        print("from __repr__ of class A")
        if hasattr(self, "z"):
            return f"x: {self.x}, y: {self.y}, z: {self.z}"
        else:
            print("z not initialized, omitting")
            return f"x: {self.x}, y: {self.y}"


# __init__() with inheritance

class C(A):

    def __new__(cls) -> Self:
        print("C's __new__() called")
        return super().__new__(cls)

    def __init__(self) -> None:
        # super().__init__()  # since this is commented, A's __new__() is called but A's __init__() is not called, so if you expect some attributes from A to be available, they won't be unless you call super
        print("C's __init__() called")
        print(self)  # since we don't have a __repr__ for C, this will print A's __repr__, A's attribute z would not have been initialized 
        super().__init__()  # although this works, it is generally advisable to keep the super().__init__() call as the first call in the child classes __init__() so that everything from the base class is available in the inherited class
        print(self)  # A has now been initialized, z would be available and would be printed in C's repr


c = C()
# print(C.__mro__)
# the order of execution if C defines its __new__() and call's super().__init__() in its own __init__() would be:
#  C.__new__() -> A.__new__() -> C.__init__() -> A.__init__()
# if anything is omitted, let's say, C doesn't define its own __new__(), it would simply be omitted from the above execution flow as well, so in that case, execution flow would be:
# A.__new__() -> C.__init__() -> A.__init__()
# if A had not defined its __new__() method, then execution flow would have been:
# C.__init__() -> A.__init__()
# if C.__init__() doesn't call super()__init__(), it would also be omitted from the execution flow

# important thing to note is that __init__() is present in the object class and that implementation is called if we don't override __init_() in our class definition

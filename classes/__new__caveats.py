"""
"""
from typing import Self

class A:
    def __new__(cls, *args, **kwargs) -> Self:
        # its good to have args and kwargs in the definition of __new__
        # note that the super class object's __new__(), i.e,
        #  object.__new__(cls) doesn't take any additional args, only the cls to instantiate
        print("A's __new__() called")
        return super().__new__(cls, *args, **kwargs)  # this will give a TypeError that object class only expects a single argument

a = A()  # note that this will work even though this calls A's __new__ and in it's definition, we are calling super().__new__(cls, *args, **kwargs); why? because we aren't passing any args or kwargs yet
# a = A(2)  # this raises TypeError and rightly so


class B:
    x = 0
    y = 0
    def __new__(cls, *args, **kwargs) -> Self:
        print("B's __new__() called")
        return super().__new__(cls) # this works
    
    def __init__(self) -> None:
        print("B's __init__() called")
        self.z = 0

class C(B):
    # def __new__(cls, *args, **kwargs) -> Self:
    #     # __new__() can be used to modify class instantiation even before the call to __init__(), for this we grab an instance of the super() class, which would either be the immediate parent class or the object class, we then modify it and return the modified instance
    #     # TODO: what is special about __new__, could we not have done the same thing we did here in C's __init__()? do we not get class attributes of the super class if we don't call super() explicitly?, but when we are modifying __new__() in subclass, we are anyway explicitly calling the parent class's __new__()
    #     print("C's __new__() called")
    #     b_instance = super().__new__(cls, *args, **kwargs)
    #     print(f"isinstance(b_instance, B): {isinstance(b_instance, B)}")

    #     # modify instance of b even before initialization
    #     b_instance.x = 1
    #     b_instance.y = 1
    #     return b_instance
    
    def __init__(self) -> None:
        print("C's __init__() called")
        # super().__init__()
        self.x = 1
        self.y = 1
        # modifying new will help if we aren't only modifying the class attributes, but also want to modify the instance attributes? but we can do that here in __init__() itself
        # super().__init__()  # will call B's __new__() to create an instace and then __init__() to initialize that instance, we will get z here
        self.z = 1

b = B()
print(b.x, b.y, b.z)
print(f"isinstance(b, B): {isinstance(b, B)}")
c = C()
print(c.x, c.y, c.z)
print(f"isinstance(c, C): {isinstance(c, C)}")

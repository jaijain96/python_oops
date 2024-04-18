"""
"""
from typing import Self

class A:
    def __new__(cls) -> Self:
        print("A's new called")
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print("A's init called")
        self.x = 5
        print(f"A.x: {self.x}[{hex(id(self.x))}]")

class B(A):
    def __new__(cls) -> Self:
        print("B's new called")
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print("B's init called")
        super().__init__()
        print(f"B.x: {self.x}[{hex(id(self.x))}]")

class C(A):
    def __new__(cls) -> Self:
        print("C's new called")
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print("C's init called")
        super().__init__()
        print(f"C.x: {self.x}[{hex(id(self.x))}]")

b = B()
c = C()

"""
"""
# from typing import Self

class A:
    def __init__(self, x) -> None:
        self.x = None
        # pass

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val


a = A(3)
print(a.x)
print(a._x)

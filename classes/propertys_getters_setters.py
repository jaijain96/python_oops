"""
"""
# from typing import Self

class A:
    def __init__(self, val) -> None:
        # we have declared a property called y below, when we assing it here in
        # the init, the assgiment goes via the setter and assigns val to self.x
        # which is the variable we don't want to expose
        # note that although we are trying to hide x this way, there is nothing
        # stopping someone from modifying x directly
        self.y = val

    @property
    def y(self):
        return self.x
    
    @y.setter
    def y(self, val):
        self.x = val
    
    @y.deleter
    def y(self):
        del self.x


a = A(3)
print(f"a.y: {a.y}")
print(f"a.x: {a.x}")
a.y = 5
print(f"a.y: {a.y}")
print(f"a.x: {a.x}")

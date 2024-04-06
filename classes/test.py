"""
"""

class Door0:
    color = "yellow"
    def __init__(self) -> None:
        print("Door0 init call")

# question: can we change class attributes from an instance, yes, we can, but it changes only for that instance
door0 = Door0()
print(f"door0.color before change: {door0.color}")
door0.color = "red"
print(f"door0.color after change: {door0.color}")
print(f"Door0.color after change: {Door0.color}")

# question: can an instance attribute have the same identifier as a class attribute, yes, we are just modifying the class attribute for that class
class Door1:
    color = "yellow"
    def __init__(self) -> None:
        print("Door1 init call")
        self.color = "white"

door1 = Door1()
print(f"door1.color before change: {door1.color}")
door1.color = "red"
print(f"door1.color after change: {door1.color}")
print(f"Door1.color after change: {Door1.color}")

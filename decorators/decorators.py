"""
"""
# from typing import Self
import functools

def decorator(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print("begin hello")
        return_list = []
        return_list.append(method(*args, **kwargs))
        print("end hello")
        return (*return_list,)
    return wrapper

def funct0(x):
    return f"hello: {x}"


# funct0(5)

# funct0 = decorator(funct0)
# print(funct0(5))

@decorator
def funct1():
    return "hello"

# print(funct1())

# help(print)

def do_twice(method):
    @functools.wraps(method)
    def wrapper():
        method()
        method()
    return wrapper    

@do_twice
def funct2():
    print("hello from funct2")

funct2()

def repeat(num_times=1):
    def decorator_repeat(method):
        @functools.wraps(method)
        def wrapper_repeat():
            for _ in range(num_times):
                method()
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=5)
def funct3():
    print("hello from funct3")

funct3()


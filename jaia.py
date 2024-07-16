"""
"""

# # arr = [5, 10, 1, 6, 2, 8, 3, 7, 11]
# # arr = [1, 3, 5, 6]
# # arr = [1, 2, 4]
# arr = [1, 2]

# n = len(arr)
# print(n)

# sum_actual = sum(arr)
# print(sum_actual)

# sum_expected = ((n + 2) * (n + 2 + 1)) // 2
# print(sum_expected)

# diff = sum_expected - sum_actual
# print(diff)

# sum_diff_half = ( (diff // 2) * (diff // 2 + 1)) // 2
# print(f"sum_diff_half: {sum_diff_half}")

# for val in arr:
#     if val <= (diff // 2):
#         sum_diff_half -= val
#         print(sum_diff_half)

# print(sum_diff_half, diff - sum_diff_half)

# lst = [0, 1, 2, 3, 4]
# print(lst[::-1])

# print(f'{"*" * 5}\n'*5)

# lst0 = [1, 0, 2, 0]
# print(lst0)

# def map_method(x):
#     return x + 1

# lst1 = list(map(map_method, lst0))
# print(lst1)

# def filter_method(x):
#     return x == 0

# lst2 = list(filter(filter_method, lst0))
# print(lst2)

# import functools

# def reduce_method(x, y):
#     return x + y

# cumulative_val = functools.reduce(reduce_method, lst0)
# print(cumulative_val)

# cumulative_val = functools.reduce(reduce_method, lst0, 5)
# print(cumulative_val)

# lst3 = dict(zip("abcd", [0,1,2]))
# print(lst3)

# f = lambda x, y: x + y
# print(f(5, 7))

# def multi_map_method(x, y):
#     return x + y

# lst4 = list(map(multi_map_method, lst0, lst0))
# print(lst4)


# def decorator(method):
#     @functools.wraps(method)
#     def wrapper(*args, **kwargs):
#         print("begin hello")
#         return_list = []
#         return_list.append(method(*args, **kwargs))
#         print("end hello")
#         return (*return_list,)
#     return wrapper

# def funct0(x):
#     return f"hello: {x}"


# funct0(5)

# funct0 = decorator(funct0)
# print(funct0(5))

# @decorator
# def funct1():
#     return "hello"

# print(funct1())

# # help(print)

# class A:
#     def __init__(self, x) -> None:
#         self.x = x


# a = A(5)
# b = a

# print(f"a == b: {a == b}")
# print(f"a is b: {a is b}")

# x = 5
# y = x

# print(f"x: {x}, id(x): {id(x)}")
# print(f"y: {y}, id(y): {id(y)}")
# print(f"x == y: {x == y}")
# print(f"x is y: {x is y}")

# x = 6

# print(f"x: {x}, id(x): {id(x)}")
# print(f"y: {y}, id(y): {id(y)}")
# print(f"x == y: {x == y}")
# print(f"x is y: {x is y}")

# lst0 = [2, 4, 6]
# lst1 = [2, 4, 6]

# print(f"lst0: {lst0}, id(lst0): {id(lst0)}")
# print(f"lst1: {lst1}, id(lst1): {id(lst1)}")
# print(f"lst0 == lst1: {lst0 == lst1}")
# print(f"lst0 is lst1: {lst0 is lst1}")

# lst1 = [2, 4, 6, 8]

# print(f"lst0: {lst0}, id(lst0): {id(lst0)}")
# print(f"lst1: {lst1}, id(lst1): {id(lst1)}")
# print(f"lst0 == lst1: {lst0 == lst1}")
# print(f"lst0 in lst1: {lst0 in lst1}")

# str0 = "helloworld"
# str1 = "owor"

# print(f"str1 in str0: {str1 in str0}")
# print(any(char is str0 or char == str0 for char in str1))

# x = 5
# y = 6

# print("x:", x, ", y:", y)
# print(f"x is y: {x is y}")
# print(f"x is not y: {x is not y}")
# print(f"not x is y: {not x is y}")
# print(f"not (x is y): {not (x is y)}")
# print(f"not y: {not y}")
# print(f"x is (not y): {x is (not y)}")
# print(f"x is not y is (not (x is y)): {x is not y is (not (x is y))}")
# print(f"not y is (not (x is y)): {not y is (not (x is y))}")
# print(f"id(x is not y): {id(x is not y)}")
# print(f"id(not (x is y)): {id(not (x is y))}")
# print(f"x is not y == (not (x is y)): {x is not y == (not (x is y))}")
# print(f"x is not y is not (x is y): {x is not y is not (x is y)}")
# # print(f"x is not y == (not (x is y)): {x is not y == not (x is y)}")  # syntax error
# print(f"x is not y is not x is y: {x is not y is not x is y}")
# print(f"(x is not y) is (not (x is y)): {(x is not y) is (not (x is y))}")
# print(f"(x is not y) == (not (x is y)): {(x is not y) == (not (x is y))}")

# from operator import attrgetter, itemgetter

# dct = {"hello": 2, "bob" : 6, "world" : 5, "ab" : 6}

# def funct0(key):
#     return (key, dct[key])

# def funct1(key):
#     return (dct[key], key)

# def comparator(key):
#     return dct[key]

# print(list(map(funct0, sorted(dct, key=lambda dct_key : dct[dct_key]))))
# print(dict(map(funct1, sorted(dct, key=comparator))))

# tuples = list(zip(dct.keys(), dct.values()))
# print(f"tuples: {tuples}")
# print(sorted(tuples, key=itemgetter(1,0)))

# # print([(lambda key : (key, dct[key])) for key in sorted(dct)])

# from time import perf_counter_ns
# import sys

# sys.setrecursionlimit(10000)
# sys.set_int_max_str_digits(100000)

# total = 100
# lst = [None] * (total + 1)
# # print(lst[:11])
# lst[0] = 1

# def fact(n):
#     # print(n)
#     if n < 1:
#         return 1
#     else:
#         if lst[n] is None:
#             # print("goes in if")
#             lst[n] = (n * fact(n - 1))
#         return lst[n] 
#         # return (n * fact(n - 1))

# begin = perf_counter_ns()
# for i in range(total):
#     print(fact(i))
#     # print(lst)
# print(f"time taken: {perf_counter_ns() - begin} nanoseconds")
# print(lst[:total + 1])


# import package.decorators as decorators

# from dataclasses import dataclass

# @dataclass
# class A:
#     x: int
#     y: str


# a = A(5, "foo")
# print(a)

# from collections import namedtuple

# Person = namedtuple("Person", "name age")
# p0 = Person("foo", "bar")
# print(p0)


# import asyncio


# async def coro(idx):
#     print(idx)
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     # for i in range(5):
#     #     print(f"{idx}: {i}")

# async def spawner():
#     # coro_list = []
#     for idx in range(5):
#         await coro(idx)
#         # coro_list.append(coro(idx))
#     # await asyncio.gather(*coro_list)

# import time

# begin = time.perf_counter()
# asyncio.run(spawner())
# print(f"time taken: {time.perf_counter() - begin}")


def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)

    return multipliers

for multiplier in create_multipliers():
    print(multiplier(2))

def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x, j=i):
            return j * x
        multipliers.append(multiplier)

    return multipliers

for multiplier in create_multipliers():
    print(multiplier(2))
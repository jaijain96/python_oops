from functools import reduce

keys = ["key3", "key1", "key0", "key2"]
vals = [67, 85, 32, 95]

"""
using the "map" inbuilt method in python, create a dictionary where the above
list "keys" are the keys of the dictionary and the list "vals" are the
corresponding values of the dictionary
"""

# code here

def funct0(x, y):
    return (x,y)

dct = dict(map(funct0, keys, vals))
print(dct)

"""
using the "reduce" method in python, calculate the sum of values of the list "vals"
"""

# code here

def funct1(val0, val1):
    return val0 + val1

res = reduce(funct1, vals)
print(res)


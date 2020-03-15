# Data types in python:
# Numbers
# String
# list
# tuple
# set
# dictionary

num = 10
print(type(num))

name = "cmpundhir"
print(type(name))

# it is an ordered collection
accessories = ["earphone", "smart watch", "ePen"]
print(type(accessories))

# set contains unique elements only and is unordered
jwel_set = {"neckles", "ring", "ring", "breslet", "earring"}
print(jwel_set)
print(type(jwel_set))

# tuple is similar to list but it is immutable i.e, cannot be modified
bike_parts = ("engine", "handle", "tyres", "breaks", "oil tanks", "seats")
print(type(bike_parts))

# dictionary is a key value pair, and it can have different types of keys
person = {"name": "cmpundhir", "id": 1, "contact": 123456789, 100: 12}
print(type(person))
print(person["name"])


# Tuples

'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets*.
'''

# Ordered, Heterogenous and Immutable

# Empty Tuple
t1 = ()
t1 = tuple()

t1 = (1, "Hello", [10, 50], (1, 2, 3))  # Heterogenous

# Single element
t1 = "Hi",
print(type(t1))

superheroes = ("Iron Man", "Captain America", "Thar", "Hunk")
# superheroes[3] = "Hulk" - Not allowed because tuples are immutable

# Length - Number of elements
# Index
superheroes.index("Iron Man")
print(superheroes[3])

# Operations
# Concatenation
print((1, 2) + (3, 4))
print((1, 2) * 10)
print("Hunk" in superheroes)
print("Thor" in superheroes)
print("Hunk" not in superheroes)
print("Thor" not in superheroes)

# Methods
# index and count
print(superheroes.index("Iron Man"))
print(superheroes.count("Captain America"))

print("################")

# Unpacking
s1, s2, s3 = ("Iron Man", "Thor", "Hulk")
print(s1)
print(s2)
print(s3)
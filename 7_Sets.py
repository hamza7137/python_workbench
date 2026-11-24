# Set

# Heterogenous, Mutable collection of Elements
# Unordered, Unique collection of elements

# Empty Set
s1 = set()

# Elements

# Only Allows Immutable Data Types
s1 = {1, "Hello", (1, 2), 1, 2, "Hello"}
print(s1)

# There is no concept on Index since the elements are not ordered

s1.add(1234)
print(id(s1))
print(s1)
print(id(s1))  # Mutable Elements

# Nested sets are not possible - Because sets doesn't allow Mutable types and set itself is a Mutable type

# Unique Elements

# Union

s1 = {"Iron Man", "Black Widow", "Captain Marvel", "Hawkeye", "Nick Fury"}
s2 = {"Nick Fury", "Agent Hill", "Black Panther", "Iron Man", "Hulk"}

print(s2.union(s1)) # Union of two sets will give all the unique elements in both the sets

# Intersection

print(s2.intersection(s1)) # Intersection of two sets will give the common elements in both the sets

# Difference

print(s2.difference(s1)) # Difference of two sets will give the elements in s2 that are not in s1

# Symmetric Difference

print(s2.symmetric_difference(s1)) # Symmetric Difference of two sets will give the elements that are in either set but not in both

s1.add("kajsdlj")
print(s1)

s1.remove("Captain Marvel")
print(s1)

s1.pop()
print(s1)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 4, 6}
print(s2.issubset(s1))
print(s1.issuperset(s2))
#############################################

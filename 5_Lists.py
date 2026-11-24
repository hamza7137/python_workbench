# Lists

'''
List is a built-in data structure used to store an ordered collection of items. 
They are dynamic, resizable and capable of storing multiple data types.

1. List elements can be changed, updated, added, or removed after the list is created.
2. Elements maintain the order in which they are inserted.
3. Elements are accessed using their position, starting from index 0.
'''

# Ordered, Heterogenous and Mutable

# Empty List
l1 = []
l1 = list()

# With Elements

l1 = [1, 2, 3, 4]

# Ordered - The order of insertion of elements will be preserved
print(l1[3])

# Heterogenous and Homogenous
# Homegenous - Allows only one type of data
# Heterogenous - Allows various datatypes
l1 = [1, "Hello", 1.5, True, [1, 2, 3]]

############

# Mutable
superheroes = ["Iron Man", "Captain America", "Thar", "Hulk"]
print(superheroes)
print(id(superheroes))
superheroes[2] = "Thor"
print(superheroes)
print(id(superheroes))

# Length - Number of elements
print(len(superheroes))
# print(superheroes.index("Thar")) # Will throw error because Thar is not present in the list

# print(superheroes[5]) #Throws error index out of range

# Operations
# Concatenation
s1 = ["Iron Man", "Captain America", "Thor", "Hunk", "Iron Man"]
s2 = ["Black Panther", "Winter Solider", "Falcon", "Ant Man"]

new_superheroes = s1 + s2
print(new_superheroes)

# Repetition

print(s1 * 5)

# Membership Check - in and not in
print("Iron Man" in s1)
print("Iron Man" not in s1)

# Replacement Operation
s1[3] = "Hulk"
print(s1)

print("----------------------")

# Methods
# Append
new_superheroes = ['Iron Man', 'Captain America', 'Thor',
                   'Hunk', 'Black Panther', 'Winter Solider', 'Falcon', 'Ant Man', "Iron Man"]

print("----------------------")
print(new_superheroes.count("Iron"))
print("----------------------")

# Adds at the end of the list - only add single element
new_superheroes.extend(["Spiderman", 10])
print(new_superheroes)

# Extend - Adds the individual elements from an collection of items
s1.extend(s2)
print(len(s1))

# Insert
print(s1)
s1.insert(1, "Winter Solider")
print(s1)

# Pop - Remove element at a given index - by default removes the element at last index
s1.pop(5)
print(s1)

print("----------------------")
print(new_superheroes.count("Iron Man"))
print("----------------------")
# Remove - By Value. Not Index
s1.remove("Iron Man")
print(s1)

# NULL - None
# Copy

avengers = ["Tony", "Steve", "Bruce", "Thor"]
superheroes = avengers.copy()
print(id(avengers))
print(avengers)
print(id(superheroes))
print(superheroes)

avengers.append("Black Widow")
print(avengers)
print(superheroes)

# Clear

# avengers.clear()
# print(avengers)

avengers.sort(reverse=True)
print(avengers)
avengers.reverse()
print(avengers)
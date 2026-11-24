# Dictionaries

'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''

# Creating a Dictionary - Empty
d1 = {}
d1 = dict()

# With Elements
# Values can be of any type
# Keys - only Immutable Type - Int, boolean, Strings, Tuples, Frozenset
# Sets, Lists, Dictionaries - Can't be dictionary keys since they are mutable
x = "name"
y = "Peter Parker"
d1 = {x: y, "superhero_name": "Spiderman",
      "age": 26, "place": "Queens", "movies": ["Civil War", "Endgame", "Infinity War"]}

print(d1[x])

# print(d1["Place"]) - Case sensitive

print(d1["place"])

print(d1)

d1["age"] = 26
print(d1)

d1["new_movie"] = "Brand New Day"
print(d1)

print("Spiderman" in d1)  # Will return false since it checks only Keys

########################################################
# Methods
print(id(d1))
# d1.clear() Will remove all elements from the dictionary
print(id(d1))
print(d1)
print("Spiderman" in d1.values())
print(d1.values())  # Only Values
print(d1.keys())  # Only Keys
print(d1.items())  # List of tuples with Key-Value as elements

d1.pop("name")
print(d1)

d1.popitem()  # Last Inserted Key-Value pair
print(d1)

d1.update({"name": "Peter Parker",
          "mentored_by": "Tony Stark", "love_interest": "MJ"})
print(d1)

# Copy
d2 = d1.copy() # Shallow Copy - Changes in d1 will not reflect in d2 and vice versa

print("#############################################")
d1["name"] = "Pete"

print(id(d1))
print(d1)
print(id(d2))
print(d2)

# find vs index
############################
print(d1["name"])
print(d1.get("name", "NA"))

t1 = ("a", "b", "c")
d2 = dict.fromkeys(t1, "NA") # Creates a dictionary with keys from the tuple and assigns "NA" as the value for all keys

print(d2)
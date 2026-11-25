# Loops :

'''
Repeating the same block of code multiple times

for - while

for -> When we know the number of elements - especially when operating on collection elements like strings, lists, tuples, set and dictionaries
while -> when we don't know the number of elements. Based on condition.

Syntax
for < element > in < collection >:
logic
'''

avengers = ("Tony", "Winter Solder", "Falcon") # tuple
print(type(avengers))

for i in avengers:
    print(i)
    if len(i) <= 4:
        print("Short name")
    else:
        print("Normal Name")

avengers = [
    {
        "name": "TS",
        "Gender": "M"
    },
    {
        "name": "CM",
        "Gender": "F"
    },
    {
        "name": "BP",
        "Gender": "M"
    },
    {
        "name": "Wasp",
        "Gender": "F"
    }
]

print(type(avengers))

print("For loop with membership check")

avengers = ["Steve", "Peter", "Hawkeye", "Loki", "Thanos", "Bruce"]

for i in avengers:
    if "e" in i:
        print(i)

l = [1, 2, 3, 4, 5]
m = [10, 5]

print("Nested for loop")

for i in l:
    print("------------------")
    print(i)
    for j in m:
        print(j)

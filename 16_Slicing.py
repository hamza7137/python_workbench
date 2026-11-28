# Slicing - Extracting part of a collection

avengers = ["War Machine", "Falcon", "Winter Solider",
            "Ant Man", "Hawkeye", "Vision", "The Wasp", 
            "Captain Marvel", "Thor", "IronMan", 
            "Star Lord", "Spiderman"]

# Default values
# Start - 0
# End - len()
# Step - 1

print(avengers[1:6:1])
print(avengers[1:6:3])

print(avengers[-1: -7: -1])

print(avengers[::-1])

print(avengers[3:10:3])
print(avengers[-2:-8:-2])

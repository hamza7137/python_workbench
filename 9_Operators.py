# Operators : help us perform operations

# Arithmetic
# +, -, *, /

print(6/3)  # Division by default gives a float value
print(6//4)  # Floor Division -> Nearest Lowest integer

print(10 % 2)  # Remainder of division between 10 and 2 - 0
print(10 % 3)  # Remainder of division between 10 and 3 - 1

print(10 ** 2)  # Exponent operator - 10 raised to the power of 2

# Comparison Operators

a = 10
b = 5

print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

print(a == b)  # Check
print(a != b)

#########

x = 5  # Assignment

# Compound Assignment Operators
x += 2
print(x)
x -= 3
print(x)
x *= 6
print(x)
x /= 7
print(x)

# Logical Operators
print("***********")
a = 10
b = 2

# or
# True False - True
# True True - True
# False True - True
# False False - True
print(a > 6 or b < 3)

# and
# True False - False
# True True - True
# False True - False
# False False - False
print(a > 6 and b < 3)

# Membership Operator

name = "Tony Stark"
print("ny" in name)
print("st" not in name)

# Identity Operator
print("## Identity Op ##")
x = [1, 2, 3]
y = x.copy()

print(id(x))
print(id(y))
print(x == y) # Check if values are same
print(x is not y) # Check if both are not same object in memory

print(id(x) == id(y)) # Check if both are same object in memory
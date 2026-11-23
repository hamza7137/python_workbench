# Strings - 

"""Strings are sequence of characters written inside quotes. It can include letters, numbers, 
symbols and spaces. Python does not have a separate character type.

1. A single character is treated as a string of length one.
2. Strings are commonly used for text handling and manipulation.
"""

# Empty String
name = ""
print(type(name))  # class 'str'

name = ''
print(type(name))  # class 'str'

# String with elements
name = "TONY STARK"
print(type(name))

# Length - Number of characters in a string
print(len(name))

# Index - Position of the element in the string - Only first occurrence - Starts from Zero
print(name.index("K"))  # Case sensitive

print(name.index("T")) # Will print the first occurrence of T so it will print 0

print(name.index("TA"))

# Accessing Elements

# Last Index - (length - 1)
print(name[5])
print(name[9])

# # Why Double and Single Quotes?

x = 'SELECT * FROM table where column="abc"'

print(x) # Single-quoted string can contain double quotes without escaping.

#2. Using single quotes inside a single-quoted string

# x = 'SELECT * FROM table where column='abc''

print(x) # This will cause a syntax error because the single quote inside the string is not escaped.


# Escaping

x = 'SELECT * FROM table where column=\'abc\''
x = "SELECT * FROM table where column=\"abc\""

print(x)

# Operations

# Concatenation - Is Combining 2 or more string to form a single string
firstname = "Tony"
lastname = "Stark"
fullname = firstname + " " + lastname
print(fullname)

# Repetition
print(firstname * 10)

# Membership Check - Check if a pattern is present or not
print("y" in firstname)  # Membership Operator
print("y" not in firstname)  # Membership Operator

# Multiline String

query = '''WITH CategorySales AS ('
    -- Calculate total sales per category
    SELECT 
        c.CategoryName,
        SUM(oi.Quantity * oi.UnitPrice) AS TotalRevenue,
        COUNT(DISTINCT o.OrderID) AS TotalOrders
    FROM 
        Categories c
    JOIN 
        Products p ON c.CategoryID = p.CategoryID
    JOIN 
        OrderDetails oi ON p.ProductID = oi.ProductID
    JOIN 
        Orders o ON oi.OrderID = o.OrderID
    WHERE 
        o.OrderDate >= '2023-01-01' AND o.OrderDate <= '2023-12-31'
    GROUP BY 
        c.CategoryName
)'''

print(query)


# Negative Indexing - doesn't start from zero
firstname = "  tony stark  "

print(firstname[-4])

# Methods of strings

firstname = "tony stark"
print(firstname.upper())
print(firstname.lower())
print(firstname.capitalize())
print(firstname.title())

# Find Method

print(firstname.find("s"))

print(firstname.startswith("to"))
print(firstname.endswith("rk"))

# Strip

firstname = "  tony stark  "

print(len(firstname.strip()))
print(len(firstname.lstrip()))
print(len(firstname.rstrip()))

# Replace

fullname = "tony-stank-howard"
print(fullname.replace("n", "r"))
print(fullname) #String is immutable so it will not change the original string

# Split - Breaking the string into a list by DELIMITER (SEPARATOR)
print(firstname.split("-"))
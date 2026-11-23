# Variables in Python

# 1. What are Variables?

""" 
Variables are one of the fundamental building blocks of programming.

A **variable** is a name used to reference or point to an object stored in memory. 
It allows us to store data and access or reuse it at different stages of a program

In Python, when we assign a value to a variable:
- Python creates an object in memory.
- The variable name refers to that object.
- We can access the object using the variable name.
- We can reassign the variable to reference a different object. 
"""

# Example

var = 10
var = 10909
var = 10900

print(var)
print(type(var))
print(id(var))

"""
Here:
- `var = 10` assigns the integer object `10` to the variable `var`.
- `var = 10909` reassigns the variable to a different integer object.
- `var = 10900` reassigns it again.

**Important:** Python variables do not store values directly in fixed memory locations. 
Instead, variable names are references to objects.
"""

# 2. Understanding Variable Reassignment

"""
The term *variable* indicates that the object a variable refers to, can change during program execution.

For example:
"""

var = "XYZ"

y = var

print(var)
print(type(var))

print(id(var))
print(id(y))

"""
Here:

- `var` references the string object `"XYZ"`.
- `y = var` makes `y` reference the same object.
- Both variables refer to the same object, so their `id()` values will be identical.

Now, let's reassign `var`:
"""

var = "abc"

print(var)
print(y)

"""
Notice that changing the reference of `var` does not affect `y`. 

The variable `y` still references the original string object `"XYZ"`.

**Important:** A variable name references one object at a time, 
but multiple variables can reference the same object.
"""

# 3. Dynamic Typing in Python

"""Python is a dynamically typed language.

This means:
- We do not need to explicitly declare a variable's datatype.
- Python automatically determines the datatype based on the object assigned to the variable.
- The same variable can reference objects of different datatypes during program execution.
"""

# Example

var = 10
print(type(var))

var = "XYZ"
print(type(var))

var = 10.5
print(type(var))

var = True
print(type(var))

"""
This behavior is known as **Dynamic Typing**.
"""

## 4. Rules for Naming Variables in Python

"""
Python follows certain rules when defining variable names.

**Rule 1: A variable name must start with a letter or an underscore.**

Valid:
"""

Abc = ""
_name = "Python"
name = "Hamza"

"""
Invalid :

1name = "Python"  # Cannot start with a number
"""

"""
**Rule 2: A variable name can contain letters, numbers, and underscores.**

Valid:
"""

Var_1 = 10
user_name = "Hamza"
employee123 = "John"

"""
Invalid:
user-name = "Hamza"  # Hyphen is not allowed
user name = "Hamza"  # Spaces are not allowed
"""

"""
**Rule 3: Python keywords cannot be used as variable names.**

Keywords are reserved words that have predefined meanings in Python's syntax.

Examples:
- `if`
- `else`
- `for`
- `while`
- `class`
- `def`
- `return`
- `import`
- `True`
- `False`

You can find the complete list of Python keywords using:
"""

import keyword

print(keyword.kwlist)

# 5. Variable Naming Conventions

"""
Apart from naming rules, Python developers follow certain conventions to make code more readable and maintainable.
"""
# 5.1 Snake Case

"""
Python generally follows the Snake Case naming convention for variables.

In Snake Case:
- All letters are lowercase.
- Multiple words are separated using underscores (`_`).

Example:
"""

favorite_movies = 1
user_name = "Hamza"
total_employee_count = 100

# 5.2 Use Meaningful Variable Names

"""
Always choose variable names that clearly describe the purpose of the data they represent.

Avoid generic names:
"""

a = 1
b = 2

print(a + b)

"""Prefer meaningful names:"""

num1 = 10
num2 = 20

total_sum = num1 + num2

print(total_sum)

"""
Meaningful variable names make code easier to understand, debug, and maintain.
"""
# 5.3 Spaces Around the Assignment Operator

"""
Use a single space before and after the assignment operator (`=`) to improve readability.

Recommended:
"""

num1 = 10
num2 = 20
total_sum = num1 + num2

"""Avoid:"""

num1=10
num2=20
total_sum=num1+num2

# 5.4 Python is Case-Sensitive

"""
Python is a case-sensitive programming language.

This means uppercase and lowercase letters are treated differently when identifying variable names.

Example:
"""

Superhero = "IronMan"

# print(Superhero)
# print(superhero)

"""
The first statement works because the variable is named `Superhero`.

The second statement raises a `NameError` because `superhero` and `Superhero` are two different identifiers.

**Remember:** Python treats `name`, `Name`, and `NAME` as three different variable names.
"""
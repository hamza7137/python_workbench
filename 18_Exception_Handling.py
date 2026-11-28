# Exception Handling - Handling the error/exceptions

'''
Exception Handling allows a program to handle unexpected errors during execution in a controlled way, instead of crashing abruptly. 
It enables programs to detect errors, manage them properly and continue execution wherever possible.

Handles runtime errors such as invalid input, file not found, division by zero and type mismatches that occur during program execution.
Helps improve program reliability by ensuring the application does not terminate unexpectedly when an error occurs.

Below is a basic example demonstrating how to catch an exception and handle it gracefully:

n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
'''

# print(1/0) # ZeroDivisionError: division by zero

# x = 1
# print(x + "2") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# y = [10, 20, 30]
# print(y[3]) # IndexError: list index out of range

# Syntax:

# try:
# logic
# except:
# what to in case of Error

i = 2
try:
    if i == 2:
        print("Both the numbers are equal")
    # print([1, 2, 3][3])
    # print(20 + "30")
    # print("I'm over here")
except ZeroDivisionError:
    print("Zero Div Occurred")
except IndexError:
    print("Index Error")
except Exception as e:
    print(f"Some Error occurred: {e}")
finally:
    print("I'm always running!")

# try - except - finally (it's optional)
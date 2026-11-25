
# Return

# 3. Functions with parameters and with return value
def add(num1, num2):
    sum = num1 + num2
    # return sum
    # print(sum)
    return sum


# Default Return value is None
# If we return something, the call's value will become the return value
print(add(5, 10))
addition = add(5, 10)
print(addition)
print("-------------")

# 4. Functions with parameters and with multiple return values
def calculator(num1, num2):
    addition = num1 + num2
    sub = num1 - num2
    mult = num1 * num2

    return addition, sub, mult

calc = calculator(30, 15)
print(calc)

# Variable Scope
# Local Variables - defined and available only within the function
length = len("Hello")
print(length)
print(id(calc))
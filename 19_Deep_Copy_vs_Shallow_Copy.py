import copy
from copy import deepcopy

print("Shallow Copy")
l1 = [1, 2, 3, [4, 5]]
l2 = l1.copy() # Shallow copy
l1[1] = 10
print(id(l1))
print(id(l2))
print(l1)
print(l2)

print("copy.deepcopy")
l2 = copy.deepcopy(l1)
l1[1] = 10
print(id(l1))
print(id(l2))
print(l1)
print(l2)


print("Deep Copy")
l2 = deepcopy(l1)
l1[1] = 10
print(id(l1))
print(id(l2))
print(l1)
print(l2)

# ###########################
# print("------------")
# l1[3][0] = 40
# print(id(l1))
# print(id(l2))
# print(l1)
# print(l2)
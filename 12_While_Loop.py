
# While Loop
# To execute a loop as long as a condition is satisfied

# while <condition>:
# logic

x = 1
l = [1, 2, 3]
while x <= 10:  # Infinite Loop - Ctrl + C to stop in case of Infinite Loop
    print("************")
    print(x)
    for i in l:
        print(i)
    x += 1


print("End of loop")
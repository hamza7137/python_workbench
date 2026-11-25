avengers = ["Steve", "Peter", "Hawkeye", "Loki", "Thanos", "Bruce"]

for i in avengers:
    if i == "Peter":
        continue  # Continue skip the execution of iteration and proceed for next iteration

    print(i)

    if i == "Loki":
        break       # Break will exit the loop completely

print("After the loop")
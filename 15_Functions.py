# Functions

'''
Functions - Reusable blocks of code.

Syntax

def <func_name>:
    logic
'''

# 1. Functions without parameters and without return value
def emergency():
    print("I'm executing from function")


emergency()

# 2. Functions with parameters and without return value
def mission_notification(avengers):  # Parameters - Exepcted Inputs

    for i in avengers:
        print(f"Hey, {i}, there is an emergency !")
        print("-------------")


avengers = ["Stark", "Steve", "Bruce"]
# mission_notification(avengers) # Passing the list of avengers as an argument to the function
# mission_notification(["Thor", "Natasha", "Black Panther"]) # Passing the list of avengers as an argument to the function


def mission_notification(city, threat_level=1, villain="Thanos"):
    level1 = ["Thor", "Stark", "Black Panther"]
    level2 = ["Bruce", "Steve", "Natasha"]
    level3 = ["Spiderman", "Doctor Strage"]

    if threat_level == 1:
        avengers = level1
    elif threat_level == 2:
        avengers = level2
    else:
        avengers = level3

    for i in avengers:
        print(
            f"Hey {i}, get ready for the mission in {city} of threat level {threat_level}")

# Positional Arguments - Based on the position of arguments
mission_notification("New York", 3)
# Default Arguments - Parameter will have a default value defined in the function definition. If the respective value is not passed while calling,
# the default will be used in the function
mission_notification("New York")
# Keyword or Named Arguments - Passing the arguments using the name of the arguments
mission_notification(villain="Dr. Doom", threat_level=1, city="New York")
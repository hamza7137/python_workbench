# Control Structures / Control Flow

# These will control the flow of the execution

# Syntax

# if <condition>:
# logic

'''
Control flow refers to the order in which statements within a program execute. 

While programs typically follow a sequential flow from top to bottom, there are scenarios where we need more flexibility. 

This article provides a clear understanding about everything you need to know about Control Flow Statements.
'''

avengers_year = 2016

if avengers_year == 2012:
    print("Correct")
elif avengers_year in [2009, 2010, 2011, 2013, 2014, 2015]:  # elif - else if
    print("Not correct but Close")
elif avengers_year in [2008, 2016]:
    print("Too far")
else:
    print("Not correct")

number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

spiderman = {"name": "Peter Parker", "place": "Queens"}

if spiderman["name"] == "Peter Parker":
    print("Correct")
else:
    print("No")

##############

superhero_name = "Tony"

if superhero_name in ["Steve", "Tony", "Thor"]:
    if superhero_name in ["Tony", "Steve"]:
        print("From Earth")
        if superhero_name == "Tony":
            print("Billionaire")
        else:
            print("Oldest")
    else:
        print("Alien Avenger")
else:
    print("Female")

#######################################

avengers = [
    {
        "name": "TS",
        "Gender": "M"
    },
    {
        "name": "CM",
        "Gender": "F"
    },
    {
        "name": "BP",
        "Gender": "M"
    },
    {
        "name": "Wasp",
        "Gender": "F"
    }
]

avengers = ["Tony", "Winter Solder", "Falcon"]

if len(avengers) > 0:
    print("Yes")
else:
    print("No")

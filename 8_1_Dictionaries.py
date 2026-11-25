marvel_data = {
    "team": "Avengers",
    "base": {
        "name": "Avengers Tower",
        "location": "New York",
        "facilities": ["Lab", "AI Control", "Hangar", "Living Quarters"]
    },
    "members": [
        {
            "name": "Iron Man",
            "real_name": "Tony Stark",
            "powers": ["Genius Intelligence", "Powered Armor Suit"],
            "weapons": {
                "primary": ["Repulsor Beams", "Unibeam"],
                "secondary": ["Missiles", "Laser"]
            },
            "allies": ["War Machine", "Spider-Man"],
            "status": "Active"
        },
        {
            "name": "Captain America",
            "real_name": "Steve Rogers",
            "powers": ["Super Strength", "Enhanced Agility"],
            "weapons": {
                "primary": ["Vibranium Shield"],
                "secondary": []
            },
            "allies": ["Falcon", "Bucky Barnes"],
            "status": "Active"
        },
        {
            "name": "Thor",
            "real_name": "Thor Odinson",
            "powers": ["God of Thunder", "Flight"],
            "weapons": {
                "primary": ["Mjolnir", "Stormbreaker"],
                "secondary": []
            },
            "allies": ["Loki", "Heimdall"],
            "status": "Active"
        },
        {
            "name": "Hulk",
            "real_name": "Bruce Banner",
            "powers": ["Super Strength", "Regeneration"],
            "weapons": {
                "primary": [],
                "secondary": []
            },
            "allies": ["Black Widow"],
            "status": "Active"
        }
    ],
    "villains": [
        {
            "name": "Thanos",
            "goal": "Balance the universe",
            "powers": ["Super Strength", "Infinity Gauntlet"],
            "stones": ["Space", "Time", "Reality", "Power", "Mind", "Soul"]
        },
        {
            "name": "Ultron",
            "goal": "Destroy humanity",
            "powers": ["AI Intelligence", "Robot Army"],
            "created_by": "Tony Stark"
        }
    ]
}

print(marvel_data["base"]["name"])
print(marvel_data["members"][2]["weapons"]["primary"][1])

x = {"x": [{"a": "b", "c": [1, 2, 3]}]}
print(x["x"][0]['c'][1])
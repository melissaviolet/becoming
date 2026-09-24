shuga_dict = {
    "first_name": "Melissa",
    "last_name": "Violet",
    "city": "Kampala",
    
    "status": "single",
    "course": "Computer Science",
    "hobby" : "music",
    "aspiration": "piano"
}

print("The information about this girl is:")
for k,v in shuga_dict.items():
    print(f"{k.title()} -> {v.title()}")

print(shuga_dict["first_name"])
something = shuga_dict["status"]


print(f"Melissa is actually very {something}, she isn't seeing anyone. In real life she has actually never dated anyone.")

print(f"Shuga was 22 years old when she decided to actually focus on herself, love herself more, fight jealous and change her life for the better.")

print(f"Shuga lives in {shuga_dict["city"]}.")

rivers = {
    "nile": "egypt",
    "amazon": "usa",
    "katonga": "uganda"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for country in rivers.values():
    print(f"{country.title()}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

poll_names = ["violet", "jen", "marie", "edward", "phil"]

for name in poll_names:
    if name in favorite_languages.keys():
        print(f"{name.title()}! Thank you for taking the poll.")
    else:
        print(f"{name.title()}! Please take the poll.")

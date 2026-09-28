# Working with dictionaries

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

# Looping thru dictionaries
rivers = {
    "nile": "egypt",
    "amazon": "usa",
    "katonga": "uganda"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for country in rivers.values():
    print(f"{country.title()}")

# Looping thru lists and dictionaries
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

# Nesting

person1 = {
    "first_name": "assumpta",
    "last_name": "maria",
    "city": "kampala"
 }

person2 = {
    "first_name": "melissa",
    "last_name": "violet",
    "city": "gulu"
}

people = [person1, person2]

for person in people:
    print(f"The information about this person is; {person}")


favourite_places = {
    "carol": ["berlin", "waterfalls"],
    "brianah": ["paris","dubai", "lake"],
    "vydia": ["london", "newyork"],
    "marcus": ["home"]
}

for name, places in favourite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favourite places are;")
    else:
        print(f"\n{name.title()}'s favourite place is;")
    for place in places:
        print(f"\t{place.title()}")

cities = {
    "paris": {"country":"france", "fact": "romance", "population": 2_000_000},
    "newyork" : {"country": "usa", "fact":"busy", "population": 7_000_000},
    "losangelos" : {"country": "usa", "fact": "movies", "population": 5_000_000}
}

for city, information in cities.items():
    print(f"\n{city.title()}")
    country = f"{information['country']}"
    fact = f"{information['fact']}"
    population = information["population"]

    print(f"Country: {country.title()}")
    print(f"Popularly known for: {fact.title()}")
    print(f"Population: {population}")
    
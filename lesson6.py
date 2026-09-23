# shuga_dict = {
#     "first_name": "Melissa",
#     "last_name": "Violet",
#     "city": "Kampala",
#     "age": 22,
#     "status": "single",
#     "course": "Computer Science",
#     "hobby" : "music",
#     "aspiration": "piano"
# }

# print(shuga_dict["first_name"])
# something = shuga_dict["status"]
# age = shuga_dict["age"]

# print(f"Melissa is actually very {something}, she isn't seeing anyone. In real life she has actually never dated anyone.")

# print(f"Shuga was {age} years old when she decided to actually focus on herself, love herself more, fight jealous and change her life for the better.")

# print(f"Shuga lives in {shuga_dict["city"]}.")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())
names = ["Shuga", "Kezia", "Violet", "Janet", "Nina", "Britah"]
print(f" These {names[-1]} girl are actually very amazing.")

names[0] = "Melissa"
print(names)

names.append("Jordan")
print(names)

names.insert(0, "LoveJoy")
print(names)

del names[-3]
print(names)

new_name = names.pop(0)
print(f"I am definitely naming one of my children {new_name}!")

names.remove("Kezia")
print(names)

places = ["switzerland", "australia","netherlands","norway","southafrica", "italy","greece"]
print(places)

print(sorted(places,reverse=True))
print(f"I want to visit {len(places)} countries.")
numbers = []
for value in range(1,21, 2):
    numbers.append(value)
print(numbers)
print(sum(numbers))
print(min(numbers))
print(max(numbers))

multiples = []
for num in range(1,11):
    multiples.append(num*3)
print(multiples)

cubes = [num**3 for num in range(1,11)]
print(cubes)

names = ["Shuga", "Kezia", "Violet", "Janet", "Nina", "Britah"]
other_names = names[:]
names.append("Jezrel")
other_names.append("Jezeel")
print(names)
print(other_names)

print("--------------------------------------------------------------")

for name in names:
    print(name)

print("--------------------------------------------------------------")

for other in other_names:
    print(other)

my_names = ("Shuga", "Kezia", "Violet", "Janet", "Nina", "Britah")
for name in my_names:
    print(name)
# If statements

flowers = ["tulips", "daffodils", "daisies", "roses", "sunflowers", "lillies"]

for flower in flowers:
    if flower == "roses" or "tulips":
        print(flower.title())

flower = "roses"
for flower in flowers:
    if flower in flowers:
        print(flower)


flower = "lilly"
print("Is flower == 'lilly', I predict True")
print(flower == "lilly")

age = 12

if age < 4:
    price = 20
elif age < 18:
    price = 40
elif age > 65:
    price = 50
elif age >= 65:
    price = 60
print(f"Your price is &{price}.")




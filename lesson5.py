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
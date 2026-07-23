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